---
description: Description of substandard techniques for exposing custom controls.
ms.assetid: 107968c6-c3b3-462d-b488-96c69f2b3b14
title: Substandard Techniques for Exposing Custom Controls
ms.topic: article
ms.date: 05/31/2018
---

# Substandard Techniques for Exposing Custom Controls

If an application does not support Microsoft Active Accessibility, it may not be fully accessible. The following techniques render controls partially compatible:

-   Return a descriptive string when the control is queried by using the WM\_GETTEXT message. For example, allow a custom equivalent of a button control labeled "Print" to return the string "Print button." This identifies both control type and label. The same string is appropriate for a button with a label that is something other than text, such as a graphic of a printer. Similarly, allow a custom control that behaves like a check box to return the caption string "Printing Enabled check box, checked."
-   Support the WM\_GETDLGCODE message, identifying the keyboard input that is supported. For example, allow a custom equivalent of an edit control to handle WM\_GETDLGCODE by returning DLGC\_HASSETSEL if it handles messages to set the selection, DLGC\_WANTARROWS if it uses arrow keys, and DLGC\_WANTCHARS to indicate that it uses character input.
    > [!Note]  
    > Only controls that have their own window handles can respond to the WM\_GETTEXT and WM\_GETDLGCODE messages.

     

To avoid compatibility problems with accessibility aids, you should follow Active Accessibility guidelines closely when designing custom controls. For more information about how to avoid compatibility problems with accessibility aids, see the [Accessibility](../accessibility/accessibility.md) section.

 

 
