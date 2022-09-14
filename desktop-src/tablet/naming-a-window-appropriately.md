---
description: Overview of naming a window appropriately and setting the window caption for the Tablet PC.
ms.assetid: 9d064188-53a1-4cb5-b516-99610d7b8134
title: Naming a Window Appropriately
ms.topic: article
ms.date: 05/31/2018
---

# Naming a Window Appropriately

Assign every window a user-friendly caption, even if the window or its caption is invisible. This allows the speech functionality to identify the window and the window hierarchy. This recommendation applies to all windows: top-level windows with visible frames; child windows, such as floating palettes; custom controls; toolbars; and panes within a window, when implemented as child windows.

There are three ways to set the window caption:

-   Set the string in your resource script when calling [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or related functions.
-   Call the [**SetWindowText**](/windows/desktop/api/winuser/nf-winuser-setwindowtexta) function.
-   Define the name of controls in dialog boxes by using the techniques described in [Naming Controls in Dialog Boxes](naming-controls-in-dialog-boxes.md). This is the only method for labeling an edit control, because setting the controls intrinsic label changes the controls contents.

You can query the caption by using either Microsoft Active Accessibility or the WM\_GETTEXT message.

For more information about querying the caption by using Active Accessibility, see the [Accessibility](/windows/desktop/accessibility) section.

 

 
