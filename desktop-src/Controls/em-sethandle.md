---
title: EM_SETHANDLE message (Winuser.h)
description: Sets the handle of the memory that will be used by a multiline edit control.
ms.assetid: 0eae9365-62af-4040-8a51-273997a00b81
keywords:
- EM_SETHANDLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETHANDLE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETHANDLE message

Sets the handle of the memory that will be used by a multiline edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the memory buffer the edit control uses to store the currently displayed text instead of allocating its own memory. If necessary, the control reallocates this memory.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

Before an application sets a new memory handle, it should send an [**EM\_GETHANDLE**](em-gethandle.md) message to retrieve the handle of the current memory buffer and should free that memory.

An edit control automatically reallocates the given buffer whenever it needs additional space for text, or it removes enough text so that additional space is no longer needed.

Sending an **EM\_SETHANDLE** message clears the undo buffer ([**EM\_CANUNDO**](em-canundo.md) returns zero) and the internal modification flag ([**EM\_GETMODIFY**](em-getmodify.md) returns zero). The edit control window is redrawn.

**Rich Edit:** The **EM\_SETHANDLE** message is not supported. Rich edit controls do not store text as a simple array of characters.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_CANUNDO**](em-canundo.md)
</dt> <dt>

[**EM\_GETHANDLE**](em-gethandle.md)
</dt> <dt>

[**EM\_GETMODIFY**](em-getmodify.md)
</dt> </dl>

 

 





