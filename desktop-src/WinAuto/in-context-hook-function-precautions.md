---
title: In-Context Hook Function Precautions
description: For performance reasons, client developers register in-context hook functions.
ms.assetid: 14b48920-a291-4519-b005-e559263a0e83
ms.topic: article
ms.date: 05/31/2018
---

# In-Context Hook Function Precautions

For performance reasons, client developers register in-context hook functions. However, because these hook functions are mapped into the server's address space, client and server developers must take precautions to ensure that the event processing goes smoothly.

## Precautions for Client Developers

Client developers should be aware of the following issues:

-   In-context hook functions should not use a lot of processor time, because the hook function must return before the server application continues.
-   After an event is triggered, it is possible that the window associated with an event no longer exists by the time the hook function is called. Clients must verify that the window associated with an event still exists before taking any other action related to the event. To ensure that a window still exists, clients use the Microsoft Win32 [**IsWindow**](/windows/desktop/api/winuser/nf-winuser-iswindow) function.
-   If the DLL in which the hook function is defined links to another DLL, client developers must ensure that the system loads the other DLL. If linking implicitly (using .def files and imports), the additional DLL must be in either the Windows directory or one of the system directories such as Windows\\System, Windows\\System32, or Windows\\SysWOW64. If linking explicitly (using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya)), the full path to the directory in which the additional DLL resides must be specified in the call to **LoadLibrary**.
-   In-context hook functions may cause a stack overflow when the DLL that contains the hook function is loaded into a 16-bit application. This problem occurs because 16-bit applications use a fixed stack size that is not large enough to accommodate the chain of system function calls that result in a call to the hook function.

## Precautions for Server Developers

Server developers need to be aware that client applications might register in-context hook functions. When a server calls [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent), it must be prepared to handle [**WM\_GETOBJECT**](wm-getobject.md) and other [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods.

## Invalid Interface Pointers

When a client calls [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent) within an in-context hook function, the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer that is returned points directly to code in the server's address space. If the client calls an interface property using this pointer, the Component Object Model (COM) library is not involved with marshaling (packaging and sending interface parameters across process boundaries) or unmarshaling (unpackaging parameters that have been sent across process boundaries) and does not detect if an object is destroyed.

If the client calls an interface property to an object that is destroyed, the invalid interface pointer causes a General Protection fault in the server's address space unless the server detects this situation.

To protect against invalid interface pointers, servers [create proxy objects](creating-proxy-objects.md) that wrap accessible objects and monitor the life span of accessible objects. For instance, when a client calls an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) property to get information about an object, the proxy checks whether the accessible object is still available, and if so, forwards the client's request to the accessible object. If the accessible object is destroyed, the proxy returns an error to the client.

 

 