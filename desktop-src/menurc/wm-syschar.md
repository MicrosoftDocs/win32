---
title: WM\_SYSCHAR message
description: Posted to the window with the keyboard focus when a WM\_SYSKEYDOWN message is translated by the TranslateMessage function.
ms.assetid: 55987105-3c53-42e5-8fab-a3c9f2ca7273
keywords:
- WM_SYSCHAR message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_SYSCHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_SYSCHAR message

Posted to the window with the keyboard focus when a [**WM\_SYSKEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646286) message is translated by the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function. It specifies the character code of a system character key   that is, a character key that is pressed while the ALT key is down.


```C++
#define WM_SYSCHAR                      0x0106
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character code of the window menu key.

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown in the following table.



| Bits                                                                             | Meaning                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 15</dt> </dl>  | The repeat count for the current message. The value is the number of times the keystroke was auto-repeated as a result of the user holding down the key. If the keystroke is held long enough, multiple messages are sent. However, the repeat count is not cumulative.<br/> |
| <dl> <dt>16 23</dt> </dl> | The scan code. The value depends on the original equipment manufacturer (OEM).<br/>                                                                                                                                                                                          |
| <dl> <dt>24</dt> </dl>    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.<br/>                                                                |
| <dl> <dt>25 28</dt> </dl> | Reserved; do not use.<br/>                                                                                                                                                                                                                                                   |
| <dl> <dt>29</dt> </dl>    | The context code. The value is 1 if the ALT key is held down while the key is pressed; otherwise, the value is 0.<br/>                                                                                                                                                       |
| <dl> <dt>30</dt> </dl>    | The previous key state. The value is 1 if the key is down before the message is sent, or it is 0 if the key is up.<br/>                                                                                                                                                      |
| <dl> <dt>31</dt> </dl>    | The transition state. The value is 1 if the key is being released, or it is 0 if the key is being pressed.<br/>                                                                                                                                                              |



 

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

When the context code is zero, the message can be passed to the [**TranslateAccelerator**](/windows/win32/Winuser/nf-winuser-translateacceleratora?branch=master) function, which will handle it as though it were a standard key message instead of a system character-key message. This allows accelerator keys to be used with the active window even if the active window does not have the keyboard focus.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN and arrow keys in the clusters to the left of the numeric keypad; the PRINT SCRN key; the BREAK key; the NUMLOCK key; and the divide (/) and ENTER keys in the numeric keypad. Other keyboards may support the extended-key bit in the parameter.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TranslateAccelerator**](/windows/win32/Winuser/nf-winuser-translateacceleratora?branch=master)
</dt> <dt>

[**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955)
</dt> <dt>

[**WM\_SYSKEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646286)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

 





