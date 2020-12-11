---
title: WM_HSCROLLCLIPBOARD message (Winuser.h)
description: Sent to the clipboard owner by a clipboard viewer window.
ms.assetid: 73558de6-a822-40f7-9eb2-47ea5afd4e6e
keywords:
- WM_HSCROLLCLIPBOARD message Data Exchange
topic_type:
- apiref
api_name:
- WM_HSCROLLCLIPBOARD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_HSCROLLCLIPBOARD message

Sent to the clipboard owner by a clipboard viewer window. This occurs when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) format and an event occurs in the clipboard viewer's horizontal scroll bar. The owner should scroll the clipboard image and update the scroll bar values.


```C++
#define WM_HSCROLLCLIPBOARD             0x030E
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the clipboard viewer window.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies a scroll bar event. This parameter can be one of the following values. The high-order word of *lParam* specifies the current position of the scroll box if the low-order word of *lParam* is **SB\_THUMBPOSITION**; otherwise, the high-order word is not used.



| Value                                                                                                                                                                                                                         | Meaning                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="SB_ENDSCROLL"></span><span id="sb_endscroll"></span><dl> <dt>**SB\_ENDSCROLL**</dt> <dt>8</dt> </dl>             | End scroll.<br/>                                                                            |
| <span id="SB_LEFT"></span><span id="sb_left"></span><dl> <dt>**SB\_LEFT**</dt> <dt>6</dt> </dl>                            | Scroll to upper left.<br/>                                                                  |
| <span id="SB_RIGHT"></span><span id="sb_right"></span><dl> <dt>**SB\_RIGHT**</dt> <dt>7</dt> </dl>                         | Scroll to lower right.<br/>                                                                 |
| <span id="SB_LINELEFT"></span><span id="sb_lineleft"></span><dl> <dt>**SB\_LINELEFT**</dt> <dt>0</dt> </dl>                | Scrolls left by one unit.<br/>                                                              |
| <span id="SB_LINERIGHT"></span><span id="sb_lineright"></span><dl> <dt>**SB\_LINERIGHT**</dt> <dt>1</dt> </dl>             | Scrolls right by one unit.<br/>                                                             |
| <span id="SB_PAGELEFT"></span><span id="sb_pageleft"></span><dl> <dt>**SB\_PAGELEFT**</dt> <dt>2</dt> </dl>                | Scrolls left by the width of the window.<br/>                                               |
| <span id="SB_PAGERIGHT"></span><span id="sb_pageright"></span><dl> <dt>**SB\_PAGERIGHT**</dt> <dt>3</dt> </dl>             | Scrolls right by the width of the window.<br/>                                              |
| <span id="SB_THUMBPOSITION"></span><span id="sb_thumbposition"></span><dl> <dt>**SB\_THUMBPOSITION**</dt> <dt>4</dt> </dl> | Scroll to absolute position. The current position is specified by the high-order word.<br/> |



 

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

 

