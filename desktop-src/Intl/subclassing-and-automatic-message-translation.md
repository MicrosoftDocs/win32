---
Description: 'Subclassing is a technique that allows an application to intercept and process messages sent or posted to a particular window before a window procedure has a chance to process them.'
ms.assetid: '6f7ee9ff-479d-4cb0-8de1-1c3b671551f9'
title: Subclassing and Automatic Message Translation
---

# Subclassing and Automatic Message Translation

Subclassing is a technique that allows an application to intercept and process messages sent or posted to a particular window before a window procedure has a chance to process them. The operating system automatically translates messages into [Windows (ANSI) code page](code-pages.md) or [Unicode](unicode.md) form, depending on the form of the function that has subclassed the window procedure.

The following call to the [**SetWindowLongA**](_win32_setwindowlong_cpp) function subclasses the current window procedure associated with the window identified by the *hWnd* parameter. Alternatively, an application can use [**SetWindowLongPtrA**](_win32_SetWindowLongPtr_cpp). The new window procedure **NewWndProc**, will receive messages with text in Windows code page format.


```C++
OldWndProc = (WNDPROC) SetWindowLongA(hWnd,
             GWL_WNDPROC, (LONG)NewWndProc); 
```



When **NewWndProc** has finished processing a message, it uses the [**CallWindowProc**](_win32_callwindowproc_cpp) function as follows to pass the message to **OldWndProc**.


```C++
CallWindowProc(OldWndProc, hWnd, uMessage, wParam, lParam);
```



If **OldWndProc** was created with a class style of UNICODE, messages are translated from the Windows code page form received by **NewWndProc** into Unicode.

Similarly, a call to the [**SetWindowLongW**](_win32_setwindowlong_cpp) or [**SetWindowLongPtrW**](_win32_SetWindowLongPtr_cpp) function subclasses the current window procedure with a window procedure that expects Unicode text messages. Message translation, if necessary, is performed during the processing of the [**CallWindowProc**](_win32_CallWindowProc_cpp) function.

For more information about subclassing, see [Window Procedures](_win32_window_procedures_cpp).

## Related topics

<dl> <dt>

[Using Unicode and Character Sets](using-unicode-and-character-sets.md)
</dt> </dl>

 

 



