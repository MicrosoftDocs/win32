---
title: Packet Monitor (Pktmon)
description: Packet Monitor (Pktmon) is an in-box, cross-component network diagnostics tool for Windows.
ms.topic: reference
ms.date: 07/03/2024
---

# Packet Monitor (Pktmon)

Packet Monitor (Pktmon) is an in-box, cross-component network diagnostics tool for Windows. It can be used for packet capture, packet drop detection, packet filtering, and counting. The tool is especially helpful in virtualization scenarios such as container networking and SDN, because it provides visibility within the networking stack. It's available in-box via the `pktmon.exe` command, and via Windows Admin Center extensions.

For more info, see [Packet Monitor (Pktmon)](/windows-server/networking/technologies/pktmon/pktmon).

## Remarks

> [!IMPORTANT]
> The Pktmon functions don't have an associated header file or import library file in the Microsoft Windows Software Development Kit (SDK). Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`Pktmonapi.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of a Pktmon function to get the function address.

The Pktmon functions correspond to the features of multisession and packet-streaming.
* **Multisession**. Ordinarily, Packet Monitor handles only one session at a time system-wide. If a long-running application (such as Defender) were already using the services of pktmon, then no other instances of pktmon could run without stopping the previous instance. But multisession helps override that limitation by offering the flexibility to create a separate session for monitoring packets.
* **Packet-streaming**. Provides the capability to observe packets in real time. Ordinarily, a live session for observing packets would be possible through ETW; but packet streaming eliminates the dependency on limited availability of ETW sessions. Packet streaming has benefits including latency monitoring, monitoring live packet drops, and more.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Supported runtime environments** | Windows/C++ |
| **Recommended programming languages** | C++ |
| **Minimum supported client** |  |
| **Minimum supported server** | Windows Server WS2022-6b update |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | Pktmonapi.dll |

## In this section

| Topic | Description |
|-|-|
| [Pktmon reference](pktmon-reference.md) | This section covers Pktmon functions. |
