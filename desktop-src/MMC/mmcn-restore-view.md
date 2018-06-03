---
title: MMCN\_RESTORE\_VIEW message
description: Sent to the snap-in's IComponent Notify method when the result pane for a scope item must be restored by the snap-in after the user has navigated the view history using the back or forward buttons.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5b6c6d7c-af9f-4773-b9b1-1e11f4a1c1f8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_RESTORE_VIEW message MMC
topic_type:
- apiref
api_name:
- MMCN_RESTORE_VIEW
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_RESTORE\_VIEW message

The **MMCN\_RESTORE\_VIEW** notification is introduced in MMC 1.1.

The **MMCN\_RESTORE\_VIEW** notification message is sent to the snap-in's [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method when the result pane for a scope item must be restored by the snap-in after the user has navigated the view history using the back or forward buttons.

The **MMCN\_RESTORE\_VIEW** notification message is also sent to the snap-in when MMC [applies persisted column configuration data to a list view](https://www.bing.com/search?q=applies persisted column configuration data to a list view). For more information, see [Using Column Persistence](using-column-persistence.md).

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

A pointer to an [**MMC\_RESTORE\_VIEW**](/windows/desktop/api/Mmc/ns-mmc-_mmc_restore_view) structure that contains information about a result pane view that must be restored by the snap-in.

</dd> <dt>

*param* \[out\]
</dt> <dd>

A pointer to a **BOOL** that specifies whether the snap-in has handled the notification.

**TRUE** specifies that the snap-in has handled the notification appropriately.

**FALSE** specifies that the snap-in did not handle the notification and MMC will attempt to restore the **View** menu selection based on the information stored in the view history. If the snap-in does not set the **param** value, MMC defaults to **FALSE**.

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

MMC maintains a navigation history of the result pane. For each item in the history, MMC stores the view type and view options specified by [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) when the result pane was originally displayed during the course of the current console session. MMC also stores other information such as the scope item and the currently selected item in the **View** menu.

When the back and forward buttons are used to navigate the result pane history of a scope item, MMC sends the snap-in that owns the item an **MMCN\_RESTORE\_VIEW** notification that has a pointer to an **MMCN\_RESTORE\_VIEW** structure as its arg parameter and a pointer to a **BOOL** as its *param* parameter.

The snap-in should respond to the notification by setting itself to the same state as when that item originally appeared in the result pane. This means performing any initialization or assignment performed in the original call to [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) or the notification handler for the context menu item that represents the view selected in the **View** menu.

If the item to display is a custom OCX, webpage, or taskpad, the snap-in should handle that notification by setting the appropriate menu item in the **View** context menu and initializing the OCX or taskpad (if necessary). Then the snap-in should set its internal view type state (usually, a member variable stores the current view type in the class that implements [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent)) and set the param value to **TRUE**.

If the item to display is a virtual list in the result pane, the snap-in should initialize or set up the virtual list, set its internal view type state, and set the param value to **TRUE**.

If the item to display is a standard list in the result pane, the snap-in only must set its internal view type state and set the param value to **TRUE**.

MMC then reselects the appropriate item in the scope pane and displays the item with the appropriate view in the result pane.

Be aware that MMC does not persist any view information other than the options specified by the [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) method. If the snap-in must persist any other view information, it must implement a mechanism for storing the information and save it to stream or storage when the **Save** method of its [**IPersistStream**](https://msdn.microsoft.com/library/windows/desktop/ms690091) or [**IPersistStorage**](https://msdn.microsoft.com/library/windows/desktop/ms679731) interface implementation is called. Furthermore, this view-related information should be saved by the **IPersistStream** or **IPersistStorage** interface queried from the [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) associated with the view. Only information not related to any specific view should be saved by the **IPersistStream** or **IPersistStorage** interface queried from the snap-in's [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) implementation.

One notable exception to the fact that MMC persists only the options specified by the [**GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) options is that MMC also persists list view column configuration data. For more information, see [Using Column Persistence](using-column-persistence.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype)
</dt> <dt>

[**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify)
</dt> <dt>

[**MMC\_RESTORE\_VIEW**](/windows/desktop/api/Mmc/ns-mmc-_mmc_restore_view)
</dt> </dl>

 

 





