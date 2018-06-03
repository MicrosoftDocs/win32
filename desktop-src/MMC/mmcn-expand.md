---
title: MMCN\_EXPAND message
description: The MMCN\_EXPAND notification message is sent to the snap-in's IComponentData implementation when a scope item must be expanded or collapsed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de89a195-082b-4d5f-bd8c-1c75215ab60f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_EXPAND message MMC
topic_type:
- apiref
api_name:
- MMCN_EXPAND
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_EXPAND message

The **MMCN\_EXPAND** notification message is sent to the snap-in's [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) implementation when a scope item must be expanded or collapsed.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the scope item that must be expanded or collapsed.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

**TRUE** if the folder is being expanded; **FALSE** if the folder is being collapsed.

</dd> <dt>

*param* \[in\]
</dt> <dd>

The HSCOPEITEM of the item that must be expanded or collapsed.

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

MMC sends the **MMCN\_EXPAND** notification the first time it must display a scope item's children in either the scope or result pane. The notification is not sent each time the item is visually expanded or collapsed.

On receipt of this notification the snap-in should enumerate the children (subcontainers only) of the specified scope item, if any, using [**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2) methods. Subsequently, if a new item is added to or deleted from this scope object through some external means, that item should also be added to or deleted from the console's namespace using **IConsoleNameSpace2** methods.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)
</dt> <dt>

[**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2)
</dt> </dl>

 

 





