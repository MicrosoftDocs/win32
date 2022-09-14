---
description: The EnableDHCP WMI class method enables the Dynamic Host Configuration Protocol (DHCP) for service with this network adapter. DHCP allows IP addresses to be dynamically allocated.
ms.assetid: 8c61d731-77a3-4ef4-bad9-26edaca60892
ms.tgt_platform: multiple
title: EnableDHCP method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.EnableDHCP
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# EnableDHCP method of the Win32\_NetworkAdapterConfiguration class

The **EnableDHCP** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method enables the Dynamic Host Configuration Protocol (DHCP) for service with this network adapter. DHCP allows IP addresses to be dynamically allocated.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 EnableDHCP();
```



## Parameters

This method has no parameters.

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

Unable to configure DHCP service.

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

DHCP not enabled on the adapter.

</dd> <dt>

**Other**
</dt> <dd>

101 4294967295

</dd> </dl>

## Remarks

This method does not clears any static default gateways present on the machine.

## Examples

The [Enable DHCP and Assign DNS Servers](https://Gallery.TechNet.Microsoft.Com/7b1cec46-bdb8-4afc-b240-9789eefce6de) VBScript code sample on TechNet Gallery uses EnableDHCP to enable DHCP and assign DNS servers to a computer.

The following VBScript code sample demonstrates how to enable DHCP use on an instance of [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md) . In this case we specify the adapter with an Index of 0. The correct index should be selected from Win32\_NetworkAdapter instances for other interfaces.

> [!Note]  
> Supported on NT platforms only.

 


```VB
Set Adapter = GetObject("winmgmts:Win32_NetworkAdapterConfiguration=0")

RetVal = Adapter.EnableDHCP()

if RetVal = 0 then 
 WScript.Echo "DHCP Enabled"
else 
 WScript.Echo "DHCP enable failed"
end if
```



The following Perl code sample demonstrates how to enable DHCP use on an instance of [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md) . In this case we specify the adapter with an Index of 0. The correct index should be selected from Win32\_NetworkAdapter instances for other interfaces.

> [!Note]  
> Supported on NT platforms only.

 


```
use strict;
use Win32::OLE;

my ( $Adapter, $RetVal );

eval { $Adapter = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2")->
       Get("Win32_NetworkAdapterConfiguration=0"); };
unless ($@)
{
 print "\n";
 $RetVal = $Adapter->EnableDHCP();
 if ( $RetVal == 0)
 {
  print "DHCP Enabled\n";
 }
 else
 {
  print "DHCP enable failed\n";
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
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

 

