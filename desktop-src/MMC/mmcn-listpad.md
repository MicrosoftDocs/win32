---
title: MMCN\_LISTPAD message
description: Sent to a snap-in's IComponent implementation when the list control for the list view taskpad for one of its scope items is being attached or detached.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce2a3146-f466-4768-a573-a4968baf659e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_LISTPAD message MMC
topic_type:
- apiref
api_name:
- MMCN_LISTPAD
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_LISTPAD message

The **MMCN\_LISTPAD** notification is introduced in MMC 1.1.

The **MMCN\_LISTPAD** notification message is sent to a snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation when the list control for the list view taskpad for one of its scope items is being attached or detached.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

A value that is **TRUE** if MMC is attaching the list control to the snap-in; **FALSE** if MMC is detaching the list control from the snap-in.

</dd> <dt>

*param* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification.

</dd> </dl>

## Remarks

When a list view taskpad is displayed, MMC clears the items in the result pane, attaches the list control used in the taskpad, and sends this notification with arg set to **TRUE**. The snap-in must handle this notification by populating the list with items using the [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata) or [**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata) interface.

When the view is switched from the list view taskpad to another view, MMC sends this notification with arg set to **FALSE**. When the snap-in handles this notification, it can free the resources (if any) used to populate the list.

When the snap-in receives the **MMCN\_LISTPAD** notification with arg set to **TRUE**, it should query for the [**IImageList**](/windows/desktop/api/Mmc/nn-mmc-iimagelist) interface and use it to add images to the list view on the taskpad. The snap-in can call the [**IConsole2::QueryResultImageList**](https://www.bing.com/search?q=**IConsole2::QueryResultImageList**) method to get an IImageList interface pointer.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify)
</dt> </dl>

 

 





