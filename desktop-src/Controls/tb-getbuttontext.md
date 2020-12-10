---
title: TB_GETBUTTONTEXT message (Commctrl.h)
description: Retrieves the display text of a button on a toolbar.
ms.assetid: 16dd7181-a404-4056-b084-05f49f5a4b14
keywords:
- TB_GETBUTTONTEXT message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETBUTTONTEXT
- TB_GETBUTTONTEXTA
- TB_GETBUTTONTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETBUTTONTEXT message

Retrieves the display text of a button on a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button whose text is to be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer that receives the button text.

</dd> </dl>

## Return value

Returns the length, in characters, of the string pointed to by *lParam*. The length does not include the terminating null character. If unsuccessful, the return value is -1.

## Remarks

**Security Warning:** Using this message incorrectly might compromise the security of your program. This message does not provide a way for you to know the size of the buffer. If you use this message, first call the message passing **NULL** in the *lParam*, this returns the number of characters, excluding **NULL** that are required. Then call the message a second time to retrieve the string. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

The returned string corresponds to the text that is currently displayed by the button.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_GETBUTTONTEXTW** (Unicode) and **TB\_GETBUTTONTEXTA** (ANSI)<br/>         |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TB\_GETBUTTONINFO**](tb-getbuttoninfo.md)
</dt> <dt>

[**TB\_GETSTRING**](tb-getstring.md)
</dt> <dt>

[**TB\_SETBUTTONINFO**](tb-setbuttoninfo.md)
</dt> </dl>

 

 





