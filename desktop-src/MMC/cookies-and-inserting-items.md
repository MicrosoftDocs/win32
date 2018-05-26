---
title: Cookies and Inserting Items
description: Shows how snap-ins can insert items into the scope or result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bf8ca366-2e8b-411f-b1e9-d5635b7212d3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- cookies and inserting items MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cookies and Inserting Items

Snap-ins insert items into the scope or result pane using the [**IResultData::InsertItem**](/windows/win32/Mmc/nf-mmc-iresultdata-insertitem?branch=master) or [**IConsoleNameSpace2::InsertItem**](iconsolenamespace2-insertitem.md) method. The cookie value of the inserted item is stored in the **lParam** member of the [**SCOPEDATAITEM**](/windows/win32/Mmc/ns-mmc-_scopedataitem?branch=master) structure (for scope items) or [**RESULTDATAITEM**](/windows/win32/Mmc/ns-mmc-_resultdataitem?branch=master) structure (for result items).

After an item is successfully inserted, MMC calls [**IComponentData::GetDisplayInfo**](/windows/win32/Mmc/nf-mmc-icomponentdata-getdisplayinfo?branch=master) or [**IComponent:GetDisplayInfo**](/windows/win32/Mmc/nf-mmc-icomponent-getdisplayinfo?branch=master), depending on which object inserted the item. The snap-in can then cast the **lParam** (cookie) back into the reference for the selected item and retrieve the display name, image index, or other information that can be displayed in the result pane's columns.

As previously mentioned, MMC often requests data objects from snap-ins by calling the [**IComponentData::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponentdata-querydataobject?branch=master) or [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) method. In the call to **QueryDataObject**, MMC also passes the cookie value of the item for which MMC requires data. If the requested data object is created to notify a snap-in of a user action on a particular scope or result item, MMC forwards the data object back to the snap-in, along with the appropriate notification message. The only way that the snap-in can properly identify the affected item is by means of the cookie value that is passed into the call to the **QueryDataObject** method.

It is therefore very important that any implementation of [**IDataObject**](_ole_idataobject) stores the cookie value of the item for which MMC is requesting a data object.

 

 




