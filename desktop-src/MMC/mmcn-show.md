---
title: MMCN\_SHOW message
description: The MMCN\_SHOW notification message is sent to the snap-ins IComponent implementation when a scope item is selected or deselected.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cc2a9da4-1351-4930-8fb4-577cdcc14e10
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_SHOW message MMC
topic_type:
- apiref
api_name:
- MMCN_SHOW
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_SHOW message

The **MMCN\_SHOW** notification message is sent to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation when a scope item is selected or deselected.

## Parameters

<dl> <dt>

*arg* 
</dt> <dd>

**TRUE** if selecting. Indicates that the snap-in should set up the result pane and add the enumerated items.

**FALSE** if deselecting. Indicates that the snap-in is going out of focus and that it should clean up all result item cookies, because the current result pane will be replaced by a new one.

</dd> <dt>

*param* 
</dt> <dd>

The **HSCOPEITEM** of the selected or deselected item.

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

In their **MMCN\_SHOW** notification handler, snap-ins that have a custom result pane (OCX or web) should cache the cookie (of the scope item) that was passed in the *lpDataObject* argument in the call to [**IComponent::Notify**](icomponent-notify.md). The snap-in needs the cookie to identify the correct scope item when MMC sends it an [**MMCN\_SELECT**](mmcn-select.md) or [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md) notification message with a special data object (**DOBJ\_CUSTOMOCX** or **DOBJ\_CUSTOMWEB**). MMC sends the **MMCN\_SELECT** or **MMCN\_DESELECT\_ALL** notification with a special data object when the result pane is selected or deselected. The notification is sent to the snap-in's [**IExtendControlbar::ControlbarNotify**](iextendcontrolbar-controlbarnotify.md) and **IComponent::Notify** method. The only way for snap-ins to identify the corresponding scope item is to use its cookie cached during **MMCN\_SHOW**.

Also, snap-ins that have a custom result pane (OCX or web) can call [**IConsole2::QueryResultView**](iconsole2-queryresultview.md) to query for the OCX control object's [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface pointer during **MMCN\_SHOW**.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





