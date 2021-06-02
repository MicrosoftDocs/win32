---
description: This topic describes high-level network interface concepts on Windows, including the ways they can be identified in code and their properties.
ms.assetid: CB01B5ED-C9DB-410B-8C98-E30D9A680847
title: Network Interfaces
ms.topic: article
ms.date: 06/29/2018
---

# Network interfaces

This topic describes high-level network interface concepts on Windows, including the ways they can be identified in code and their properties. 

> [!IMPORTANT]
> This topic is intended for a developer audience, both for Windows desktop networking apps and kernel mode networking drivers. Nevertheless, some of the information presented here can also be useful for system administrators managing network interfaces through PowerShell cmdlets.

## Overview

A *network interface* is the point where two pieces of network equipment or protocol layers connect. Typically, this is represented by a physical Network Interface Card (NIC) for connection between a computer and a private or public network. However, it can also take the form of a software-only component such as the loopback interface (`127.0.0.1` for IPv4 or `::1` for IPv6).

Network interfaces are defined by the Internet Engineering Task Force (IETF) in [RFC 2863](https://tools.ietf.org/html/rfc2863) and are not meant to be defined by Windows. For detailed questions about the meaning of network interface identifiers such as **ifIndex**, see the IETF's definitions of them. The rest of this topic discusses Windows-specific implementation details.

## Network interface identifiers and properties

On Windows, a network interface can be identified in different ways. Some of these identifiers are used to distinguish network interfaces from each other, but not all identifiers are equally suited to that task because of their differing properties. Generally, network interfaces are identified by a network address to external components. For example, this may be a node ID and a port number, or simply a unique node ID. 

In code, a network interface can be identified in many ways. The following table details the ways a network interface can be identified along with associated properties. We recommend using the interface GUID (**ifGuid**) for programming unless a specific API requires a different network interface identifier.

> [!NOTE]
> In the following table, **bolded** cells represent a property that is desirable for networking programmers.

| Identifier | Size | Is unique on the system | Is unique in the world | Is predictable | Will be recycled if the NIC is removed | Persists across reboots | End users can modify at any time | Drivers can modify at any time | General familiarity with end users | Is always present |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ifIndex** | **4 bytes** | **Yes** | No | No | Yes | No<sup>1</sup> | **No** | **No** | **Some**<sup>2</sup> | **Yes** |
| **NetLuid** | **8 bytes** | **Yes** | No | No | Yes | **Yes** | **No** | **No** | No | **Yes** |
| **ifGuid** | **16 bytes** | **Yes** | **Usually**<sup>3</sup> | No | **No** | **Yes** | **No** | **No** | No | **Yes** |
| **ifAlias** | 514 bytes | **Yes for NICs**<sup>4</sup> | No | Sometimes<sup>5</sup> | Yes | **Yes** | Yes | **No** | **Yes** | **Usually**<sup>4</sup> |
| **ifDescr** | 514 bytes | Usually<sup>6</sup> | No | No | Yes | **Yes** | **No** | Yes | **Yes** | **Usually** |
| **ifPhysAddress (MAC ADDRESS)**| 0 to 32 bytes | Usually, for NICs | **Usually, for NICs** | **Yes** | **Tied to hardware** | **Yes** | **No** | **No** | **Yes** | **Usually** <sup>7</sup> |
| **PnP instance ID** | Up to 400 bytes | **Yes** | No | No | Yes | **Yes** | **No** | **No** | No | **Usually, for NICs**<sup>8</sup> |
| **PnP location (PCI slot number)** | Up to 400 bytes | **Yes** | No | **Yes** | Yes | **Yes** | **No** | **No** | Sometimes | Sometimes<sup>8,9</sup> |

Notes for the preceding table:

1. **IfIndexes** are not guaranteed to be stable across reboots, even though they often receive the same value as the previous boot. Therefore, it is not recommended that drivers use **ifIndex** except where required by an API.
2. Some `netsh` commands take `ifIndex`, or `index`, as an input. Therefore, some administrative users are familiar with the **ifIndex** property if they use the `netsh` command frequently.
3. If a machine is cloned or imaged, then some of the GUIDs might be the same. Also, certain special network interfaces such as the built-in Teredo interface might have the same GUID on all machines.
4. NetCfg enforces that an **ifAlias** is a non-empty string and is unique among all NICs. However, the NDIS interface provider does not. Thererfore, it is possible to find special network interfaces with duplicate or empty names. This is most commonly seen with LBFO teams.
5. Only if the firmware supports Consistent Device Naming. Typcically, servers have this feature.
6. NetCfg assigns unique **ifDescrs** to all network interfaces. However, drivers can call an API to change the **ifDescr** to anything, including something that is not unique. Some 3rd party software packages do this.
7. Not all media types have a "MAC address." For example, some tunnels do not have this concept and simply advertise a zero-length byte array as their network address.
8. Only present on network interfaces that are backed by a PnP device. For example, loopback interfaces, light weight filter interfaces, interfaces provided by an NDIS interface provider, and certain special built-in NICs don't have PnP devices backing them.
9. Only some PnP buses support a PnP location ID. The built-in PCI and USB buses do, while root-enumerated devices do not.

## Visibility to developers

In the preceding table, all properties except for the Plug and Play (PnP) properties are visible to user mode desktop apps and kernel mode drivers via a shared header (Netioapi.h). The PnP properties are visible via the Devpkey.h header and are used by both user mode desktop apps and kernel mode drivers. For example, see the [DEVPKEY](/windows-hardware/drivers/install/devpkey-device-instanceid) documentation.

The [IP Helper](/windows/desktop/IpHlp/ip-helper-start-page) API is also available for both user mode desktop apps and kernel mode drivers.

The UWP API surface only exposes the [ifGuid](/uwp/api/windows.networking.connectivity.networkadapter.networkadapterid) property directly. However, it is possible for a UWP app developers to import the [**GetIfTable2**](/windows/desktop/api/netioapi/nf-netioapi-getiftable2) function using P/Invoke if they are required to access other network interface properties.

## Related topics

For management information base (MIB) definitions for network interfaces, see [RFC 2863](https://tools.ietf.org/html/rfc2863).

For NDIS network interfaces in network drivers, see [NDIS Network Interfaces](/windows-hardware/drivers/network/ndis-network-interfaces2).

For Netioapi.h API reference, see [netioapi.h header](/windows/desktop/api/netioapi/).
