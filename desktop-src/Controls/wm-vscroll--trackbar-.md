---
title: WM_VSCROLL (Trackbar) notification code
description: The WM\_VSCROLL message is sent to the owner of a vertical trackbar control when the slider changes position. A window receives this message through its WindowProc function.
ms.assetid: E491E210-9605-4ABB-A667-471830DA7C2B
keywords:
- WM_VSCROLL (Trackbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- WM_HSCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_VSCROLL (Trackbar) notification code

The **WM\_VSCROLL** message is sent to the owner of a vertical trackbar control when the slider changes position.

A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
WM_HSCROLL

    WPARAM wParam
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the current position of the slider if the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) is TB\_THUMBPOSITION or TB\_THUMBTRACK. For all other notification codes, the high-order word is zero; send the [**TBM\_GETPOS**](tbm-getpos.md) message to determine the slider position.

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies a notification code that indicates the user's interaction with the trackbar. This word can be one of the following values.



| Value                                                                                                                                                                  | Meaning                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TB_BOTTOM"></span><span id="tb_bottom"></span><dl> <dt>**TB\_BOTTOM**</dt> </dl>                      | The user pressed the END key ([**VK\_END**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-end)).<br/>                                                                                          |
| <span id="TB_ENDTRACK"></span><span id="tb_endtrack"></span><dl> <dt>**TB\_ENDTRACK**</dt> </dl>                | The trackbar received [**WM\_KEYUP**](https://msdn.microsoft.com/library/windows/desktop/ms646281), meaning that the user released a key that sent a relevant virtual key code. <br/>                                           |
| <span id="TB_LINEDOWN"></span><span id="tb_linedown"></span><dl> <dt>**TB\_LINEDOWN**</dt> </dl>                | The user pressed the RIGHT ARROW ([**VK\_RIGHT**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-right)) or DOWN ARROW ([**VK\_DOWN**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-down)) key.<br/> |
| <span id="TB_LINEUP"></span><span id="tb_lineup"></span><dl> <dt>**TB\_LINEUP**</dt> </dl>                      | The user pressed the LEFT ARROW ([**VK\_LEFT**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-left)) or UP ARROW ([**VK\_UP**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-up)) key.<br/>             |
| <span id="TB_PAGEDOWN"></span><span id="tb_pagedown"></span><dl> <dt>**TB\_PAGEDOWN**</dt> </dl>                | The user clicked the channel below or to the right of the slider ([**VK\_NEXT**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-next)).<br/>                                                   |
| <span id="TB_PAGEUP"></span><span id="tb_pageup"></span><dl> <dt>**TB\_PAGEUP**</dt> </dl>                      | The user clicked the channel above or to the left of the slider ([**VK\_PRIOR**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-prior)).<br/>                                                 |
| <span id="TB_THUMBPOSITION"></span><span id="tb_thumbposition"></span><dl> <dt>**TB\_THUMBPOSITION**</dt> </dl> | The trackbar received [**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608) following a TB\_THUMBTRACK notification code.<br/>                                                                   |
| <span id="TB_THUMBTRACK"></span><span id="tb_thumbtrack"></span><dl> <dt>**TB\_THUMBTRACK**</dt> </dl>          | The user dragged the slider.<br/>                                                                                                                                                     |
| <span id="TB_TOP"></span><span id="tb_top"></span><dl> <dt>**TB\_TOP**</dt> </dl>                               | The user pressed the HOME key ([**VK\_HOME**](https://msdn.microsoft.com/library/windows/desktop/dd375731#vk-home)). <br/>                                                                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The handle to the trackbar control.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

The TB\_THUMBTRACK code is typically used by applications that provide feedback as the user drags the scroll box.

Note that the **WM\_VSCROLL** message carries only 16 bits of position data. Thus, applications that rely solely on **WM\_VSCROLL** (and [**WM\_HSCROLL**](wm-hscroll--trackbar-.md)) for slider position data have a practical maximum position value of 65,535.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WM\_HSCROLL**](wm-hscroll--trackbar-.md)
</dt> </dl>

 

 





