#! /usr/bin/env python
"""
Script to generate Network configuration files by 
combining data from excel files with Jinja templates 
"""


from openpyxl import load_workbook
from jinja2 import Template

templates_dir = "./templates"
outputcfg_dir = "./outputconfigs"

xwb_source_file = "ip_list_v0.xlsx"
access_template_file = f"{templates_dir}/nx_int_access.j2"
uplink_template_file = f"{templates_dir}/nx_int_uplink.j2"
vlan_template_file   = f"{templates_dir}/nx_vlans.j2"
fhrp_template_file   = f"{templates_dir}/nx_fhrp.j2"
portch_template_file = f"{templates_dir}/nx_portchannel.j2"
nxos_template_file   = f"{templates_dir}/nx_base.j2"
ospf_template_file   = f"{templates_dir}/nx_ospf.j2"
mgmt_template_file   = f"{templates_dir}/nx_mgmt.j2"

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
with open(access_template_file) as f:
    access_template = Template(f.read(), keep_trailing_newline=True)

with open(uplink_template_file) as f:
    uplink_template = Template(f.read(), keep_trailing_newline=True)

with open(vlan_template_file) as f:
    vlan_template = Template(f.read(), keep_trailing_newline=True)

with open(fhrp_template_file) as f:
    fhrp_template = Template(f.read(), keep_trailing_newline=True)

with open(portch_template_file) as f:
    portch_template = Template(f.read(), keep_trailing_newline=True)

with open(nxos_template_file) as f:
    nxos_template = Template(f.read(), keep_trailing_newline=True)

with open(ospf_template_file) as f:
    ospf_template = Template(f.read(), keep_trailing_newline=True)

with open(mgmt_template_file) as f:
    mgmt_template = Template(f.read(), keep_trailing_newline=True)


# Open up the excel file containing the data 
xwb = load_workbook(xwb_source_file, data_only=True)
xsheet_sw = xwb["switchnames"]
xsheet_vl = xwb["vlans"]
xsheet_ip = xwb["IP_list"]
xsheet_ul = xwb["SW_uplinks"]
xsheet_ospf = xwb["ospf"]

#extract columns from switchnames sheet
hstnm_sw = xsheet_sw['A']
obmad_sw = xsheet_sw['B']
obmmk_sw = xsheet_sw['C']
obmgw_sw = xsheet_sw['D']
obmvf_sw = xsheet_sw['E']
ibmad_sw = xsheet_sw['F']
ibmmk_sw = xsheet_sw['G']
ibmgw_sw = xsheet_sw['H']
ibmvf_sw = xsheet_sw['I']
domnm_sw = xsheet_sw['J']

#extract columns from vlan sheet
vlnum_vl = xsheet_vl['A']
vlnam_vl = xsheet_vl['B']
vlnet_vl = xsheet_vl['C']
vlmsk_vl = xsheet_vl['D']
vlbit_vl = xsheet_vl['E']
vlgtw_vl = xsheet_vl['F']
fhsw1_vl = xsheet_vl['G']
fhpr1_vl = xsheet_vl['H']
fhad1_vl = xsheet_vl['I']
fhsw2_vl = xsheet_vl['J']
fhpr2_vl = xsheet_vl['K']
fhad2_vl = xsheet_vl['L']
fhprt_vl = xsheet_vl['M']
fhvrf_vl = xsheet_vl['N']

# extract columns from IP_List sheet for endpoint interfaces
hstnm_ep = xsheet_ip['A']
hstpt_ep = xsheet_ip['B']
swtch_ep = xsheet_ip['C']
intid_ep = xsheet_ip['D']
intno_ep = xsheet_ip['E']
vlnid_ep = xsheet_ip['F']
prpse_ep = xsheet_ip['G']
prtch_ep = xsheet_ip['H']
mlgid_ep = xsheet_ip['I']
intrl_ep = xsheet_ip['J']
swpad_ep = xsheet_ip['K']
swpmk_ep = xsheet_ip['L']

