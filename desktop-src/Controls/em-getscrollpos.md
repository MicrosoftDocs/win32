---
title: EM_GETSCROLLPOS message (Richedit.h)
description: Obtains the current scroll position of the edit control.
ms.assetid: 26e122da-f1b4-4694-978c-ff678dad5d9f
keywords:
- EM_GETSCROLLPOS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETSCROLLPOS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETSCROLLPOS message

Obtains the current scroll position of the edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](/previous-versions//dd162805(v=vs.85)) structure. After calling **EM\_GETSCROLLPOS**, this parameters contains a point in the virtual text space of the document, expressed in pixels. This point will be the point that is currently located in the upper-left corner of the edit control window.

</dd> </dl>

## Return value

This message always returns 1.

## Remarks

The values returned in the [**POINT**](/previous-versions//dd162805(v=vs.85)) structure are 16-bit values (even in the 32-bit wide fields).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETSCROLLPOS**](em-setscrollpos.md)
</dt> </dl>

 

