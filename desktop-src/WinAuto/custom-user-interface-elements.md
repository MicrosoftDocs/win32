---
title: Custom User Interface Elements
description: Server developers design accessible objects based on an application's UI.
ms.assetid: d9453fb0-9b4a-4103-81e3-1255091255a0
ms.topic: article
ms.date: 05/31/2018
---

# Custom User Interface Elements

Server developers design accessible objects based on an application's UI. Because [Active Accessibility implements the IAccessible interface on behalf of system-provided user interface elements](appendix-a--supported-user-interface-elements-reference.md) such as list boxes, menus, and trackbar controls, you need to implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface only for the following kinds of custom UI elements:

-   Custom controls created by registering an application-defined window class
-   Custom controls drawn directly on the screen that do not have an associated **HWND**
-   Custom controls such as Microsoft ActiveX and Java controls
-   Controls or objects in the application's client window that aren't already exposed

Owner-drawn controls and menus are accessible as long as you follow the guidelines discussed in [Shortcuts for Exposing Custom User Interface Elements](shortcuts-for-exposing-custom-user-interface-elements.md). If you follow these guidelines, then you do not need to implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface for owner-drawn controls and menus.

In most cases, superclassed and subclassed controls are accessible because the system handles the basic functionality of the control. However, if a superclassed or subclassed control significantly modifies the behavior of the system-provided control on which it is based, then you must implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. For more information, see [Exposing Controls Based on System Controls](exposing-controls-based-on-system-controls.md).

If an application uses only system-provided user interface elements, then it does not need to implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible), except for its client window. For example, an application that includes a text editor, not implemented using an edit control, exposes lines of text as accessible objects. Note that Microsoft Active Accessibility automatically exposes the text in edit and rich edit controls as a single string of text in the [**Value**](value-property.md) property of the control.

 

 




