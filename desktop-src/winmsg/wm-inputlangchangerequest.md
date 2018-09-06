---
Description: Posted to the window with the focus when the user chooses a new input language, either with the hotkey (specified in the Keyboard control panel application) or from the indicator on the system taskbar.
ms.assetid: db38c31c-6ae4-4401-82b8-7fd220c1678c
title: WM_INPUTLANGCHANGEREQUEST message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_INPUTLANGCHANGEREQUEST message

Posted to the window with the focus when the user chooses a new input language, either with the hotkey (specified in the Keyboard control panel application) or from the indicator on the system taskbar. An application can accept the change by passing the message to the [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function or reject the change (and prevent it from taking place) by returning immediately.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_INPUTLANGCHANGEREQUEST       0x0050
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The new input locale. This parameter can be a combination of the following flags.



| Value                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INPUTLANGCHANGE_BACKWARD"></span><span id="inputlangchange_backward"></span><dl> <dt>**INPUTLANGCHANGE\_BACKWARD**</dt> <dt>0x0004</dt> </dl>       | A hot key was used to choose the previous input locale in the installed list of input locales. This flag cannot be used with the INPUTLANGCHANGE\_FORWARD flag.<br/> |
| <span id="INPUTLANGCHANGE_FORWARD"></span><span id="inputlangchange_forward"></span><dl> <dt>**INPUTLANGCHANGE\_FORWARD**</dt> <dt>0x0002</dt> </dl>          | A hot key was used to choose the next input locale in the installed list of input locales. This flag cannot be used with the INPUTLANGCHANGE\_BACKWARD flag.<br/>    |
| <span id="INPUTLANGCHANGE_SYSCHARSET"></span><span id="inputlangchange_syscharset"></span><dl> <dt>**INPUTLANGCHANGE\_SYSCHARSET**</dt> <dt>0x0001</dt> </dl> | The new input locale's keyboard layout can be used with the system character set.<br/>                                                                               |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The input locale identifier. For more information, see [Languages, Locales, and Keyboard Layouts](https://msdn.microsoft.com/en-us/library/ms646267(v=VS.85).aspx).

</dd> </dl>

## Return value

Type: **LRESULT**

This message is posted, not sent, to the application, so the return value is ignored. To accept the change, the application should pass the message to [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx). To reject the change, the application should return zero without calling **DefWindowProc**.

## Remarks

When the [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function receives the **WM\_INPUTLANGCHANGEREQUEST** message, it activates the new input locale and notifies the application of the change by sending the [**WM\_INPUTLANGCHANGE**](wm-inputlangchange.md) message.

The language indicator is present on the taskbar only if you have installed more than one keyboard layout and if you have enabled the indicator using the Keyboard control panel application.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx)
</dt> <dt>

[**WM\_INPUTLANGCHANGE**](wm-inputlangchange.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




