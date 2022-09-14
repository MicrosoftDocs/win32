---
title: SB_GETTEXTLENGTH message (Commctrl.h)
description: Retrieves the length, in characters, of the text from the specified part of a status window.
ms.assetid: 2cd43106-dd43-499e-b595-760e9ededab5
keywords:
- SB_GETTEXTLENGTH message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETTEXTLENGTH
- SB_GETTEXTLENGTHA
- SB_GETTEXTLENGTHW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETTEXTLENGTH message

Retrieves the length, in characters, of the text from the specified part of a status window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part from which to retrieve text.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a 32-bit value that consists of two 16-bit values. The low word specifies the length, in characters, of the text. The high word specifies the type of operation used to draw the text. The type can be one of the following values:



| Return code                                                                                    | Description                                                                                       |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>               | The text is drawn with a border to appear lower than the plane of the window.<br/>          |
| <dl> <dt>**SBT\_NOBORDERS**</dt> </dl>  | The text is drawn without borders.<br/>                                                     |
| <dl> <dt>**SBT\_OWNERDRAW**</dt> </dl>  | The text is drawn by the parent window.<br/>                                                |
| <dl> <dt>**SBT\_POPOUT**</dt> </dl>     | The text is drawn with a border to appear higher than the plane of the window.<br/>         |
| <dl> <dt>**SBT\_RTLREADING**</dt> </dl> | The text will be displayed in the opposite direction to the text in the parent window.<br/> |



 

## Remarks

Normal windows display text left-to-right (LTR). Windows can be *mirrored* to display languages such as Hebrew or Arabic that read right-to-left (RTL). If SBT\_RTLREADING is set, the specified status window text will read in the opposite direction from the text in the parent window.

This message returns a maximum string length of 65,535 characters. If the actual text string is longer than that, the [**SB\_GETTEXT**](sb-gettext.md) message truncates it.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **SB\_GETTEXTLENGTHW** (Unicode) and **SB\_GETTEXTLENGTHA** (ANSI)<br/>         |



 

 





