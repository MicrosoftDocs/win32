---
title: EM_SCROLL message (Winuser.h)
description: Scrolls the text vertically in a multiline edit control. This message is equivalent to sending a WM\_VSCROLL message to the edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 616b5ac2-d92f-4fc5-9a9e-2c7527fb0d97
keywords:
- EM_SCROLL message Windows Controls
topic_type:
- apiref
api_name:
- EM_SCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SCROLL message

Scrolls the text vertically in a multiline edit control. This message is equivalent to sending a [**WM\_VSCROLL**](wm-vscroll.md) message to the edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The action the scroll bar is to take. This parameter can be one of the following values.



| Value                                                                                                                                                   | Meaning                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="SB_LINEDOWN"></span><span id="sb_linedown"></span><dl> <dt>**SB\_LINEDOWN**</dt> </dl> | Scrolls down one line.<br/> |
| <span id="SB_LINEUP"></span><span id="sb_lineup"></span><dl> <dt>**SB\_LINEUP**</dt> </dl>       | Scrolls up one line.<br/>   |
| <span id="SB_PAGEDOWN"></span><span id="sb_pagedown"></span><dl> <dt>**SB\_PAGEDOWN**</dt> </dl> | Scrolls down one page.<br/> |
| <span id="SB_PAGEUP"></span><span id="sb_pageup"></span><dl> <dt>**SB\_PAGEUP**</dt> </dl>       | Scrolls up one page.<br/>   |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message is successful, the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) of the return value is **TRUE**, and the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is the number of lines that the command scrolls. The number returned may not be the same as the actual number of lines scrolled if the scrolling moves to the beginning or the end of the text. If the *wParam* parameter specifies an invalid value, the return value is **FALSE**.

## Remarks

To scroll to a specific line or character position, use the [**EM\_LINESCROLL**](em-linescroll.md) message. To scroll the caret into view, use the [**EM\_SCROLLCARET**](em-scrollcaret.md) message.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_LINESCROLL**](em-linescroll.md)
</dt> <dt>

[**EM\_SCROLLCARET**](em-scrollcaret.md)
</dt> <dt>

[**WM\_VSCROLL**](wm-vscroll.md)
</dt> </dl>

 

