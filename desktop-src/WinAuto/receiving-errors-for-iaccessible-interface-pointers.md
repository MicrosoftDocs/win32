---
title: Receiving Errors for IAccessible Interface Pointers
description: This topic describes situations in which you might receive an error for an IAccessible interface pointer.
ms.assetid: 408bfa47-fda0-4a25-89c1-da41d967ad61
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Errors for IAccessible Interface Pointers

This topic describes situations in which you might receive an error for an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer. **IAccessible** functions can return errors for **IAccessible** interface pointers when a user closes an application that the object belongs to, or if a user dismisses a control through the user interface.

## User Closes an Application

If a user closes the application that contains an object to which the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer was pointing, then all future calls to that object will return an error code. The error, such as **CO\_E\_OBJNOTCONNECTED**, will indicate that the object does not exist anymore. This applies to all **IAccessible** interface pointers.

## User Dismisses a Control

If a user dismisses a control (for example, by pressing a push button), clients can still call [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods and properties on this object because the object has not been released. However, future calls will receive error messages.

This situation applies to the following functions and methods:

-   [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent)
-   [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
-   [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow)
-   [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**IAccessible::accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**IAccessible::get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)
-   [**IAccessible::get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection)

 

 




