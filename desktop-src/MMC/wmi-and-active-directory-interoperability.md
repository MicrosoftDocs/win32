---
title: WMI and Active Directory Interoperability
description: Illustrates how WMI and active directory technologies can be combined in MMC snap-in design.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e0bfd7b1-6352-4db0-b6ba-688c49db95ad
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WMI and Active Directory Interoperability

These two technologies, WMI and Active Directory, can act in concert to make a snap-in developer's work much easier. Both offer a data store, a query engine, and an index engine. However, the uses for the data stores and engines are very different.

Active Directory provides a replicated, highly available store, optimized for fast access to largely static information. It holds the information necessary to locate users, systems, and devices in the enterprise, along with meta-information about the network and environment that is not available elsewhere.

WMI provides access to detailed system and device information for managed objects in the enterprise. It supports both static and dynamic properties, methods, and events for its managed objects.

Snap-ins can use Active Directory to locate objects in the enterprise and WMI to gather information from those objects, making enterprise management more centralized and accessible, and therefore easier.

 

 




