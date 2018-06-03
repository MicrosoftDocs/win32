---
title: MMCN\_DESELECT\_ALL message
description: The MMCN\_DESELECT\_ALL notification message is sent to the virtual list view when all items of an owner-data result pane are deselected.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54a491a2-35bd-4650-a912-527ee7af78c5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_DESELECT_ALL message MMC
topic_type:
- apiref
api_name:
- MMCN_DESELECT_ALL
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_DESELECT\_ALL message

The **MMCN\_DESELECT\_ALL** notification message is sent to the virtual list view when all items of an owner-data result pane are deselected.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

NULL.

</dd> <dt>

*arg* 
</dt> <dd>

Zero.

</dd> <dt>

*param* 
</dt> <dd>

Zero.

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

When all the items in a virtual list are deselected, MMC sends an **MMCN\_DESELECT\_ALL** notification rather than an [**MMCN\_SELECT**](mmcn-select.md) that identifies all the deselected items. **MMCN\_DESELECT\_ALL** is not sent for standard (non-virtual) lists.

For snap-ins that have a custom result pane (OCX or web), MMC sends an [**MMCN\_SELECT**](mmcn-select.md) or **MMCN\_DESELECT\_ALL** notification with a special data object (DOBJ\_CUSTOMOCX or DOBJ\_CUSTOMWEB) when the result pane is selected or deselected. The notification is sent to the snap-in's [**IExtendControlbar::ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) and [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method. The only way for snap-ins to identify the corresponding scope item is to use the cookie (of the scope item) cached during [**MMCN\_SHOW**](mmcn-show.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





