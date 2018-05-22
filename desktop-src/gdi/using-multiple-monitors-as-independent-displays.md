---
Description: 'When using multiple monitors as independent displays, the desktop contains one display or set of displays.'
ms.assetid: 'fbc88c91-3209-4b59-bdbb-0f5ba009a312'
title: Using Multiple Monitors as Independent Displays
---

# Using Multiple Monitors as Independent Displays

When using multiple monitors as independent displays, the desktop contains one display or set of displays. This set of displays always includes the primary monitor and behaves as mentioned in the other sections of this topic. An application can use any other monitor as an independent display.

> [!Note]  
> Using other monitors as independent displays isn't supported on drivers that are implemented to the Windows Display Driver Model (WDDM).

 

The window manager knows nothing about the independent displays. They are completely controlled by the application, and no window manager functions are available to the application (all window manager calls automatically go to the primary display). Each independent display has its own origin and horizontal and vertical coordinates, and is accessed through the GDI functions such as [**CreateDC**](createdc.md) or the DirectX functions such as **DirectDrawCreate**.

To locate the independent displays, call [**EnumDisplayDevices**](enumdisplaydevices.md) and look for the displays that do not have DISPLAY\_DEVICE\_ATTACHED\_TO\_DESKTOP flag in the [**DISPLAY\_DEVICE**](display-device.md) structure.

An application can open a display by calling


```C++
hdc = CreateDC(lpszDisplayName, NULL, NULL, lpDevMode);
```



In this call, the *lpszDisplayName* parameter is one of the device names returned by [**EnumDisplayDevices**](enumdisplaydevices.md) and *lpDevMode* is a description of the graphics mode for this device. The resulting hdc can be used to perform any graphics operation to the device.

 

 



