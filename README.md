# meraki-ddns

This is a very simple tool that creates and updates a Route53 `A` record that points to a network that doesn't have a static IP address. Runs on Alpine Linux and takes up about ~26MBs of your memory.

While Meraki already offers this feature on its MX firewalls by giving you a `dynamic-m.com` hostname, this tool allows you to have this functionality with *any* kind of Meraki device. Useful for networks where you might have only an MR access point.

To use this tool, you need:
- A Cisco Meraki device of any kind, deployed and running inside said network
- A domain name pointing to a hosted zone inside your Route53 account
- API access for both your Meraki dashboard and your Route53 account, and
- A device to run this container on (this could be anywhere in the world)

## Setup
Clone this repo into a directory, and navigate inside.

Edit the Dockerfile with a text editor of your choosing, and replace the environment variables with your parameters:

- `AWS_ACCESS_KEY_ID` and  `AWS_SECRET_ACCESS_KEY`: An Access Key pair that has write permissions on the hosted zone you want to use
- `R53_HOSTED_ZONE`: Your Hosted Zone ID.
- `R53_FQDN`: The full domain name that you want to update, with the subdomain included (if applicable). For instance, if your hosted zone was `example.com` and you wanted `whatever.example.com` to point to your network, you would set this as `whatever.example.com`.
- `R53_TTL`: The TTL (time-to-live) value that you want for your `A` record, in seconds.
- `UPDATE_FREQ`: The time that the script sleeps for before checking for updates again, in seconds.
- `MERAKI_API_KEY`: The API key of a Cisco Meraki account that has at least read-only access to the network and device that you want to use.
- `MERAKI_NETWORK_ID`:  The ID of your network on the Meraki dashboard. Should look something like `L_000000000000000000`.
- `MERAKI_DEVICE_SN`: The serial number of the device that you want to use. Should look something like `XXXX-XXXX-XXXX`.

Run `make`. Your container will be built and run automatically.

## Roadmap
- Add commands to pull pre-built image from Docker Hub
- Add Cisco Umbrella address update functionality through DNS-O-Matic
- Implement a better configuration system and allow the script to be run over multiple networks across multiple orgs
