---
title: SB_SETTEXT message (Commctrl.h)
description: Sets the text in the specified part of a status window.
ms.assetid: 6039a61c-6ec6-42cd-94d5-5f1cf2998586
keywords:
- SB_SETTEXT message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETTEXT
- SB_SETTEXTA
- SB_SETTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETTEXT message

Sets the text in the specified part of a status window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOBYTE**](/previous-versions/windows/desktop/legacy/ms632658(v=vs.85)) of the low-order word specifies the zero-based index of the part to set. If the **LOBYTE** is set to SB\_SIMPLEID, the status window is assumed to be a simple mode status bar; that is, a status bar with only one part.

The [**HIBYTE**](/previous-versions/windows/desktop/legacy/ms632656(v=vs.85)) of the low-order word specifies the type of the drawing operation. This parameter can be one of the following values.

The high-order word of *wParam* is ignored.




| Value | Meaning | 
|-------|---------|
| <span id="0"></span><dl><dt><strong>0</strong></dt></dl> | The text is drawn with a border to appear lower than the plane of the window.<br /> | 
| <span id="SBT_NOBORDERS"></span><span id="sbt_noborders"></span><dl><dt><strong>SBT_NOBORDERS</strong></dt></dl> | The text is drawn without borders.<br /> | 
| <span id="SBT_OWNERDRAW"></span><span id="sbt_ownerdraw"></span><dl><dt><strong>SBT_OWNERDRAW</strong></dt></dl> | The text is drawn by the parent window. <br /><blockquote>[!Note]<br />A simple mode status bar does not support owner drawing.</blockquote><br /> | 
| <span id="SBT_POPOUT"></span><span id="sbt_popout"></span><dl><dt><strong>SBT_POPOUT</strong></dt></dl> | The text is drawn with a border to appear higher than the plane of the window.<br /> | 
| <span id="SBT_RTLREADING"></span><span id="sbt_rtlreading"></span><dl><dt><strong>SBT_RTLREADING</strong></dt></dl> | The text will be displayed in the opposite direction to the text in the parent window.<br /> | 
| <span id="SBT_NOTABPARSING"></span><span id="sbt_notabparsing"></span><dl><dt><strong>SBT_NOTABPARSING</strong></dt></dl> | Tab characters are ignored.<br /> | 




 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a null-terminated string that specifies the text to set. If *wParam* is SBT\_OWNERDRAW, this parameter represents 32 bits of data. The parent window must interpret the data and draw the text when it receives the [**WM\_DRAWITEM**](wm-drawitem.md) message.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The message invalidates the portion of the window that has changed, causing it to display the new text when the window next receives the [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message.

Normal windows display text left-to-right (LTR). Windows can be *mirrored* to display languages such as Hebrew or Arabic that read right-to-left (RTL). If SBT\_RTLREADING is set, the *lParam* string will read in the opposite direction from the text in the parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **SB\_SETTEXTW** (Unicode) and **SB\_SETTEXTA** (ANSI)<br/>                     |



## See also

<dl> <dt>

[**SB\_GETTEXT**](sb-gettext.md)
</dt> </dl>

 

