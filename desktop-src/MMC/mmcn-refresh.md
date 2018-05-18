---
title: MMCN\_REFRESH message
description: The MMCN\_REFRESH notification message is sent to a snap-in's IComponent implementation when the refresh verb is selected. Refresh can be invoked through the context menu, through the toolbar, or by pressing F5.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c39d99f7-7e80-4bad-8494-41f7f28c83a3'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_REFRESH message MMC"]
topic_type:
- apiref
api_name:
- MMCN_REFRESH
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_REFRESH message

The **MMCN\_REFRESH** notification message is sent to a snap-in's [**IComponent**](icomponent.md) implementation when the refresh verb is selected. Refresh can be invoked through the context menu, through the toolbar, or by pressing F5.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

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

A snap-in should respond to a refresh notification by updating its scope and result items if they display information that is not always kept current.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





