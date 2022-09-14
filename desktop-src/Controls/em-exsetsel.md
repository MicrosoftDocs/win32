---
title: EM_EXSETSEL message (Richedit.h)
description: Selects a range of characters or Component Object Model (COM) objects in a Microsoft Rich Edit control.
ms.assetid: 85a0d1d4-1826-4ac5-b823-de81a051441d
keywords:
- EM_EXSETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXSETSEL
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_EXSETSEL message

Selects a range of characters or Component Object Model (COM) objects in a Microsoft Rich Edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-charrange) structure that specifies the selection range.

</dd> </dl>

## Return value

The return value is the selection that is actually set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





