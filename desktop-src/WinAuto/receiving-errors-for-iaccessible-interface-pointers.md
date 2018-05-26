---
title: Receiving Errors for IAccessible Interface Pointers
description: This topic describes situations in which you might receive an error for an IAccessible interface pointer.
ms.assetid: 408bfa47-fda0-4a25-89c1-da41d967ad61
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving Errors for IAccessible Interface Pointers

This topic describes situations in which you might receive an error for an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer. **IAccessible** functions can return errors for **IAccessible** interface pointers when a user closes an application that the object belongs to, or if a user dismisses a control through the user interface.

## User Closes an Application

If a user closes the application that contains an object to which the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer was pointing, then all future calls to that object will return an error code. The error, such as **CO\_E\_OBJNOTCONNECTED**, will indicate that the object does not exist anymore. This applies to all **IAccessible** interface pointers.

## User Dismisses a Control

If a user dismisses a control (for example, by pressing a push button), clients can still call [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods and properties on this object because the object has not been released. However, future calls will receive error messages.

This situation applies to the following functions and methods:

-   [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master)
-   [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master)
-   [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master)
-   [**IAccessible::accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**IAccessible::get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)
-   [**IAccessible::get\_accSelection**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accselection?branch=master)

 

 




