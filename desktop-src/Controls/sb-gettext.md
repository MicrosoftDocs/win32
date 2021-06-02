---
title: SB_GETTEXT message (Commctrl.h)
description: Retrieves the text from the specified part of a status window.
ms.assetid: 95bef9ff-04e5-431e-bc79-06d8498fcab0
keywords:
- SB_GETTEXT message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETTEXT
- SB_GETTEXTA
- SB_GETTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETTEXT message

Retrieves the text from the specified part of a status window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part from which to retrieve text.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the buffer that receives the text as a null-terminated string. Use the [**SB\_GETTEXTLENGTH**](sb-gettextlength.md) message to determine the required size of the buffer.

</dd> </dl>

## Return value

Returns a 32-bit value that consists of two 16-bit values. The low word specifies the length, in characters, of the text. The high word specifies the type of operation used to draw the text. The type can be one of the following values.



| Return code                                                                                    | Description                                                                               |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>               | The text is drawn with a border to appear lower than the plane of the window.<br/>  |
| <dl> <dt>**SBT\_NOBORDERS**</dt> </dl>  | The text is drawn without borders.<br/>                                             |
| <dl> <dt>**SBT\_POPOUT**</dt> </dl>     | The text is drawn with a border to appear higher than the plane of the window.<br/> |
| <dl> <dt>**SBT\_RTLREADING**</dt> </dl> | The text displays in the opposite direction of the text in the parent window.<br/>  |



 

## Remarks

**Security Warning:** Using this message incorrectly can compromise the security of your program. This message does not provide a way for you to know the size of the buffer. If you use this message, first call [**SB\_GETTEXTLENGTH**](sb-gettextlength.md) to get the number of characters that are required and then call the message to retrieve the string. If you wait before calling **SB\_GETTEXT** the text could change, thereby invalidating the return value of **SB\_GETTEXTLENGTH**. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

This message returns a maximum of 65,535 characters. If the text string is longer than that, it is truncated.

If the text has the SBT\_OWNERDRAW drawing type, this message returns the 32-bit value associated with the text instead of the length and operation type.

Normal windows display text left-to-right (LTR). Windows can be *mirrored* to display languages such as Hebrew or Arabic that read right-to-left (RTL). If SBT\_RTLREADING is set, the *lParam* string reads in the opposite direction from the text in the parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **SB\_GETTEXTW** (Unicode) and **SB\_GETTEXTA** (ANSI)<br/>                     |



## See also

<dl> <dt>

[**SB\_SETTEXT**](sb-settext.md)
</dt> </dl>

 

 





