---
title: Stand-alone Snap-ins
description: Stand-alone snap-ins must implement the IComponentData interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92e44c36-45f9-40a0-be8c-6984b02fcd55
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- stand-alone snap-ins MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Stand-alone Snap-ins

Stand-alone snap-ins must implement the [**IComponentData**](icomponentdata.md) interface. Additional interfaces must also be implemented, depending on the type of functionality you want the stand-alone snap-in to have. These requirements are described in detail in the sections of the Programmer's Guide that cover adding features such as different result pane views, toolbars, and property pages.

Snap-in developers are also encouraged to implement the [**ISnapinAbout**](isnapinabout.md) interface in their stand-alone snap-ins.

Stand-alone snap-ins that add to their namespace node types that are extended by extension snap-ins have additional requirements. For more information, see [Requirements for Primary Snap-ins](requirements-for-primary-snap-ins.md).

 

 




