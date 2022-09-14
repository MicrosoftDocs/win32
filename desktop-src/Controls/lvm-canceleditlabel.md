---
title: LVM_CANCELEDITLABEL message (Commctrl.h)
description: Cancels an item text editing operation.
ms.assetid: 73e9c922-3223-4c49-a33c-df7c09443ccc
keywords:
- LVM_CANCELEDITLABEL message Windows Controls
topic_type:
- apiref
api_name:
- LVM_CANCELEDITLABEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_CANCELEDITLABEL message

Cancels an item text editing operation.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

This message causes a an [LVN\_ENDLABELEDIT](lvn-endlabeledit.md) notification to be sent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





