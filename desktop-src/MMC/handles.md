---
title: Handles
description: Creates a handle for each inserted item that is subsequently valid as long as the item is in the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ad9f11a5-785e-4630-86bb-6c5ff229bdc3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- handles MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Handles

When a scope item is inserted into the scope pane, MMC creates a handle, or *HSCOPEITEM*, that uniquely identifies the inserted item. For all items other than the static node, MMC returns the item's HSCOPEITEM after the snap-in successfully inserts the item in the scope pane using [**IConsoleNameSpace2::InsertItem**](iconsolenamespace2-insertitem.md).

In the case of the static node, MMC itself inserts it into the snap-in's namespace. MMC then passes the static node's HSCOPEITEM to the snap-in as the *param* parameter in the [**MMCN\_EXPAND**](mmcn-expand.md) notification.

MMC also returns to the snap-in a handle for each inserted result item. This handle, called an *HRESULTITEM*, is returned after the snap-in successfully inserts the result item using [**IResultData::InsertItem**](/windows/win32/Mmc/nf-mmc-iresultdata-insertitem?branch=master).

A scope item's handle is valid for as long as the item is present in the snap-in's scope pane. Furthermore, a scope item's handle is the same in all views (MDI child windows). A result item's handle is only valid for as long as the item is displayed in a result pane. When the result pane is torn down, MMC destroys all handles to any of the result items that were displayed in the result pane.

A snap-in needs an item's handle in order to manipulate it using the methods of the [**IConsoleNameSpace2**](/windows/win32/Mmc/nn-mmc-iconsolenamespace2?branch=master), [**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master), and [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) interfaces. Therefore, the snap-in should store the item's handle after successfully inserting it into the scope pane or result pane. In the case of result items, snap-ins can also acquire a result item's handle by calling the [**IResultData::FindItemByLParam**](/windows/win32/Mmc/nf-mmc-iresultdata-finditembylparam?branch=master) method, which enables a snap-in to find result item based on the snap-in-defined **lParam** value (cookie value).

## Cookies Compared with Handles

Cookies and handles both refer to inserted scope or result items. However, it's important to keep in mind the following differences between the two:

-   An inserted item's cookie value is determined solely by the snap-in that inserts the item. The snap-in specifies the item's cookie value in the **lParam** member of the [**SCOPEDATAITEM**](/windows/win32/Mmc/ns-mmc-_scopedataitem?branch=master)or [**RESULTDATAITEM**](/windows/win32/Mmc/ns-mmc-_resultdataitem?branch=master) structure it must fill when inserting the item. MMC caches this value and uses it to uniquely identify the item in calls made to the snap-in's [**IComponentData::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponentdata-querydataobject?branch=master) or [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) implementation.
-   MMC creates an inserted item's handle and returns it to the snap-in after the item is successfully inserted. Snap-ins must specify an item's handle when attempting to manipulate the item using the methods of the [**IConsoleNameSpace2**](/windows/win32/Mmc/nn-mmc-iconsolenamespace2?branch=master), [**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master), or [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) interface.

 

 




