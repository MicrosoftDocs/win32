---
title: EM_INSERTIMAGE message (Richedit.h)
description: Replaces the selection with a blob that displays an image.
ms.assetid: 147B298B-C4A9-455B-9736-A0B09D72902B
keywords:
- EM_INSERTIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- EM_INSERTIMAGE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_INSERTIMAGE message

Replaces the selection with a blob that displays an image.


```C++
#define EM_INSERTIMAGE       (WM_USER + 314)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RICHEDIT\_IMAGE\_PARAMETERS**](/windows/win32/api/richedit/ns-richedit-richedit_image_parameters) structure that contains the image blob.

</dd> </dl>

## Return value

Returns S\_OK if successful, or one of the following error codes.



| Return code                                                                                    | Description                                                   |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_FAIL** </dt> </dl>        | Cannot insert the image. <br/>                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *lParam* parameter is NULL or points to an invalid image. |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl> | Insufficient memory is available.<br/>                  |



 

## Remarks

If the selection is an insertion point, the image blob is inserted at the insertion point.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_INSERTTABLE**](em-inserttable.md)
</dt> </dl>

 

 





