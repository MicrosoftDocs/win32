---
description: The IME window class is a predefined system global class that defines the appearance and behavior of the standard IME windows.
ms.assetid: 0fa01d84-1304-4235-a148-ea5e8dd5d0b3
title: IME Window Class
ms.topic: article
ms.date: 05/31/2018
---

# IME Window Class

The IME window class is a predefined system global class that defines the appearance and behavior of the standard IME windows. The class is similar to common control classes in that the application creates a window of this class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. Like static controls, an IME window does not respond to user input by itself. Instead, it notifies the IME of user input actions and processes control messages sent to it by the IME or applications to carry out a response to the user action.

IME-aware applications sometimes create customized IME windows using the IME window class. Use of window customization allows the application to take advantage of the default processing of the IME window while having control of window positioning.

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 
