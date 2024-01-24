---
title: EM_SETENDOFLINE message (CommCtrl.h)
description: Sets the end-of-line character used when a linebreak is inserted.
ms.assetid: a10b3f57-0e67-4a0f-89f3-9c8ebd1514f8
keywords:
- EM_SETENDOFLINE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETENDOFLINE
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM\_SETENDOFLINE message

Sets the end-of-line character used when a linebreak is inserted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the end-of-line character used when a linebreak is inserted. This can be one of the following values.


| Value                                                                                                                                                   | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="EC_ENDOFLINE_DETECTFROMCONTENT"></span><span id="ec_endofline_detectfromcontent"></span><dl> <dt>**EC\_ENDOFLINE\_DETECTFROMCONTENT**</dt> </dl> | Sets the end-of-line character used for new linebreaks to the character used by the current document.<br/>  |
| <span id="EC_ENDOFLINE_CRLF"></span><span id="ec_endofline_crlf"></span><dl> <dt>**EC\_ENDOFLINE\_CRLF**</dt> </dl>                                        | Sets the end-of-line character used for new linebreaks to carriage return followed by linefeed (CRLF).<br/> |
| <span id="EC_ENDOFLINE_CR"></span><span id="ec_endofline_cr"></span><dl> <dt>**EC\_ENDOFLINE\_CR**</dt> </dl>                                              | Sets the end-of-line character used for new linebreaks to carriage return (CR).<br/>                        |
| <span id="EC_ENDOFLINE_LF"></span><span id="ec_endofline_lf"></span><dl> <dt>**EC\_ENDOFLINE\_LF**</dt> </dl>                                              | Sets the end-of-line character used for new linebreaks to linefeed (LF).<br/>                               |

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the operation succeeds, the return value is nonzero.

If the operation fails, the return value is zero.

## Remarks

When the end-of-line character set is **EC\_ENDOFLINE\_DETECTFROMCONTENT**, the edit control will only detect end-of-line characters supported according to its extended window style, see [Edit Control Extended Styles](edit-control-window-extended-styles.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETENDOFLINE*](em-getendofline.md)
</dt> </dl>

 

 





