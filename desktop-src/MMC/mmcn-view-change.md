---
title: MMCN\_VIEW\_CHANGE message
description: The MMCN\_VIEW\_CHANGE notification message is sent to the snap-ins IComponent implementation so it can update the view when a change occurs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3c76e700-0162-41ec-8f9d-45a03e6f5956
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_VIEW_CHANGE message MMC
topic_type:
- apiref
api_name:
- MMCN_VIEW_CHANGE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_VIEW\_CHANGE message

The **MMCN\_VIEW\_CHANGE** notification message is sent to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation so it can update the view when a change occurs.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object passed to [**IConsole::UpdateAllViews**](iconsole2-updateallviews.md).

</dd> <dt>

*arg* \[in\]
</dt> <dd>

The *data* parameter passed to [**IConsole::UpdateAllViews**](iconsole2-updateallviews.md).

</dd> <dt>

*param* \[in\]
</dt> <dd>

The *hint* parameter passed to [**IConsole::UpdateAllViews**](iconsole2-updateallviews.md).

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

This notification is generated when the snap-in ( [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) or [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master)) calls [**IConsole2::UpdateAllViews**](iconsole2-updateallviews.md).

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

[**IConsole::UpdateAllViews**](iconsole2-updateallviews.md)
</dt> </dl>

 

 





