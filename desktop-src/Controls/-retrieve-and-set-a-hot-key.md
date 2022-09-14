---
title: How to Retrieve and Set a Hot Key
description: This topic demonstrates how to retrieve or set the key combination for a hot key control.
ms.assetid: F3643196-F847-4EE4-97ED-75AF52D4FF8D
ms.topic: article
ms.date: 05/31/2018
---

# How to Retrieve and Set a Hot Key

This topic demonstrates how to retrieve or set the key combination for a hot key control. The [**HKM\_SETHOTKEY**](hkm-sethotkey.md) message allows an application to set the hot key combination for a hot key control. Applications use the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message to retrieve the virtual key code and modifier flags of the hot key that is chosen by the user.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


Use the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message to retrieve the virtual key code and modifier keys that describe a hot key chosen by the user. Use the [**HKM\_SETHOTKEY**](hkm-sethotkey.md) message to set those values for a hot key.

In the following C++ code example, the application-defined function uses the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message to retrieve a key combination from a hot key control and then uses the [**WM\_SETHOTKEY**](/windows/desktop/inputdev/wm-sethotkey) message to set a global hot key. Note that you cannot set a global hot key for a window that has the [**WS\_CHILD**](/windows/desktop/winmsg/window-styles) window style.



```C++
// Retrieves the hot key from the hot key control and sets it as
// the hot key for the application's main window. 
//
// Parameters 
//     hwndHot  - Handle of the hot key control. 
//     hwndMain - Handle of the main window. 

BOOL WINAPI ProcessHotkey(HWND hwndHot, HWND hwndMain) 
{ 
    WORD wHotkey;  

    // Retrieve the hot key (virtual key code and modifiers). 
    wHotkey = (WORD) SendMessage(hwndHot, HKM_GETHOTKEY, 0, 0); 
    
    // Use the result as wParam for WM_SETHOTKEY. 
    SendMessage(hwndMain, WM_SETHOTKEY, wHotkey, 0); 
    return TRUE;
}
```



## Related topics

<dl> <dt>

[Hot Key Control Reference](bumper-hot-key-hot-key-control-reference.md)
</dt> <dt>

[About Hot Key Controls](hot-key-controls.md)
</dt> <dt>

[Using Hot Key Controls](using-hot-key-controls.md)
</dt> </dl>

 

 