# extract columns from Uplink sheet for switch to switch interfaces
hstnm_ul = xsheet_ul['A']
hstpt_ul = xsheet_ul['B']
swtch_ul = xsheet_ul['C']
intid_ul = xsheet_ul['D']
intno_ul = xsheet_ul['E']
vlnid_ul = xsheet_ul['F']
prpse_ul = xsheet_ul['G']
prtch_ul = xsheet_ul['H']
mlgid_ul = xsheet_ul['I']
intrl_ul = xsheet_ul['J']
swpad_ul = xsheet_ul['K']
swpmk_ul = xsheet_ul['L']

# extract columns from ospf sheet for routing
swtch_ospf = xsheet_ospf['A']
loopb_opsf = xsheet_ospf['B']
rtrid_ospf = xsheet_ospf['C']
araid_ospf = xsheet_ospf['D']
prcid_ospf = xsheet_ospf['E']
aukey_ospf = xsheet_ospf['F']

#config j2 template as functions for access interfaces
def access_generate (int_ty, int_no, vln_no, hst_nm, hst_pt, int_pr, prt_ch, int_rl, swp_ad, swp_mk):
    access_config = access_template.render(
        inttype  = int_ty,
        int_num  = int_no,
        vlan     = vln_no,
        hostname = hst_nm,
        link     = hst_pt,
        purpose  = int_pr,
        portch   = prt_ch,
        introle  = int_rl,
        ipaddr   = swp_ad,
        subnet   = swp_mk,
        )
    return(access_config)

#config j2 template as functions for uplink interfaces
def uplink_generate (int_ty, int_no, vln_no, hst_nm, hst_pt, int_pr, prt_ch, int_rl, swp_ad, swp_mk):
    uplink_config = uplink_template.render(
        inttype  = int_ty,
        int_num  = int_no,
        vlanid   = vln_no,
        hostname = hst_nm,
        link     = hst_pt,
        purpose  = int_pr,
        portch   = prt_ch,
        introle  = int_rl,
        ipaddr   = swp_ad,
        subnet   = swp_mk,
        )
    return(uplink_config)

#config j2 template as function for portchannel interfaces
def portch_generate (pch_id, mlg_id, hst_nm, vln_no, int_rl):
    portch_config = portch_template.render(
        portchid  = pch_id,
        mlagid    = mlg_id,
        hostname  = hst_nm,
        vlanid    = vln_no,
        introle   = int_rl,
    )
    return(portch_config)


#config j2 template as functions for vlans
def vlan_generate (vln_no, vln_nm):
    vlan_gen= vlan_template.render(
        vlanid   = vln_no,
        vlanname = vln_nm,
        )
    return(vlan_gen)

#config j2 template as functions for fhrp
def fhrp_generate (vln_no, vln_nm, fhr_ad, fhr_nt, vln_gw, fhr_pr, fhr_vf, fhr_pt):
    fhrp_gen= fhrp_template.render(
        vlanid          = vln_no,
        vlandescription = vln_nm,
        fhrpipaddress   = fhr_ad,
        bitmask         = fhr_nt,
        fhrpgroup       = vln_no,
        vlangateway     = vln_gw,
        fhrppriority    = fhr_pr,
        interfacevrf    = fhr_vf,
        fhrpprotocol    = fhr_pt,

        )
    return(fhrp_gen)

#config j2 template as function for ospf
def ospf_generate (prc_id, rtr_id):
    ospf_config = ospf_template.render(
        processid = prc_id,
        routerid  = rtr_id,
    )
    return(ospf_config)

def mgmt_generate (obm_vf, obm_ad, obm_mk, obm_gw):
    mgmt_config = mgmt_template.render(
        obmgmtvrf = obm_vf,
        obipaddr  = obm_ad,
        obsubnet  = obm_mk,
        obgateway = obm_gw,
    )
    return(mgmt_config)

# Save the final configuraiton to a file 
def save_config (swc_nm, dmn_nm, acc_cf, upl_cf, vln_cf, fhr_cf, pch_cf, ospf, mgt_cf):
    save_config = nxos_template.render(
        hostname     = swc_nm,
        domainname   = dmn_nm,
        ospfconfigs  = ospf,
        vlanconfigs  = vln_cf,
        fhrpconfigs  = fhr_cf,
        portchconfigs= pch_cf,
        intf_access  = acc_cf,
        intf_uplink  = upl_cf,
        mgmtconfigs  = mgt_cf,
    )
#open file and save configuration with switch hostname
    with open(f"{outputcfg_dir}/{swc_nm}" + "config.txt", "w") as f:
        f.write(save_config)



