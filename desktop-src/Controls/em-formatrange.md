---
title: EM_FORMATRANGE message (Richedit.h)
description: Formats a range of text in a rich edit control for a specific device.
ms.assetid: 6d1e562b-d741-4d4a-a395-554083cb0dbb
keywords:
- EM_FORMATRANGE message Windows Controls
topic_type:
- apiref
api_name:
- EM_FORMATRANGE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FORMATRANGE message

Formats a range of text in a rich edit control for a specific device.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether to render the text. If this parameter is not zero, the text is rendered. Otherwise, the text is just measured.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**FORMATRANGE**](/windows/desktop/api/Richedit/ns-richedit-formatrange) structure containing information about the output device, or **NULL** to free information cached by the control.

</dd> </dl>

## Return value

This message returns the index of the last character that fits in the region, plus 1.

## Remarks

This message is typically used to format the content of rich edit control for an output device such as a printer.

After using this message to format a range of text, it is important that you free cached information by sending **EM\_FORMATRANGE** again, but with *lParam* set to **NULL**; otherwise, a memory leak will occur. Also, after using this message for one device, you must free cached information before using it again for a different device.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_DISPLAYBAND**](em-displayband.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Printing Rich Edit Controls](printing-rich-edit-controls.md)
</dt> </dl>

 

 





