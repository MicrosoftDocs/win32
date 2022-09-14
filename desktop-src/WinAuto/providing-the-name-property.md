---
title: Providing the Name Property
description: Server developers must take care when creating predefined and common controls to ensure that Microsoft Active Accessibility can expose the Name property for the control.
ms.assetid: 2b4ec5ae-bda1-41e6-9387-6ee3cb6c3163
ms.topic: article
ms.date: 05/31/2018
---

# Providing the Name Property

Server developers must take care when creating predefined and common controls to ensure that Microsoft Active Accessibility can expose the [Name property](name-property.md) for the control. Depending on the type of control, the text for the Name property comes from one of the following:

-   The control's window text (or caption)
-   Static text that labels the control

To find the control's window text, Microsoft Active Accessibility sends the [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext) message to the control. This text corresponds to the text parameter in the control's resource definition statement. For some controls, such as buttons, this is the same text that is displayed with the control. For other controls, such as toolbars, this text is not displayed. Therefore, server developers must provide meaningful text in the control's resource definition statement to help users of client utilities identify the control.

To find the control's label, Microsoft Active Accessibility searches for a static text control by calling [**GetWindow**](/windows/desktop/api/winuser/nf-winuser-getwindow) with the GW\_HWNDPREV flag. The search is halted if a static text control is found, or if a control is encountered that has the window styles WS\_GROUP \| WS\_TABSTOP. This search order corresponds to the reverse tab order on a dialog box. Server developers must observe the tab order when creating controls so that a static text control immediately precedes the control that it labels.

For more information about the techniques that Microsoft Active Accessibility uses to expose the [Name property](name-property.md), see [User Interface Element Reference](user-interface-element-reference.md).

 

 