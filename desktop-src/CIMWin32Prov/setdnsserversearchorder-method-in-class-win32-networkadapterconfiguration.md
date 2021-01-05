---
description: The SetDNSServerSearchOrder &\#32; WMI class method uses an array of string elements to set the server search order.
ms.assetid: fce688fa-7264-4965-8e1c-138160e03a7e
ms.tgt_platform: multiple
title: SetDNSServerSearchOrder method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.SetDNSServerSearchOrder
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetDNSServerSearchOrder method of the Win32\_NetworkAdapterConfiguration class

The **SetDNSServerSearchOrder** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method uses an array of string elements to set the server search order.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetDNSServerSearchOrder(
  [in] string DNSServerSearchOrder[]
);
```



## Parameters

<dl> <dt>

*DNSServerSearchOrder* \[in\]
</dt> <dd>

List of server IP addresses to query for DNS servers.

Example: 130.215.24.1 or 157.54.164.1

</dd> </dl>

## Return value

Returns a value of 0 (zero) for a successful completion when no reboot is required, 1 (one) for a successful completion when a reboot is required, and a different number if there is an error. For more information on error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion, no reboot required** (0)
</dt> <dt>

**Successful completion, reboot required** (1)
</dt> <dt>

**Method not supported on this platform** (64)
</dt> <dt>

**Unknown failure** (65)
</dt> <dt>

**Invalid subnet mask** (66)
</dt> <dt>

**An error occurred while processing an Instance that was returned** (67)
</dt> <dt>

**Invalid input parameter** (68)
</dt> <dt>

**More than 5 gateways specified** (69)
</dt> <dt>

**Invalid IP address** (70)
</dt> <dt>

**Invalid gateway IP address** (71)
</dt> <dt>

**An error occurred while accessing the Registry for the requested information** (72)
</dt> <dt>

**Invalid domain name** (73)
</dt> <dt>

**Invalid host name** (74)
</dt> <dt>

**No primary/secondary WINS server defined** (75)
</dt> <dt>

**Invalid file** (76)
</dt> <dt>

**Invalid system path** (77)
</dt> <dt>

**File copy failed** (78)
</dt> <dt>

**Invalid security parameter** (79)
</dt> <dt>

**Unable to configure TCP/IP service** (80)
</dt> <dt>

**Unable to configure DHCP service** (81)
</dt> <dt>

**Unable to renew DHCP lease** (82)
</dt> <dt>

**Unable to release DHCP lease** (83)
</dt> <dt>

**IP not enabled on adapter** (84)
</dt> <dt>

**IPX not enabled on adapter** (85)
</dt> <dt>

**Frame/network number bounds error** (86)
</dt> <dt>

**Invalid frame type** (87)
</dt> <dt>

**Invalid network number** (88)
</dt> <dt>

**Duplicate network number** (89)
</dt> <dt>

**Parameter out of bounds** (90)
</dt> <dt>

**Access denied** (91)
</dt> <dt>

**Out of memory** (92)
</dt> <dt>

**Already exists** (93)
</dt> <dt>

**Path, file or object not found** (94)
</dt> <dt>

**Unable to notify service** (95)
</dt> <dt>

**Unable to notify DNS service** (96)
</dt> <dt>

**Interface not configurable** (97)
</dt> <dt>

**Not all DHCP leases could be released/renewed** (98)
</dt> <dt>

**DHCP not enabled on adapter** (100)
</dt> <dt>

**Other** (101 4294967295)
</dt> </dl>

## Remarks

This is an instance-dependent method call that applies on a per-adapter basis. After static DNS servers are specified to start using Dynamic Host Configuration Protocol (DHCP) instead of static DNS servers, you can call the method without supplying "in" parameters.

## Examples

The [Set DNS Server Search Order for Multiple Computers in an Organizational Unit](https://Gallery.TechNet.Microsoft.Com/Set-DNS-Server-Search-6a3e3ede) VBScript sample on TechNet Gallery retrieves or sets DNS Server search order for multiple computers that belongs to one organizational unit.

The [Modify the DNS Server Search Order for a Network Adapter](https://Gallery.TechNet.Microsoft.Com/7824348c-5a92-42cb-b4e9-ef2187702e02) VBScript sample configures a TCP/IP-bound network adapter to use two DNS servers.

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

 

