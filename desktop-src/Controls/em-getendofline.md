---
title: EM_GETENDOFLINE message (Commctrl.h)
description: Retrieves the end-of-line character used when a linebreak is inserted. Send this message explicitly or by using the Edit\_GetEndOfLine macro.
ms.assetid: 557f796e-c9d1-4ea1-b8a6-44ae0bed5ffc
keywords:
- EM_GETENDOFLINE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETENDOFLINE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM\_GETENDOFLINE message

Retrieves the end-of-line character for an edit control. Send this message explicitly or by using the [**Edit\_GetEndOfLine**](/windows/desktop/api/Commctrl/nf-commctrl-edit_getendofline) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the end-of-line character used by the edit control. This can be one of the following values.

| Value                                                                                                                                                   | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="EC_ENDOFLINE_CRLF"></span><span id="ec_endofline_crlf"></span><dl> <dt>**EC\_ENDOFLINE\_CRLF**</dt> </dl> | The end-of-line character used for new linebreaks is carriage return followed by linefeed (CRLF).<br/> |
| <span id="EC_ENDOFLINE_CR"></span><span id="ec_endofline_cr"></span><dl> <dt>**EC\_ENDOFLINE\_CR**</dt> </dl>       | The end-of-line character used for new linebreaks is carriage return (CR).<br/>                        |
| <span id="EC_ENDOFLINE_LF"></span><span id="ec_endofline_lf"></span><dl> <dt>**EC\_ENDOFLINE\_LF**</dt> </dl>       | The end-of-line character used for new linebreaks is linefeed (LF).<br/>                               |

## Remarks

When the end-of-line character used is set to **EC\_ENDOFLINE\_DETECTFROMCONTENT** using [**Edit\_SetEndOfLine**](/windows/desktop/api/Commctrl/nf-commctrl-edit_setendofline), this message will return the detected end-of-line character.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETENDOFLINE*](em-setendofline.md)
</dt> </dl>
 

 





