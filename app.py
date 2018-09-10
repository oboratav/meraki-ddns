import os
import boto3
import time
from meraki import meraki

def get_device_wan_addr(key, network, serial):
    return meraki.getdeviceuplink(
        key,
        network,
        serial,
        suppressprint=True
    )[0]['publicIp']

def get_device_name(key, network, serial):
    return meraki.getdevicedetail(
        key,
        network,
        serial,
        suppressprint=True
    )["name"]

def change_record(client, hosted_zone, domain, addr, ttl, comment='Updated by meraki-ddns'):
    return client.change_resource_record_sets(
        HostedZoneId=hosted_zone,
        ChangeBatch={
            "Comment": comment,
            "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": domain,
                    "Type": "A",
                    "TTL": ttl,
                    "ResourceRecords": [{
                        "Value": addr
                        }]
                    }
                }]
            }
    )
    

def main():
    r53_client = boto3.client('route53')
    r53_hosted_zone = os.environ.get('R53_HOSTED_ZONE')
    r53_fqdn = os.environ.get('R53_FQDN')
    r53_ttl = int(os.environ.get('R53_TTL'))
    frequency = int(os.environ.get('UPDATE_FREQ'))

    meraki_key = os.environ.get('MERAKI_API_KEY')
    meraki_network = os.environ.get('MERAKI_NETWORK_ID')
    meraki_device_sn = os.environ.get('MERAKI_DEVICE_SN')
    #comment = "Updated to match {0}'s WAN address.".format(get_device_name(meraki_key, meraki_network, meraki_device_sn))
    while True:
            change_record(
                r53_client,
                r53_hosted_zone,
                r53_fqdn,
                get_device_wan_addr(meraki_key, meraki_network, meraki_device_sn),
                r53_ttl
            )
            time.sleep(frequency)

if __name__ == "__main__":
    main()