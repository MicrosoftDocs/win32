---
title: MMCN\_SELECT message
description: The MMCN\_SELECT notification message is sent to the snap-ins IComponent Notify or IExtendControlbar ControlbarNotify method when an item is selected in either the scope pane or result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca3a39ee-da6d-46bc-ac75-4afd89cc8565
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_SELECT message MMC
topic_type:
- apiref
api_name:
- MMCN_SELECT
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_SELECT message

The **MMCN\_SELECT** notification message is sent to the snap-in's [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) or [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) method when an item is selected in either the scope pane or result pane.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master), this parameter is a pointer to the data object of the currently selected/deselected scope pane or result item. For [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), this parameter is not used.

</dd> <dt>

*arg* 
</dt> <dd>

BOOL *bScope* = (BOOL) LOWORD(*arg*);

BOOL *bSelect* = (BOOL) HIWORD(*arg*);

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master), *bScope* is **TRUE** if the selected item is a scope item, or **FALSE** if the selected item is a result item. For *bScope* = **TRUE**, MMC does not provide information about whether the scope item is selected in the scope pane or in the result pane.

For [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), *bScope* is **TRUE** if an item in the scope pane is selected, or **FALSE** if an item in the result pane is selected.

For either [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) or [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), *bSelect* is **TRUE** if the item is selected, or **FALSE** if the item is deselected.

</dd> <dt>

*param* 
</dt> <dd>

LPDATAOBJECT *pDataobject* = (LPDATAOBJECT)*param*;

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master), this parameter is not used. For [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), *pDataobject* is the data object of the item being selected or deselected.

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

When an [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method receives the **MMCN\_SELECT** notification it should update the standard verbs.

When an [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) method receives the **MMCN\_SELECT** notification it should update the custom toolbars. On select, it should detach unused toolbars and attach new ones as required. On deselect, to minimize flashing, it should not detach toolbars; it is best to disable them, but doing nothing on deselect is also acceptable.

Snap-ins should have the ability to create and attach toolbars when they receive a selection notification, regardless of whether the item is in the scope pane or result pane.

For snap-ins that have a custom result pane (OCX or web), MMC sends the **MMCN\_SELECT** or [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md) notification with a special data object (**DOBJ\_CUSTOMOCX** or **DOBJ\_CUSTOMWEB**) when the result pane is selected or deselected. The notification is sent to the snap-in's [**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) and [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method. The only way for snap-ins to identify the corresponding scope item is to use the cookie (of the scope item) cached during [**MMCN\_SHOW**](mmcn-show.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master)
</dt> <dt>

[**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master)
</dt> </dl>

 

 





