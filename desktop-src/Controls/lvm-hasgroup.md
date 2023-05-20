---
title: LVM_HASGROUP message (Commctrl.h)
description: Determines whether the list-view control has a specified group.
ms.assetid: 0b8a9208-5221-4f66-8b26-7de55afe485f
keywords:
- LVM_HASGROUP message Windows Controls
topic_type:
- apiref
api_name:
- LVM_HASGROUP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_HASGROUP message

Determines whether the list-view control has a specified group.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>ID of the group.</dd> <dt>

*lParam* 
 </dt> <dd>Must be <b>NULL</b>.</dd> </dl>

## Return value

Returns **TRUE** if the list-view control has the specified group, or **FALSE** otherwise.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





