---
title: SNMP Service
description: The Microsoft Windows implementation of the Simple Network Management Protocol (SNMP) is used to configure remote devices, monitor network performance, audit network usage, and detect network faults or inappropriate access.Important The Microsoft Windows SNMP API only supports protocol versions up to SNMPv2C. It does not support any later versions of the protocol.
ms.assetid: fbaddb10-804b-4230-8986-717edc19a2f5
keywords:
- SNMP SNMP
- SNMP SNMP , start page
ms.topic: article
ms.date: 05/31/2018
---

# SNMP Service

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

## Purpose

The Microsoft Windows implementation of the Simple Network Management Protocol (SNMP) is used to configure remote devices, monitor network performance, audit network usage, and detect network faults or inappropriate access.

> [!IMPORTANT]
> The Microsoft Windows SNMP API only supports protocol versions up to SNMPv2C. It does not support any later versions of the protocol.

 

## Where applicable

SNMP uses a distributed architecture consisting of management applications and agent applications. The SNMP service implements an SNMP agent. To use the information the SNMP service provides, you must have at least one host that is running an SNMP management application. You can use third-party SNMP management software, or you can develop your own SNMP management software application. The following APIs are available for this purpose:

-   SNMP Management API, a set of functions that can be used to quickly develop basic SNMP management systems
-   WinSNMP API, version 2.0, a set of functions for encoding, decoding, sending, and receiving SNMP messages

Additionally, the SNMP Extension Agent API defines the interface between the SNMP service and third-party SNMP extension agent DLLs. The SNMP Utility API functions can be used to simplify the processing of SNMP messages.

## Developer audience

The APIs listed in the preceding section are designed for use by C/C++ programmers. Familiarity with SNMP and SNMPv2C, as well as a working knowledge of networking and network management concepts, are required.

## Run-time requirements

For more information about the operating system required to use a particular function, see the Requirements section of the reference page for that function.

## In this section



| Topic                                                                                                | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [New in SNMP](new-in-snmp.md)<br/>                                                            | Information on updates to SNMP.<br/>                                                                                                      |
| [Simple Network Management Protocol (SNMP)](simple-network-management-protocol-snmp-.md)<br/> | Information and API reference for SNMP, including the SNMP Management API, SNMP Extension Agent API, and SNMP Utility API functions.<br/> |
| [WinSNMP API](snmp-reference.md)<br/>                                                         | Information and API reference for the Microsoft Windows SNMP Application Programming Interface (WinSNMP API). <br/>                       |



 

## Related topics

<dl> <dt>

[Dynamic Host Configuration Protocol (DHCP)](/previous-versions/windows/desktop/dhcp/dhcp-start-page)
</dt> <dt>

[Network Management](/windows/desktop/NetMgmt/network-management)
</dt> <dt>

[Routing and Remote Access Service](/windows/desktop/RRAS/portal)
</dt> </dl>

 

