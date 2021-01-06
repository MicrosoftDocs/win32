---
description: The SetGateways &\#32; WMI class method specifies a list of gateways for routing packets to a subnet that is different from the subnet that the network adapter is connected to.
ms.assetid: 240f7aff-7a07-4e0d-af30-7bcabb68c736
ms.tgt_platform: multiple
title: SetGateways method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.SetGateways
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetGateways method of the Win32\_NetworkAdapterConfiguration class

The **SetGateways** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method specifies a list of gateways for routing packets to a subnet that is different from the subnet that the network adapter is connected to.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetGateways(
  [in]           string DefaultIPGateway[],
  [in, optional] uint16 GatewayCostMetric[]
);
```



## Parameters

<dl> <dt>

*DefaultIPGateway* \[in\]
</dt> <dd>

List of IP addresses to gateways where network packets are routed.

</dd> <dt>

*GatewayCostMetric* \[in, optional\]
</dt> <dd>

Assigns a value that ranges from 1 to 9999, which is used to calculate the fastest and most reliable routes. The values of this parameter correspond with the values in the *DefaultIPGateway* parameter. The default value for a gateway is 1.

</dd> </dl>

## Return value

Returns a value of 0 (zero) for a successful completion when a reboot is not required, 1 (one) for a successful completion when a reboot is required, and any other value if there is an error. For more information on error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion, no reboot required**
</dt> <dd>

0

</dd> <dt>

**Successful completion, reboot required**
</dt> <dd>

1

</dd> <dt>

**Method not supported on this platform**
</dt> <dd>

64

Method not supported when the NIC is in DHCP mode.

</dd> <dt>

**Unknown failure**
</dt> <dd>

65

</dd> <dt>

**Invalid subnet mask**
</dt> <dd>

66

</dd> <dt>

**An error occurred while processing an Instance that was returned**
</dt> <dd>

67

</dd> <dt>

**Invalid input parameter**
</dt> <dd>

68

</dd> <dt>

**More than 5 gateways specified**
</dt> <dd>

69

</dd> <dt>

**Invalid IP address**
</dt> <dd>

70

</dd> <dt>

**Invalid gateway IP address**
</dt> <dd>

71

</dd> <dt>

**An error occurred while accessing the Registry for the requested information**
</dt> <dd>

72

</dd> <dt>

**Invalid domain name**
</dt> <dd>

73

</dd> <dt>

**Invalid host name**
</dt> <dd>

74

</dd> <dt>

**No primary/secondary WINS server defined**
</dt> <dd>

75

</dd> <dt>

**Invalid file**
</dt> <dd>

76

</dd> <dt>

**Invalid system path**
</dt> <dd>

77

</dd> <dt>

**File copy failed**
</dt> <dd>

78

</dd> <dt>

**Invalid security parameter**
</dt> <dd>

79

</dd> <dt>

**Unable to configure TCP/IP service**
</dt> <dd>

80

</dd> <dt>

**Unable to configure DHCP service**
</dt> <dd>

81

</dd> <dt>

**Unable to renew DHCP lease**
</dt> <dd>

82

</dd> <dt>

**Unable to release DHCP lease**
</dt> <dd>

83

</dd> <dt>

**IP not enabled on adapter**
</dt> <dd>

84

</dd> <dt>

**IPX not enabled on adapter**
</dt> <dd>

85

</dd> <dt>

**Frame/network number bounds error**
</dt> <dd>

86

</dd> <dt>

**Invalid frame type**
</dt> <dd>

87

</dd> <dt>

**Invalid network number**
</dt> <dd>

88

</dd> <dt>

**Duplicate network number**
</dt> <dd>

89

</dd> <dt>

**Parameter out of bounds**
</dt> <dd>

90

</dd> <dt>

**Access denied**
</dt> <dd>

91

</dd> <dt>

**Out of memory**
</dt> <dd>

92

</dd> <dt>

**Already exists**
</dt> <dd>

93

</dd> <dt>

**Path, file or object not found**
</dt> <dd>

94

</dd> <dt>

**Unable to notify service**
</dt> <dd>

95

</dd> <dt>

**Unable to notify DNS service**
</dt> <dd>

96

</dd> <dt>

**Interface not configurable**
</dt> <dd>

97

</dd> <dt>

**Not all DHCP leases could be released/renewed**
</dt> <dd>

98

</dd> <dt>

**DHCP not enabled on adapter**
</dt> <dd>

100

</dd> <dt>

**Other**
</dt> <dd>

101 4294967295

</dd> </dl>

## Remarks

This method only works when the Network Interface Card (NIC) is in the static IP mode.

To clear the gateway, set your gateway to the same IP you use on [**EnableStatic**](enablestatic-method-in-class-win32-networkadapterconfiguration.md).

## Examples

The [Modify the Gateways for a Network Adapter](https://Gallery.TechNet.Microsoft.Com/9ea7670b-f68f-4efb-9cd2-7c299a8f657f) VBScript sample configures two gateways for a network adapter.

The [Assign a Static IP Address](https://Gallery.TechNet.Microsoft.Com/8979c752-8288-4a18-b5ed-f3b79f013f4a) VBScript sample sets the IP address and gateway of a computer.

The [Static IP and then join to a domain](https://Gallery.TechNet.Microsoft.Com/Static-IP-and-then-join-to-130d4b8a) PowerShell sample assists in rebuilding machines.

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

 

