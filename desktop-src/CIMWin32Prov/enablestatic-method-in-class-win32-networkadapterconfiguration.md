---
description: The EnableStatic WMI class method enables static TCP/IP addressing for the target network adapter. As a result, DHCP for this network adapter is disabled.
ms.assetid: d0076424-58c0-4cfe-b55b-44c0f2620388
ms.tgt_platform: multiple
title: EnableStatic method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.EnableStatic
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# EnableStatic method of the Win32\_NetworkAdapterConfiguration class

The **EnableStatic** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method enables static TCP/IP addressing for the target network adapter. As a result, DHCP for this network adapter is disabled.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 EnableStatic(
  [in] string IPAddress[],
  [in] string SubnetMask[]
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Lists all of the static IP addresses for the current network adapter.

Example: 155.34.22.0.

</dd> <dt>

*SubnetMask* \[in\]
</dt> <dd>

Subnet masks that complement the values in the *IPAddress* parameter.

Example: 255.255.0.0.

</dd> </dl>

## Return value

Returns a value of 0 (zero) for a successful completion when a reboot is not required, 1 (one) for a successful completion when a reboot is required, and any other number if there is an error. For more information on error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion, no reboot required**
</dt> <dd>

0

Successful completion, no reboot required.

</dd> <dt>

**Successful completion, reboot required**
</dt> <dd>

1

Successful completion, reboot required.

</dd> <dt>

**Method not supported on this platform**
</dt> <dd>

64

Method not supported on this platform.

</dd> <dt>

**Unknown failure**
</dt> <dd>

65

Unknown failure.

</dd> <dt>

**Invalid subnet mask**
</dt> <dd>

66

Invalid subnet mask.

</dd> <dt>

**An error occurred while processing an Instance that was returned**
</dt> <dd>

67

An error occurred while processing an instance that was returned.

</dd> <dt>

**Invalid input parameter**
</dt> <dd>

68

Invalid input parameter.

</dd> <dt>

**More than 5 gateways specified**
</dt> <dd>

69

More than five gateways specified.

</dd> <dt>

**Invalid IP address**
</dt> <dd>

70

Invalid IP address.

</dd> <dt>

**Invalid gateway IP address**
</dt> <dd>

71

Invalid gateway IP address.

</dd> <dt>

**An error occurred while accessing the Registry for the requested information**
</dt> <dd>

72

An error occurred while accessing the registry for the requested information.

</dd> <dt>

**Invalid domain name**
</dt> <dd>

73

Invalid domain name.

</dd> <dt>

**Invalid host name**
</dt> <dd>

74

Invalid host name.

</dd> <dt>

**No primary/secondary WINS server defined**
</dt> <dd>

75

No primary or secondary WINS server defined.

</dd> <dt>

**Invalid file**
</dt> <dd>

76

Invalid file.

</dd> <dt>

**Invalid system path**
</dt> <dd>

77

Invalid system path.

</dd> <dt>

**File copy failed**
</dt> <dd>

78

File copy failed.

</dd> <dt>

**Invalid security parameter**
</dt> <dd>

79

Invalid security parameter.

</dd> <dt>

**Unable to configure TCP/IP service**
</dt> <dd>

80

Unable to configure TCP/IP service.

</dd> <dt>

**Unable to configure DHCP service**
</dt> <dd>

81

Unable to configure DHCP service. For more information, see the Remarks section.

</dd> <dt>

**Unable to renew DHCP lease**
</dt> <dd>

82

Unable to renew DHCP lease.

</dd> <dt>

**Unable to release DHCP lease**
</dt> <dd>

83

Unable to release DHCP lease.

</dd> <dt>

**IP not enabled on adapter**
</dt> <dd>

84

IP not enabled on adapter.

</dd> <dt>

**IPX not enabled on adapter**
</dt> <dd>

85

IPX not enabled on adapter.

</dd> <dt>

**Frame/network number bounds error**
</dt> <dd>

86

Frame or network number bounds error.

</dd> <dt>

**Invalid frame type**
</dt> <dd>

87

Invalid frame type.

</dd> <dt>

**Invalid network number**
</dt> <dd>

88

Invalid network number.

</dd> <dt>

**Duplicate network number**
</dt> <dd>

89

Duplicate network number.

</dd> <dt>

**Parameter out of bounds**
</dt> <dd>

90

Parameter out of bounds.

</dd> <dt>

**Access denied**
</dt> <dd>

91

Access denied.

</dd> <dt>

**Out of memory**
</dt> <dd>

92

Out of memory.

</dd> <dt>

**Already exists**
</dt> <dd>

93

Already exists.

</dd> <dt>

**Path, file or object not found**
</dt> <dd>

94

Path, file, or object not found.

</dd> <dt>

**Unable to notify service**
</dt> <dd>

95

Unable to notify service.

</dd> <dt>

**Unable to notify DNS service**
</dt> <dd>

96

Unable to notify DNS service.

</dd> <dt>

**Interface not configurable**
</dt> <dd>

97

Interface not configurable.

</dd> <dt>

**Not all DHCP leases could be released/renewed**
</dt> <dd>

98

Not all DHCP leases could be released or renewed.

</dd> <dt>

**DHCP not enabled on adapter**
</dt> <dd>

100

DHCP not enabled on adapter.

</dd> <dt>

**2147786788**
</dt> <dd>

Write lock not enabled. For more information, see [**INetCfgLock::AcquireWriteLock**](/previous-versions/windows/hardware/network/ff547914(v=vs.85)).

</dd> <dt>

**Other**
</dt> <dd>

101 4294967295

</dd> </dl>

## Remarks

When using **EnableStatic** to change the IP address of the remote computer, while being connected through that adapter, you will likely loose connection to the remote computer, and receive an RPC not available error-message. (the settings are changed however). To avoid this scenario, consider changing the Gateway and/or DNS-settings prior to setting the adapter's IP-address.

When using **EnableStatic** to give an adapter a static IP configuration, the function returns an "81 - Unable to configure DHCP service" if the adapter is already configured with a static address. However, the function still succeeds in setting with the new operation.

## Examples

The [Static IP and then join to a domain](https://Gallery.TechNet.Microsoft.Com/Static-IP-and-then-join-to-130d4b8a) PowerShell code sample, on TechNet Gallery, uses **EnableStatic** to add a static IP to a local machine.

The [Assign a Static IP Address](https://Gallery.TechNet.Microsoft.Com/8979c752-8288-4a18-b5ed-f3b79f013f4a) VBScript code example, on TechNet Gallery, uses **EnableStatic** to set the IP address of a computer.

The following VBScript sample demonstrates how to disable DHCP use on an instance of [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md). In this case we specify the adapter with an Index of 0. The correct index should be selected from Win32\_NetworkAdapter instances for other interfaces.

> [!Note]  
> This script only applies to NT-based systems Change the ipaddr and subnet variables below to the values you wish to apply to the adapter.

 


```VB
Set Adapter = GetObject("winmgmts:Win32_NetworkAdapterConfiguration=1")

ipaddr = Array("1.1.1.1")
subnet = Array("255.255.255.0")


RetVal = Adapter.EnableStatic(ipaddr,subnet)

if RetVal = 0 then 
 WScript.Echo "DHCP disabled, using static IP address"
else 
 WScript.Echo "DHCP disable failed"
end if
```



The following Perl sample demonstrates how to disable DHCP use on an instance of [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md). In this case we specify the adapter with an Index of 0. The correct index should be selected from Win32\_NetworkAdapter instances for other interfaces.

> [!Note]  
> This script only applies to NT-based systems Change the ipaddr and subnet variables below to the values you wish to apply to the adapter.

 


```
use strict;
use Win32::OLE;

my ($Adapter, @ipaddr, @subnet, $RetVal);  
eval { $Adapter = 
 Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2:Win32_NetworkAdapterConfiguration.Index=\"0\""); };

unless ($@) 
{
 push @ipaddr, "192.168.144.107";
 push @subnet, "255.255.255.0";

 $RetVal = $Adapter->EnableStatic(\@ipaddr, \@subnet);

 if ($RetVal == 0) 
 {
  print "\nDHCP disabled, using static IP address\n";
 }
 else 
 {
  print "\nDHCP disable failed\n";
 }
}
else
{
 print STDERR "\n", Win32::OLE->LastError, "\n";
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> <dt>

[**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md)
</dt> <dt>

[WMI Tasks: Networking](/windows/desktop/WmiSdk/wmi-tasks--networking)
</dt> <dt>

[WMI Tasks: Accounts and Domains](/windows/desktop/WmiSdk/wmi-tasks--accounts-and-domains)
</dt> <dt>

[IPv6 and IPv4 Support in WMI](/windows/desktop/WmiSdk/ipv6-and-ipv4-support-in-wmi)
</dt> </dl>

 

