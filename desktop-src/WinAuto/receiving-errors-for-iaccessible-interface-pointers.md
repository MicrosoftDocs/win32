---
title: Receiving Errors for IAccessible Interface Pointers
description: This topic describes situations in which you might receive an error for an IAccessible interface pointer.
ms.assetid: '408bfa47-fda0-4a25-89c1-da41d967ad61'
---

# Receiving Errors for IAccessible Interface Pointers

This topic describes situations in which you might receive an error for an [**IAccessible**](iaccessible.md) interface pointer. **IAccessible** functions can return errors for **IAccessible** interface pointers when a user closes an application that the object belongs to, or if a user dismisses a control through the user interface.

## User Closes an Application

If a user closes the application that contains an object to which the [**IAccessible**](iaccessible.md) interface pointer was pointing, then all future calls to that object will return an error code. The error, such as **CO\_E\_OBJNOTCONNECTED**, will indicate that the object does not exist anymore. This applies to all **IAccessible** interface pointers.

## User Dismisses a Control

If a user dismisses a control (for example, by pressing a push button), clients can still call [**IAccessible**](iaccessible.md) methods and properties on this object because the object has not been released. However, future calls will receive error messages.

This situation applies to the following functions and methods:

-   [**AccessibleObjectFromEvent**](accessibleobjectfromevent.md)
-   [**AccessibleObjectFromPoint**](accessibleobjectfrompoint.md)
-   [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md)
-   [**IAccessible::accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**IAccessible::accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**IAccessible::get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)
-   [**IAccessible::get\_accSelection**](iaccessible-iaccessible--get-accselection.md)

 

 




