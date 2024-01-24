---
description: Sets the Internetworking Packet Exchange (IPX) virtual network number on the target computer system.
ms.assetid: 52064250-b94f-4dc0-bf1a-8601cd135a90
ms.tgt_platform: multiple
title: SetIPXVirtualNetworkNumber method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.SetIPXVirtualNetworkNumber
api_type: 
- COM
api_location: 
- cimwin32.dll
---

# SetIPXVirtualNetworkNumber method of the Win32\_NetworkAdapterConfiguration class

Sets the Internetworking Packet Exchange (IPX) virtual network number on the target computer system. Windows 2000 and Windows NT 3.51 or greater uses an internal network number for internal routing. The internal network number is also known as a virtual network number. It uniquely identifies the computer system on the network. The method returns an integer value that can be interpretted as follows:

## Syntax


```mof
uint32 SetIPXVirtualNetworkNumber(
  [in] string IPXVirtualNetNumber
);
```



## Parameters

<dl> <dt>

*IPXVirtualNetNumber* \[in\]
</dt> <dd>

The virtual network number for this system.

</dd> </dl>

## Return value

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

**Other** (101–4294967295)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CimWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Cimwin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md)
</dt> </dl>

 

 




