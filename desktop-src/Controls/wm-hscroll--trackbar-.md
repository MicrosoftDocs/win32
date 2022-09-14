---
title: WM_HSCROLL (Trackbar) notification code (Winuser.h)
description: The WM\_HSCROLL message is sent to the owner of a horizontal trackbar control when the slider changes position. A window receives this message through its WindowProc function.
ms.assetid: EC4AF407-E13F-4562-A0A6-FA109C15101B
keywords:
- WM_HSCROLL (Trackbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- WM_HSCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_HSCROLL (Trackbar) notification code

The **WM\_HSCROLL** message is sent to the owner of a horizontal trackbar control when the slider changes position.

A window receives this message through its [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
WM_HSCROLL

    WPARAM wParam
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the current position of the slider if the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is TB\_THUMBPOSITION or TB\_THUMBTRACK. For all other notification codes, the high-order word is zero; send the [**TBM\_GETPOS**](tbm-getpos.md) message to determine the slider position.

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies a notification code that indicates the user's interaction with the trackbar. This word can be one of the following values.



| Value                                                                                                                                                                  | Meaning                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TB_BOTTOM"></span><span id="tb_bottom"></span><dl> <dt>**TB\_BOTTOM**</dt> </dl>                      | The user pressed the END key ([**VK\_END**](/windows/desktop/inputdev/virtual-key-codes)).<br/>                                                                                          |
| <span id="TB_ENDTRACK"></span><span id="tb_endtrack"></span><dl> <dt>**TB\_ENDTRACK**</dt> </dl>                | The trackbar received [**WM\_KEYUP**](/windows/desktop/inputdev/wm-keyup), meaning that the user released a key that sent a relevant virtual key code. <br/>                                           |
| <span id="TB_LINEDOWN"></span><span id="tb_linedown"></span><dl> <dt>**TB\_LINEDOWN**</dt> </dl>                | The user pressed the RIGHT ARROW ([**VK\_RIGHT**](/windows/desktop/inputdev/virtual-key-codes)) or DOWN ARROW ([**VK\_DOWN**](/windows/desktop/inputdev/virtual-key-codes)) key.<br/> |
| <span id="TB_LINEUP"></span><span id="tb_lineup"></span><dl> <dt>**TB\_LINEUP**</dt> </dl>                      | The user pressed the LEFT ARROW ([**VK\_LEFT**](/windows/desktop/inputdev/virtual-key-codes)) or UP ARROW ([**VK\_UP**](/windows/desktop/inputdev/virtual-key-codes)) key.<br/>             |
| <span id="TB_PAGEDOWN"></span><span id="tb_pagedown"></span><dl> <dt>**TB\_PAGEDOWN**</dt> </dl>                | The user clicked the channel below or to the right of the slider ([**VK\_NEXT**](/windows/desktop/inputdev/virtual-key-codes)).<br/>                                                   |
| <span id="TB_PAGEUP"></span><span id="tb_pageup"></span><dl> <dt>**TB\_PAGEUP**</dt> </dl>                      | The user clicked the channel above or to the left of the slider ([**VK\_PRIOR**](/windows/desktop/inputdev/virtual-key-codes)).<br/>                                                 |
| <span id="TB_THUMBPOSITION"></span><span id="tb_thumbposition"></span><dl> <dt>**TB\_THUMBPOSITION**</dt> </dl> | The trackbar received [**WM\_LBUTTONUP**](/windows/desktop/inputdev/wm-lbuttonup) following a TB\_THUMBTRACK notification code.<br/>                                                                   |
| <span id="TB_THUMBTRACK"></span><span id="tb_thumbtrack"></span><dl> <dt>**TB\_THUMBTRACK**</dt> </dl>          | The user dragged the slider.<br/>                                                                                                                                                     |
| <span id="TB_TOP"></span><span id="tb_top"></span><dl> <dt>**TB\_TOP**</dt> </dl>                               | The user pressed the HOME key ([**VK\_HOME**](/windows/desktop/inputdev/virtual-key-codes)). <br/>                                                                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The handle to the trackbar control.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

The TB\_THUMBTRACK code is typically used by applications that provide feedback as the user drags the scroll box.

Note that the **WM\_HSCROLL** message carries only 16 bits of position data. Thus, applications that rely solely on **WM\_HSCROLL** (and [**WM\_VSCROLL**](wm-vscroll--trackbar-.md)) for slider position data have a practical maximum position value of 65,535.

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

[**WM\_VSCROLL**](wm-vscroll--trackbar-.md)
</dt> </dl>

 

