from cisco import CiscoIosSSH
from cisco import CiscoAsaSSH
from cisco import CiscoNxosSSH
from cisco import CiscoXrSSH
from arista import AristaSSH
from hp import HPProcurveSSH

CLASS_MAPPER = {
    'cisco_ios'     : CiscoIosSSH,
    'cisco_xe'      : CiscoIosSSH,
    'cisco_asa'     : CiscoAsaSSH,
    'cisco_nxos'    : CiscoNxosSSH,
    'cisco_xr'      : CiscoXrSSH,
    'arista_eos'    : AristaSSH,
    'hp_procurve'   : HPProcurveSSH,
    'f5_ltm_ssh'    : F5LtmSSH,
}

def ssh_dispatcher(device_type):
    '''
    Select the class to be instantiated based on vendor/platform
    '''

    return CLASS_MAPPER[device_type]
