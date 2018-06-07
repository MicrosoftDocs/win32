---
Description: Subclassing is a technique that allows an application to intercept and process messages sent or posted to a particular window before a window procedure has a chance to process them.
ms.assetid: 6f7ee9ff-479d-4cb0-8de1-1c3b671551f9
title: Subclassing and Automatic Message Translation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Subclassing and Automatic Message Translation

Subclassing is a technique that allows an application to intercept and process messages sent or posted to a particular window before a window procedure has a chance to process them. The operating system automatically translates messages into [Windows (ANSI) code page](code-pages.md) or [Unicode](unicode.md) form, depending on the form of the function that has subclassed the window procedure.

The following call to the [**SetWindowLongA**](https://www.bing.com/search?q=**SetWindowLongA**) function subclasses the current window procedure associated with the window identified by the *hWnd* parameter. Alternatively, an application can use [**SetWindowLongPtrA**](https://www.bing.com/search?q=**SetWindowLongPtrA**). The new window procedure **NewWndProc**, will receive messages with text in Windows code page format.


```C++
OldWndProc = (WNDPROC) SetWindowLongA(hWnd,
             GWL_WNDPROC, (LONG)NewWndProc); 
```



When **NewWndProc** has finished processing a message, it uses the [**CallWindowProc**](https://www.bing.com/search?q=**CallWindowProc**) function as follows to pass the message to **OldWndProc**.


```C++
CallWindowProc(OldWndProc, hWnd, uMessage, wParam, lParam);
```



If **OldWndProc** was created with a class style of UNICODE, messages are translated from the Windows code page form received by **NewWndProc** into Unicode.

Similarly, a call to the [**SetWindowLongW**](https://www.bing.com/search?q=**SetWindowLongW**) or [**SetWindowLongPtrW**](https://www.bing.com/search?q=**SetWindowLongPtrW**) function subclasses the current window procedure with a window procedure that expects Unicode text messages. Message translation, if necessary, is performed during the processing of the [**CallWindowProc**](https://www.bing.com/search?q=**CallWindowProc**) function.

For more information about subclassing, see [Window Procedures](https://www.bing.com/search?q=Window+Procedures).

## Related topics

<dl> <dt>

[Using Unicode and Character Sets](using-unicode-and-character-sets.md)
</dt> </dl>

 

 



