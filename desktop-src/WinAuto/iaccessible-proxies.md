---
title: IAccessible Proxies
description: IAccessible proxies provide default accessibility information for standard UI elements USER controls, USER menus, and common controls from COMCTL and COMCTL32.
ms.assetid: 236c2064-de44-4021-8825-f1519312dbfc
ms.topic: article
ms.date: 05/31/2018
---

# IAccessible Proxies

[**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) proxies provide default accessibility information for standard UI elements: USER controls, USER menus, and common controls from COMCTL and COMCTL32. This default support is exposed through **IAccessible** objects created by Oleacc.dll and delivers Microsoft Active Accessibility support without additional server development work. The server can then use the [Dynamic Annotation API](dynamic-annotation-api.md) to modify much of the information exposed by Oleacc.dll, but it does not have complete control.

## Creating a Proxy

To determine whether a UI element natively supports the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface, Oleacc.dll sends it a [**WM\_GETOBJECT**](wm-getobject.md) message. A nonzero return value means the element natively supports Microsoft Active Accessibility and provides its own **IAccessible** support. However, if the return value is zero, Oleacc.dll provides a proxy object for the UI element and attempts to return meaningful information on its behalf. For more information about **WM\_GETOBJECT**, see [How WM\_GETOBJECT Works](how-wm-getobject-works.md).

## What Information Is Exposed

Oleacc.dll uses the UI element's Windows class name to determine what information should be exposed for each of its [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and how to collect that information. For example, Oleacc.dll calls the [**GetWindowText**](/windows/desktop/api/winuser/nf-winuser-getwindowtexta) function to retrieve the [**Name**](name-property.md) property for a standard push button, but calls this same function to retrieve the [**Value**](value-property.md) property for a standard edit control. In effect, Oleacc.dll is mapping each **IAccessible** method to an appropriate Microsoft Win32 or control-specific message or function call. By using this class name-based special casing, it can return meaningful information through **IAccessible** proxies without any Microsoft Active Accessibility support in the server.

Applications built with standard UI elements typically get full Microsoft Active Accessibility support without additional development work. The exceptions to this rule are controls that have been subclassed, that do not store their own strings (absence of the **HASSTRINGS** style), or that are owner-drawn. In these cases, Oleacc.dll cannot gather the information it needs because the information is stored outside the control. However in many of these scenarios, established workarounds, or the use of Dynamic Annotation, allow the server to cooperate with the proxies provided by Oleacc.dll.

## Generic Proxy Objects

If Oleacc.dll does not recognize the class name of the UI element, it creates a generic proxy that exposes as much information as possible. At most, this includes the object's bounding rectangle, parent object, name (from [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)), and any children in the window hierarchy.

 

 