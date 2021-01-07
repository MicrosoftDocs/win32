---
description: The operating system sends IME window messages to the window procedure of an application when certain events occur that affect the IME windows.
ms.assetid: 7eac1ab7-d04b-4e1b-9e2c-fa9a778756cd
title: IME Messages
ms.topic: article
ms.date: 05/31/2018
---

# IME Messages

The operating system sends IME window messages to the window procedure of an application when certain events occur that affect the IME windows. For example, the operating system sends the [**WM\_IME\_SETCONTEXT**](wm-ime-setcontext.md) message to the application when a window is activated. IME-unaware applications pass these messages to the [DefWindowProc](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, which sends them to the corresponding default IME window. IME-aware applications either process these messages or forward them to their own IME windows.

Your application can direct an IME window to carry out a command, for example, change the position of a composition window, by using the [**WM\_IME\_CONTROL**](wm-ime-control.md) message. The IME notifies the application about changes to the composition string by using the [**WM\_IME\_COMPOSITION**](wm-ime-composition.md) message, and about general changes to the status of the IME windows by sending the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message.

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 
