---
title: Creating Common Controls
description: This topic describes how to create a window that belongs to a window class defined in the common control library, Comctl32.dll.
ms.assetid: BCF25606-5B49-43A5-8107-E7220BE3253C
ms.topic: article
ms.date: 05/31/2018
---

# Creating Common Controls

This topic describes how to create a window that belongs to a window class defined in the common control library, Comctl32.dll.


Most common controls belong to a window class defined in the common control DLL. The window class and the corresponding window procedure define the properties, appearance, and behavior of the control. To ensure that the common control DLL is loaded, include the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function in your application. You create a common control by specifying the name of the window class when calling the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function or by specifying the appropriate class name in a dialog box template.


Each type of common control has a set of control styles that you can use to vary the appearance and behavior of the control. The common control library also includes a set of control styles that apply to two or more types of common controls. The common control styles are described in the [Styles](common-control-styles.md) section.

## Related topics

<dl> <dt>

[About Common Controls](common-controls-intro.md)
</dt> </dl>

 

 