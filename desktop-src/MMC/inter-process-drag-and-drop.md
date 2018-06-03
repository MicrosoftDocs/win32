---
title: Inter-process Drag-and-Drop Operations
description: MMC 2.0 supports the dragging of an item from one instance of mmc.exe to another instance of mmc.exe (both instances of mmc.exe must be running MMC 2.0).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71707082-8652-486b-b367-92a9d9fadc13
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inter-process Drag-and-Drop Operations

MMC 2.0 supports the dragging of an item from one instance of mmc.exe to another instance of mmc.exe (both instances of mmc.exe must be running MMC 2.0). To facilitate this feature, MMC 2.0 introduces the [**MMCN\_CANPASTE\_OUTOFPROC**](mmcn-canpaste-outofproc.md) notification. If an inter-process drag-and-drop operation is performed, and the drop target snap-in had earlier indicated (by its response to the **MMCN\_CANPASTE\_OUTOFPROC** notification) that it accepts data objects from other MMC processes, then the drag source data object will be sent to the drop target as part of a [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification. If the drop target snap-in had earlier indicated that it does not accept data objects from other MMC processes, then the **MMCN\_QUERY\_PASTE** notification is not sent.

Be aware that a snap-in, OCX, or external application can directly copy data onto the clipboard, in which case MMC does not know the details of the data object. In this event, MMC 2.0 behaves as did MMC 1.2 - the data object will be sent to the snap-in (as part of the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification) regardless of the snap-in's response to the [**MMCN\_CANPASTE\_OUTOFPROC**](mmcn-canpaste-outofproc.md) notification. Also, a snap-in running in MMC 2.0 always receives a **MMCN\_CANPASTE\_OUTOFPROC** notification.

When your snap-in receives data from a different process, do not cast (using C or C++ techniques) the provided [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) interface to its internal implementation; the data object is actually a marshaled interface. Instead, retrieve data from the data object by either a) implementing a marshaling interface on the data object (then have the drop target query and use that interface) or b) calling the [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) or [**IDataObject::GetDataHere**](https://www.bing.com/search?q=**IDataObject::GetDataHere**) method using clipboard formats, which do not contain any process-specific information (hence, pointers, handles, and so on cannot be part of the clipboard data).

 

 




