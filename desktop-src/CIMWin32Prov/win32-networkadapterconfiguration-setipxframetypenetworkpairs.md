---
description: Sets the Internetworking Packet Exchange (IPX) network number/frame pairs for this network adapter.
ms.assetid: 8190564f-7d9f-4b05-9949-2e732ce36dba
ms.tgt_platform: multiple
title: SetIPXFrameTypeNetworkPairs method of the Win32_NetworkAdapterConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterConfiguration.SetIPXFrameTypeNetworkPairs
api_type: 
- COM
api_location: 
- cimwin32.dll
---

# SetIPXFrameTypeNetworkPairs method of the Win32\_NetworkAdapterConfiguration class

Sets the Internetworking Packet Exchange (IPX) network number/frame pairs for this network adapter.

Windows 2000 and Windows NT 3.51 and higher use an IPX network number for routing purposes. It is assigned to each configured frame type/network adapter combination on your computer system. This number is sometimes referred to as the "external network number." It must be unique for each network segment. If the frame type is set to AUTO, the network number should to zero.

## Syntax


```mof
uint32 SetIPXFrameTypeNetworkPairs(
  [in] string IPXNetworkNumber[],
  [in] uint32 IPXFrameType[]
);
```



## Parameters

<dl> <dt>

*IPXNetworkNumber* \[in\]
</dt> <dd>

An array of characters that uniquely identify an adapter on the computer system. The NetWare Link (NWLink) IPX/SPX-compatible transport in Windows 2000 and Windows NT 3.51 or higher, uses two different types of network numbers. This number is sometimes referred to as the External Network Number. It must be unique for each network segment. The values in this string list must have a corresponding value in the IPXFrameType parameter identifying the packet frame type used for this network.

</dd> <dt>

*IPXFrameType* \[in\]
</dt> <dd>

An integer array of frame type identifiers. The values in this array correspond to the elements in the *IPXNetworkNumber* parameter.

<dt>

<span id="Ethernet_II"></span><span id="ethernet_ii"></span><span id="ETHERNET_II"></span>

**Ethernet II** (0)


</dt> <dd></dd> <dt>

<span id="Ethernet_802.3"></span><span id="ethernet_802.3"></span><span id="ETHERNET_802.3"></span>

**Ethernet 802.3** (1)


</dt> <dd></dd> <dt>

<span id="Ethernet_802.2"></span><span id="ethernet_802.2"></span><span id="ETHERNET_802.2"></span>

**Ethernet 802.2** (2)


</dt> <dd></dd> <dt>

<span id="Ethernet_SNAP"></span><span id="ethernet_snap"></span><span id="ETHERNET_SNAP"></span>

**Ethernet SNAP** (3)


</dt> <dd></dd> <dt>

<span id="AUTO"></span><span id="auto"></span>

**AUTO** (255)


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 




