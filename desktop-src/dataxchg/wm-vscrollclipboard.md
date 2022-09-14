---
title: WM_VSCROLLCLIPBOARD message (Winuser.h)
description: Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the CF\_OWNERDISPLAY format and an event occurs in the clipboard viewer's vertical scroll bar.
ms.assetid: 17bd32c4-1b07-42b7-b269-f517e3ec13f3
keywords:
- WM_VSCROLLCLIPBOARD message Data Exchange
topic_type:
- apiref
api_name:
- WM_VSCROLLCLIPBOARD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_VSCROLLCLIPBOARD message

Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) format and an event occurs in the clipboard viewer's vertical scroll bar. The owner should scroll the clipboard image and update the scroll bar values.


```C++
#define WM_VSCROLLCLIPBOARD             0x030A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the clipboard viewer window.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies a scroll bar event. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                         | Meaning                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="SB_BOTTOM"></span><span id="sb_bottom"></span><dl> <dt>**SB\_BOTTOM**</dt> <dt>7</dt> </dl>                      | Scroll to lower right.<br/>                                                                 |
| <span id="SB_ENDSCROLL"></span><span id="sb_endscroll"></span><dl> <dt>**SB\_ENDSCROLL**</dt> <dt>8</dt> </dl>             | End scroll.<br/>                                                                            |
| <span id="SB_LINEDOWN"></span><span id="sb_linedown"></span><dl> <dt>**SB\_LINEDOWN**</dt> <dt>1</dt> </dl>                | Scroll one line down.<br/>                                                                  |
| <span id="SB_LINEUP"></span><span id="sb_lineup"></span><dl> <dt>**SB\_LINEUP**</dt> <dt>0</dt> </dl>                      | Scroll one line up.<br/>                                                                    |
| <span id="SB_PAGEDOWN"></span><span id="sb_pagedown"></span><dl> <dt>**SB\_PAGEDOWN**</dt> <dt>3</dt> </dl>                | Scroll one page down.<br/>                                                                  |
| <span id="SB_PAGEUP"></span><span id="sb_pageup"></span><dl> <dt>**SB\_PAGEUP**</dt> <dt>2</dt> </dl>                      | Scroll one page up.<br/>                                                                    |
| <span id="SB_THUMBPOSITION"></span><span id="sb_thumbposition"></span><dl> <dt>**SB\_THUMBPOSITION**</dt> <dt>4</dt> </dl> | Scroll to absolute position. The current position is specified by the high-order word.<br/> |
| <span id="SB_TOP"></span><span id="sb_top"></span><dl> <dt>**SB\_TOP**</dt> <dt>6</dt> </dl>                               | Scroll to upper left.<br/>                                                                  |



 

The high-order word of *lParam* specifies the current position of the scroll box if the low-order word of *lParam* is **SB\_THUMBPOSITION**; otherwise, the high-order word of *lParam* is not used.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

The clipboard owner can use the [**ScrollWindow**](https://msdn.microsoft.com/library/Cc410994(v=MSDN.10).aspx) function to scroll the image in the clipboard viewer window and invalidate the appropriate region.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**ScrollWindow**](https://msdn.microsoft.com/library/Cc410994(v=MSDN.10).aspx)
</dt> </dl>

 

