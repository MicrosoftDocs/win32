---
title: MMCN\_DBLCLICK message
description: The MMCN\_DBLCLICK notification message is sent to the snap-in's IComponent implementation when a user double-clicks a mouse button on a list view item or on a scope item in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0c85cd06-4799-4bb6-aa1d-3386edbf1a37'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_DBLCLICK message MMC"]
topic_type:
- apiref
api_name:
- MMCN_DBLCLICK
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_DBLCLICK message

The **MMCN\_DBLCLICK** notification message is sent to the snap-in's [**IComponent**](icomponent.md) implementation when a user double-clicks a mouse button on a list view item or on a scope item in the result pane.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected item.

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

Do the default action, if the default action is either the properties or open standard verb.

</dd> </dl>

## Remarks

Pressing enter while the list item or scope item has focus in the list view also generates an **MMCN\_DBLCLICK** notification message.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent**](icomponent.md)
</dt> </dl>

 

 





