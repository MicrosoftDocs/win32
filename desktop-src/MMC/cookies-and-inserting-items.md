---
title: Cookies and Inserting Items
description: Shows how snap-ins can insert items into the scope or result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bf8ca366-2e8b-411f-b1e9-d5635b7212d3'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["cookies and inserting items MMC"]
---

# Cookies and Inserting Items

Snap-ins insert items into the scope or result pane using the [**IResultData::InsertItem**](iresultdata-insertitem.md) or [**IConsoleNameSpace2::InsertItem**](iconsolenamespace2-insertitem.md) method. The cookie value of the inserted item is stored in the **lParam** member of the [**SCOPEDATAITEM**](scopedataitem.md) structure (for scope items) or [**RESULTDATAITEM**](resultdataitem.md) structure (for result items).

After an item is successfully inserted, MMC calls [**IComponentData::GetDisplayInfo**](icomponentdata-getdisplayinfo.md) or [**IComponent:GetDisplayInfo**](icomponent-getdisplayinfo.md), depending on which object inserted the item. The snap-in can then cast the **lParam** (cookie) back into the reference for the selected item and retrieve the display name, image index, or other information that can be displayed in the result pane's columns.

As previously mentioned, MMC often requests data objects from snap-ins by calling the [**IComponentData::QueryDataObject**](icomponentdata-querydataobject.md) or [**IComponent::QueryDataObject**](icomponent-querydataobject.md) method. In the call to **QueryDataObject**, MMC also passes the cookie value of the item for which MMC requires data. If the requested data object is created to notify a snap-in of a user action on a particular scope or result item, MMC forwards the data object back to the snap-in, along with the appropriate notification message. The only way that the snap-in can properly identify the affected item is by means of the cookie value that is passed into the call to the **QueryDataObject** method.

It is therefore very important that any implementation of [**IDataObject**](_ole_idataobject) stores the cookie value of the item for which MMC is requesting a data object.

 

 




