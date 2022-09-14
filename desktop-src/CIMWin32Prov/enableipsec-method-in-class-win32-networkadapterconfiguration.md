---
description: The EnableIPSec&\#8194;WMI class method enables Internet Protocol security (IPsec) on a TCP/IP-enabled network adapter.
ms.assetid: 0a45d864-606d-4adb-9b51-62d46a0d68b1
ms.tgt_platform: multiple
title: EnableIPSec method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.EnableIPSec
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# EnableIPSec method of the Win32\_NetworkAdapterConfiguration class

The **EnableIPSec** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method enables Internet Protocol security (IPsec) on a TCP/IP-enabled network adapter.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 EnableIPSec(
  [in] string IPSecPermitTCPPorts[],
  [in] string IPSecPermitUDPPorts[],
  [in] string IPSecPermitIPProtocols[]
);
```



## Parameters

<dl> <dt>

*IPSecPermitTCPPorts* \[in\]
</dt> <dd>

List of ports to be granted access permission for TCP. A numeric value of 0 (zero) indicates access permission is granted for all ports. An empty array indicates that no ports are to be granted access permission.

</dd> <dt>

*IPSecPermitUDPPorts* \[in\]
</dt> <dd>

List of ports to be granted access permission for UDP. A numeric value of 0 (zero) indicates access permission is granted for all ports. An empty array indicates that no ports are to be granted access permission.

</dd> <dt>

*IPSecPermitIPProtocols* \[in\]
</dt> <dd>

List of protocols permitted to run over the IP. A numeric value of 0 (zero) indicates access permission is granted for all protocols. An empty array indicates that no protocols are granted access permission.

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

Ports are secured only when the **IPFilterSecurityEnabled** property in [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md) is **true**.

## Examples

The [Enable IPSec on a Network Adapter](https://Gallery.TechNet.Microsoft.Com/ff821218-c392-42fb-a77c-c3eab899587c) VBScript sample, on TechNet Gallery, uses **EnableIPSec** to enable IP security for a network adapter.

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

 

