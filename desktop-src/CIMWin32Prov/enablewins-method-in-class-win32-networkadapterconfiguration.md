---
description: The EnableWINS &\#32; WMI class static method enables Windows Internet Naming Service (WINS) settings specific to TCP/IP, but independent of the network adapter.
ms.assetid: ce0fb170-978f-4d70-bced-e530e43da719
ms.tgt_platform: multiple
title: EnableWINS method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.EnableWINS
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# EnableWINS method of the Win32\_NetworkAdapterConfiguration class

The **EnableWINS** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) static method enables Windows Internet Naming Service (WINS) settings specific to TCP/IP, but independent of the network adapter.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 EnableWINS(
  [in]           boolean DNSEnabledForWINSResolution,
  [in]           boolean WINSEnableLMHostsLookup,
  [in, optional] string  WINSHostLookupFile,
  [in, optional] string  WINSScopeID
);
```



## Parameters

<dl> <dt>

*DNSEnabledForWINSResolution* \[in\]
</dt> <dd>

If **true**, the Domain Name System (DNS) is enabled for name resolution over WINS resolution.

</dd> <dt>

*WINSEnableLMHostsLookup* \[in\]
</dt> <dd>

If **true**, local lookup files are used. Lookup files will contain mappings of IP addresses to host names.

</dd> <dt>

*WINSHostLookupFile* \[in, optional\]
</dt> <dd>

Lookup files that contain mappings of IP addresses to host names. If available, the files will be found in %SystemRoot%\\system32\\drivers\\ .

</dd> <dt>

*WINSScopeID* \[in, optional\]
</dt> <dd>

Scope identifier value that will be appended to the end of the computer's NetBIOS name. Systems that use the same scope identifier can communicate with this computer.

</dd> </dl>

## Return value

Returns a value of 0 (zero) for a successful completion when no reboot is required; 1 (one) for a successful completion when a reboot is required; a different number if there is an error. For more information on error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

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

## Examples

The [Enable WINS for All Network Adapters](https://Gallery.TechNet.Microsoft.Com/64cae6dd-4155-4825-ab25-5727503edf5a) VBScript code sample, on TechNet Gallery, uses **EnableWINS** to Enables WINS on all the network adapters installed in a computer.

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

 

