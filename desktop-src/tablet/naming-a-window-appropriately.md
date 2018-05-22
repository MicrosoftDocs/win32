---
Description: 'Overview of naming a window appropriately and setting the window caption for the Tablet PC.'
ms.assetid: '9d064188-53a1-4cb5-b516-99610d7b8134'
title: Naming a Window Appropriately
---

# Naming a Window Appropriately

Assign every window a user-friendly caption, even if the window or its caption is invisible. This allows the speech functionality to identify the window and the window hierarchy. This recommendation applies to all windows: top-level windows with visible frames; child windows, such as floating palettes; custom controls; toolbars; and panes within a window, when implemented as child windows.

There are three ways to set the window caption:

-   Set the string in your resource script when calling [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) or related functions.
-   Call the [**SetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633546) function.
-   Define the name of controls in dialog boxes by using the techniques described in [Naming Controls in Dialog Boxes](naming-controls-in-dialog-boxes.md). This is the only method for labeling an edit control, because setting the controls intrinsic label changes the controls contents.

You can query the caption by using either Microsoft Active Accessibility or the WM\_GETTEXT message.

For more information about querying the caption by using Active Accessibility, see the [Accessibility](https://msdn.microsoft.com/library/windows/desktop/ee663255) section.

 

 



