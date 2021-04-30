---
title: TB_GETSTRING message (Commctrl.h)
description: Retrieves a string from a toolbar's string pool.
ms.assetid: a5f80c16-bc6d-466d-8ec6-77451432148e
keywords:
- TB_GETSTRING message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETSTRING
- TB_GETSTRINGA
- TB_GETSTRINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETSTRING message

Retrieves a string from a toolbar's string pool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the length of the *lParam* buffer, in bytes. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the index of the string.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer used to return the string.

</dd> </dl>

## Return value

Returns the string length if successful, or -1 otherwise.

## Remarks

This message returns the specified string from the toolbar's string pool. It does not necessarily correspond to the text string currently being displayed by a button. To retrieve a button's current text string, send the toolbar a [**TB\_GETBUTTONTEXT**](tb-getbuttontext.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_GETSTRINGW** (Unicode) and **TB\_GETSTRINGA** (ANSI)<br/>                 |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TB\_ADDSTRING**](tb-addstring.md)
</dt> <dt>

[**TB\_ADDBUTTONS**](tb-addbuttons.md)
</dt> <dt>

[**TB\_INSERTBUTTON**](tb-insertbutton.md)
</dt> </dl>

 

