---
Description: Sent when a window is being destroyed. It is sent to the window procedure of the window being destroyed after the window is removed from the screen.
ms.assetid: 089c0645-199b-4a90-9cbc-740f0cf3267d
title: WM\_DESTROY message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_DESTROY message

Sent when a window is being destroyed. It is sent to the window procedure of the window being destroyed after the window is removed from the screen.

This message is sent first to the window being destroyed and then to the child windows (if any) as they are destroyed. During the processing of the message, it can be assumed that all child windows still exist.

A window receives this message through its [**WindowProc**](/windows/desktop/api/Winuser/nf-winuser-callwindowproca) function.


```C++
#define WM_DESTROY                      0x0002
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

If the window being destroyed is part of the clipboard viewer chain (set by calling the [**SetClipboardViewer**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\dataexchange\clipboard\clipboardreference\clipboardfunctions\setclipboardviewer.htm) function), the window must remove itself from the chain by processing the [**ChangeClipboardChain**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\dataexchange\clipboard\clipboardreference\clipboardfunctions\changeclipboardchain.htm) function before returning from the **WM\_DESTROY** message.

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

[**ChangeClipboardChain**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\dataexchange\clipboard\clipboardreference\clipboardfunctions\changeclipboardchain.htm)
</dt> <dt>

[**DestroyWindow**](/windows/desktop/api/Winuser/nf-winuser-destroywindow)
</dt> <dt>

[**PostQuitMessage**](/windows/desktop/api/Winuser/nf-winuser-postquitmessage)
</dt> <dt>

[**SetClipboardViewer**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\dataexchange\clipboard\clipboardreference\clipboardfunctions\setclipboardviewer.htm)
</dt> <dt>

[**WM\_CLOSE**](wm-close.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




