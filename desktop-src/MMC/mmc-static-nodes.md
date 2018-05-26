---
title: MMC Static Nodes
description: A static node is a node in the MMC namespace that is present as long as the snap-in that provides it is loaded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 58c982b6-0a52-4b4c-bd06-6757772c720d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC static nodes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC Static Nodes

A static node is a node in the MMC namespace that is present as long as the snap-in that provides it is loaded. Snap-ins must implement the [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) interface to have static nodes in the tree. The first time a static node is accessed in an MMC console, MMC calls [**CoCreateInstance**](_com_cocreateinstance) to create an instance of the snap-in COM server that owns the static node in that console. Each static node in each console is associated with a different instance of a snap-in.

Only stand-alone snap-ins can have static nodes. Extension snap-ins can extend the static nodes of other snap-ins, but they never provide their own static nodes in any console in which they are loaded.

Stand-alone snap-ins use static nodes to store their setup configuration and relative placement in the console. The static node is inserted when the snap-in is loaded in a console. The console itself inserts the static node in the scope pane. This differs from enumerated nodes, which snap-ins insert themselves.

A static node has a [cookie](cookies.md) value of **NULL**. The snap-in must be prepared to receive notifications on a **NULL** cookie just like any other node.

When a (stand-alone) snap-in is loaded in a console file, MMC requests a data object for the snap-in's static node and then calls its [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) method with the [**CCF\_DISPLAY\_NAME**](ccf-display-name.md) clipboard format to retrieve the static node's display name. MMC requests the display name when the static node is first displayed in the **Standalone** tab of the **Add/Remove Snap-in** dialog box and when the static node is first added to the scope pane. After the initial creation of the static node, a snap-in must use the [**IConsoleNameSpace2::SetItem**](iconsolenamespace2-setitem.md) method to change the static node's name.

Cookies, data objects, and clipboard formats are discussed in detail later on in this overview.

 

 




