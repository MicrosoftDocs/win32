---
title: Using Microsoft Locator
description: Microsoft Locator is the default name service. The RPC run-time library uses it to find server programs on server host systems.
ms.assetid: 8481de50-4e72-432d-aef7-524f18f5c9c4
keywords:
- Remote Procedure Call RPC , tasks, using Microsoft Locator
ms.topic: article
ms.date: 05/31/2018
---

# Using Microsoft Locator

Microsoft Locator is the default name service. The RPC run-time library uses it to find server programs on server host systems.

**Note**  Microsoft RPC locator is not supported in Windows Vista and later operating systems.

Prior to Windows 2000, Microsoft Locator did not provide persistent name service entries. All entries in the name service were stored in a memory cache on the server program's host computer. The locator used a broadcast mechanism to discover the location of servers as requested by clients. Whenever the host system shut down, all name service entries were lost.

Beginning with the release of Windows 2000, Microsoft Locator now supports persistent name service entries. To accomplish this, the system employs a distributed directory service to store name service entries. This mechanism has several advantages:

-   **Persistence.** Server programs are no longer required to export their binding information to the name service each time they start up. The name service now stores the information until the server program on the network administrator explicitly removes it.
-   **Efficiency.** By eliminating the majority of broadcasting for name service entries, the locator reduces network traffic. It also finds name service entries more rapidly.
-   **Cross-Domain Interoperability.** Clients are now able to make name service requests across multiple domains.

Current versions of Microsoft Locator are backward compatible. For instance, a server host system running the locator that ships with Windows 2000 can operate correctly on a network that contains server host systems running the locator that ships with Windows NT 4.0.

With the release of Windows 2000, Microsoft Locator now supports name service entries for groups of users. It also provides the ability for you to create user profiles.

In addition, the current version of Microsoft Locator supports the use of Access Control Lists in name service entries. This ability enhances the security of the network.

Plug and Play support is now included in Microsoft Locator. Therefore, it can transparently handle Plug and Play events such as domain changes. For more information, see [**RpcNsBindingExportPnP**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingexportpnpa) and [**RpcNsBindingUnexportPnP**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingunexportpnpa).

 

 




