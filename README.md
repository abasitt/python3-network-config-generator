# python3-network-config-generator

This script generate Cisco Nexus configuration using the power of python and Jinja2 templates based on the attached excel sheet. There are some sample data provided in the excel sheet.

I have been working on multiple datacenter green field deployments where i use excel sheet for planning. If the excel sheet is filled properly in the planning phase, all the configuration can be extracted from the excel sheet without even the physical switches are arrived.

Even though i wrote the script for Cisco but it is very easy to modify Jinja2 and use it for other vendors. I have used the same script with Dell by just modifying Jinj2 templates. I will be uploading scripts for other vendors here

Current features
- Access interface configurations
- Uplink interface configurations
- VLAN configurations
- FHRP configurations
- OSPF configurations
- VRF configurations
- Management configurations
