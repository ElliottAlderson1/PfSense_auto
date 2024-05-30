# Automated Pfsense firewall provisioning

Automate the provisioning of high-availability PfSense firewalls. The objective is to create an automated process to generate PfSense configuration files from template using configurations provided in an inventory file.

# Project Overview
 Currently, our environment requires manual provisioning of High-Availability virtual PfSense firewalls. This process is slow and error prone - taking 2 hours for basic functionality, up to 6 hours to include the full rule listing, and potentially longer for troubleshooting of errors. 

## Objective
 Create an automated process to generate PfSense configuration files from a template using configurations provided in an inventory file. 

## End Goal
The configuration file must accomplish the following:
 - List and apply all required VLANs
 - Create and activate all VLAN subinterfaces.
 - Create firewall rules provided in the template customized for the 
network requested by the user.
 - Configure High-Availability over the PfSync VLAN interface and ensure all configurations are mirrored to the subordinate PfSense
 - Create another user separate from the default 'admin' user.
 - Set dhcp-relay to a given IP address and assert all interfaces are advertising this server.
