---
description: Description of using customer controls for the Tablet PC.
ms.assetid: 43d78acd-1f02-417d-97be-1682e90a81a2
title: Using Custom Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using Custom Controls

You can customize standard controls by using owner-drawing to change the control's appearance and establishing a superclass or subclass to change the control's behavior. In each case, the underlying system code for the standard control type handles basic control functions. Most of these controls can be accessible if you use them properly.

An owner-drawn control that is based on a standard control appears as the standard control to accessibility aids and supports Microsoft Active Accessibility; however, it has a customized appearance. Some applications use custom controls to change the appearance of a control, but owner-drawn controls are a more accessible solution. For more information about how to define owner-drawn menus and expose owner-drawn controls, see [Accessibility](../accessibility/accessibility.md).

Establishing a superclass or subclass is a technique for customizing the behavior of existing controls. Depending on the new behavior of the control, it may be necessary to supplement the accessibility information that it exposes. For example, an application can use an owner-drawn control to display an X in a selected check box, rather than a check mark, or label a command button with a picture instead of a word.

When using owner-drawn controls that are either a superclass or a subclass:

-   Provide labels for all controls, even when the labels are not visible on the screen. If you customize a control so that the standard caption is not visible (for example, a button with a graphic face) and leave the caption as a blank string, the accessibility aid is not able to get the caption and use it to identify the control.
-   Ensure that [**WM\_GETTEXT**](../winmsg/wm-gettext.md) is supported.
-   Ensure that all class-specific messages are supported. It is especially important to support text-retrieval messages such as [**CB\_GETLBTEXT**](../controls/cb-getlbtext.md) and [**LB\_GETTEXT**](../controls/lb-gettext.md). Set the appropriate style bits, such as **CBS\_HASSTRINGS** and **LBS\_HASSTRINGS**, to indicate the control supports those messages.

 

 
