---
title: Multicast Address Dynamic Client Allocation Protocol
description: The Multicast Address Dynamic Client Allocation Protocol (MADCAP) enables applications to obtain, renew, and release multicast addresses.
ms.assetid: be313f7a-6332-4601-98b2-01561582213b
keywords:
- MADCAP MADCAP
- MADCAP MADCAP , (See Multicast Address Dynamic Client Allocation Protocol MADCAP )
- Multicast Address Dynamic Client Allocation Protocol MADCAP , start page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multicast Address Dynamic Client Allocation Protocol

## Purpose

The Multicast Address Dynamic Client Allocation Protocol (MADCAP) enables applications to obtain, renew, and release multicast addresses. MADCAP enables applications determine to which multicast scope zones a client belongs. This determination enables clients to dynamically obtain multicast address, while also allowing network administrators to dynamically manage the distribution of multicast addresses across the network.

## Where applicable

Developers can use MADCAP to:

-   Enumerate the multicast zones to which a client belongs.
-   Dynamically obtain a multicast address for a client, enabling that client to participate in network multicast sessions.
-   Release multicast addresses when appropriate.

Microsoft Windows implementation of MADCAP adheres to recommendations published by the Internet Engineering Task Force (IETF). For more information, see ([www.ietf.org](Http://go.microsoft.com/fwlink/p/?linkid=84023)). MADCAP has been ratified as RFC 2730, but is subject to growth and evolution. Microsoft Corporation is involved with the standards process.

## Developer audience

MADCAP is designed for use by C/C++ programmers. Familiarity with Windows networking and multicast technology is required.

## Run-time requirements

MADCAP requires Windows 2000 or later.

## In this section



| Topic                                        | Description                                    |
|----------------------------------------------|------------------------------------------------|
| [Overview](about-madcap.md)<br/>      | General information about MADCAP.<br/>   |
| [Reference](madcap-reference.md)<br/> | Reference documentation for MADCAP.<br/> |



 

## Related topics

<dl> <dt>

[Quality of Service](_gqos_qos_start_page)
</dt> </dl>

 

 





