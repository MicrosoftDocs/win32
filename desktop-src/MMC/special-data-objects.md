---
title: Special Data Objects
description: Demonstrates the use of a custom data object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22db48da-3b94-40c6-9b0a-aff1ade33d7e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- special data objects MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Special Data Objects

In certain circumstances, the data object that MMC passes to the snap-in during a notification is a special type of data object instead of a pointer to an actual [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) object.

To determine whether the data object is a special data object, the snap-in can use the [**IS\_SPECIAL\_DATAOBJECT**](/windows/desktop/api/Mmc/nf-mmc-is_special_dataobject) macro. A return value of **TRUE** indicates that the data object is a special data object. Based on the return value, the snap-in can then handle the notification message appropriately.

The special data object can take three values: DOBJ\_NULL, DOBJ\_CUSTOMOCX, and DOBJ\_CUSTOMWEB.

The DOBJ\_NULL value indicates that MMC does not require a data object for the notification message being sent. Examples of notification messages for which the LPDATAOBJECT is set to DOBJ\_NULL include [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) and [**MMCN\_FILTERBTN\_CLICK**](mmcn-filterbtn-click.md).

The DOBJ\_CUSTOMOCX value indicates that the result pane contains an OCX control. The DOBJ\_CUSTOMWEB value indicates that the result pane contains a webpage.

MMC can pass DOBJ\_CUSTOMOCX or DOBJ\_CUSTOMWEB as the data object in the following methods with the following notifications:

-   [**IExtendControlbar::ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify)
    -   [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md)
-   [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify)
    -   [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) with *param* set to MMC\_VERB\_PROPERTIES
    -   [**MMCN\_DELETE**](mmcn-delete.md)
    -   [**MMCN\_PASTE**](mmcn-paste.md)
    -   [**MMCN\_PRINT**](mmcn-print.md)
    -   [**MMCN\_REFRESH**](mmcn-refresh.md)

 

 




