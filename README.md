# python3-network-config-generator

This script generate Cisco Nexus configuration using the power of python and Jinja2 templates based on the attached excel sheet. There are some sample data provided in the excel sheet.

I have been working on multiple datacenter green field deployments where i use excel sheet for planning. If the excel sheet is filled properly in the planning phase, all the configuration can be extracted from the excel sheet without even the physical switches are arrived.

This script currently generated configuration for Cisco and Cumulus. Cisco only have support for L2 Spine/Leaf with VPC. Cumulus Can generated both L2 and L3 Spine/Leaf architecture

Current features for Cisco Nexus
- Access interface configurations
- Uplink interface configurations
- VLAN configurations
- VPC configurations
- FHRP configurations
- OSPF configurations
- VRF configurations
- Management configurations

Current features for Cumulus
- Access interface configurations
- Uplink interface configurations
- VLAN configurations
- MLAG configurations
- FHRP configurations
- BGP configurations
- EVPN configurations
- VRF configurations
- Management configurations

For any questions, please contact me on linkedin: www.linkedin.com/in/abdbasit