#Main function to generate the configurations for all the templates
for x in range (1, xsheet_sw.max_row):
    access_configs = ""
    uplink_configs = ""
    portch_configs = ""
    vlanid_configs = ""
    fhrp_configs   = ""
    ospf_configs   = ""
    mgmt_configs   = ""

    #generate management configuration of the switch
    mgmt_configs = mgmt_generate (obmvf_sw[x].value, obmad_sw[x].value, obmmk_sw[x].value, obmgw_sw[x].value)

    #Loop through IP list sheet 
    for y in range (1, xsheet_ip.max_row):
        if swtch_ep[y].value == hstnm_sw[x].value:
            # find the switchname in the call and call access config function for it to connected endpoint
            access_config = access_generate(intid_ep[y].value, intno_ep[y].value, vlnid_ep[y].value,
            hstnm_ep[y].value, hstpt_ep[y].value, prpse_ep[y].value, prtch_ep[y].value, intrl_ep[y].value,
            swpad_ep[y].value, swpmk_ep[y].value )

            # Append this interface configuration to the full configuration 
            access_configs += access_config

            #check if portchannel is configured, if yes then generate porchannel configurations
            if prtch_ep[y].value != None:
                portch_config = portch_generate(prtch_ep[y].value, mlgid_ep[y].value, hstnm_ep[y].value,
                vlnid_ep[y].value, intrl_ep[y].value)
                portch_configs += portch_config

    #Loop through Switch uplink sheet
    for y in range (1, xsheet_ul.max_row):
        if swtch_ul[y].value == hstnm_sw[x].value:
            # find the switchname in the call and call uplink config function for it to connected endpoint
            uplink_config = uplink_generate(intid_ul[y].value, intno_ul[y].value, vlnid_ul[y].value,
            hstnm_ul[y].value, hstpt_ul[y].value, prpse_ul[y].value, prtch_ul[y].value, intrl_ul[y].value,
            swpad_ul[y].value, swpmk_ul[y].value )

            # Append this interface configuration to the full configuration 
            uplink_configs += uplink_config

            #check if portchannel is configured, if yes then generate porchannel configurations
            if prtch_ep[y].value != None:
                portch_config = portch_generate(prtch_ep[y].value, mlgid_ep[y].value, hstnm_ep[y].value,
                vlnid_ep[y].value, intrl_ep[y].value)
                portch_configs += portch_config

    #generate vlan and fhrp configurations        
    for y in range (1, xsheet_vl.max_row):
        #generate vlan configuration
        if swtch_ep[y].value == hstnm_sw[x].value:
            vlan_config = vlan_generate (vlnum_vl[y].value, vlnam_vl[y].value)

            #append vlan configurations together
            vlanid_configs += vlan_config

        #generate fhrp configuration
        if fhsw1_vl[y].value == hstnm_sw[x].value:
            fhrp_config = fhrp_generate(vlnum_vl[y].value, vlnam_vl[y].value, fhad1_vl[y].value, vlbit_vl[y].value,
            vlgtw_vl[y].value, fhpr1_vl[y].value, fhvrf_vl[y].value, fhprt_vl[y].value)

            #append fhrp1 configuration
            fhrp_configs += fhrp_config

        elif fhsw2_vl[y].value == hstnm_sw[x].value:
            fhrp_config = fhrp_generate(vlnum_vl[y].value, vlnam_vl[y].value, fhad2_vl[y].value, vlbit_vl[y].value,
            vlgtw_vl[y].value, fhpr2_vl[y].value, fhvrf_vl[y].value, fhprt_vl[y].value)

            #append fhrp2 configuration
            fhrp_configs += fhrp_config

    #generate ospf configurations
    for y in range (1, xsheet_ospf.max_row):
        if swtch_ospf[y].value == hstnm_sw[x].value:
            ospf_config = ospf_generate (prcid_ospf[y].value, rtrid_ospf[y].value)
            
            # Append ospf configurations together
            ospf_configs += ospf_config

    #call save_config to save configuration for a switch
    save_config(hstnm_sw[x].value, domnm_sw[x].value, access_configs, uplink_configs, portch_configs, vlanid_configs,
    fhrp_configs, ospf_configs, mgmt_configs)


