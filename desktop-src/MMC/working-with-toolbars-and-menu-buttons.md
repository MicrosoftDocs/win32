---
title: Working with Toolbars and Menu Buttons
description: MMC creates it easy to use toolbars and menu buttons \ 8212; two of the most frequently included features in todays applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ebf7c785-822f-4121-9915-b63fa3e2b5d8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- toolbars and menu buttons MMC
- toolbars and menu buttons MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with Toolbars and Menu Buttons

MMC creates it easy to use toolbars and menu buttons — two of the most frequently included features in today's applications. There are several interfaces related to these features, beginning with [**IControlbar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master). This interface allows for creating and manipulating a control bar to hold toolbars and other controls. This interface's methods include [**Create**](/windows/win32/Mmc/nf-mmc-icontrolbar-create?branch=master), which is used to create and return the requested control — either a toolbar or a drop-down menu. The other **IControlbar** methods are [**Attach**](/windows/win32/Mmc/nf-mmc-icontrolbar-attach?branch=master), which associates a control with the control bar, and [**Detach**](/windows/win32/Mmc/nf-mmc-icontrolbar-detach?branch=master), which breaks that association. You should also use these methods to display or hide a toolbar or menu button.

The [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface enables a snap-in to add toolbars and menu buttons by using a callback interface, and has two methods. The first is [**SetControlBar**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar?branch=master), which gets a pointer to the [**IControlbar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master) interface implemented by the console. The second method, [**ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), is the mechanism that allows the snap-in to respond to user actions such as mouse-button clicks. When the user causes an event, MMC sends a notification message to the snap-in. All notifications applicable to toolbars and menu buttons are listed in the documentation of the **ControlbarNotify** method.

The [**IToolbar**](/windows/win32/Mmc/nn-mmc-itoolbar?branch=master) interface is implemented by the console. It allows your snap-in to perform a variety of actions related to toolbars, including creating them, adding items to them, extending them, and that displays them. The [**AddBitmap**](/windows/win32/Mmc/nf-mmc-itoolbar-addbitmap?branch=master) method allows you to add images to the toolbar, and the [**AddButtons**](/windows/win32/Mmc/nf-mmc-itoolbar-addbuttons?branch=master) method provides a way to add an array of buttons to the toolbar. To add a single button, you can use the [**InsertButton**](/windows/win32/Mmc/nf-mmc-itoolbar-insertbutton?branch=master) method; to remove one, you can use the [**DeleteButton**](/windows/win32/Mmc/nf-mmc-itoolbar-deletebutton?branch=master) method. Finally, you can get an attribute of a button by using the [**GetButtonState**](/windows/win32/Mmc/nf-mmc-itoolbar-getbuttonstate?branch=master) method and set an attribute with the [**SetButtonState**](/windows/win32/Mmc/nf-mmc-itoolbar-setbuttonstate?branch=master) method.

The [**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master) interface is also implemented by the console. The interface enables a snap-in to add menu buttons to the console's menu bar. MMC provides one menu bar per view; when a snap-in has the focus you can add one or more menu buttons for the view to this bar. These buttons are always added by appending them to the buttons already in the menu bar.

The [**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master) interface has three methods. These methods allow you to add and set the attributes and states of menu buttons. The [**AddButton**](/windows/win32/Mmc/nf-mmc-imenubutton-addbutton?branch=master) method enables you to add a button to the MMC menu bar for a particular view. The [**SetButton**](/windows/win32/Mmc/nf-mmc-imenubutton-setbutton?branch=master) method can then be used to set the text attributes of a button in the menu bar. Finally, the [**SetButtonState**](/windows/win32/Mmc/nf-mmc-imenubutton-setbuttonstate?branch=master) method enables you to change the state of a menu button.

The last interface you have to consider when working with toolbars is [**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master). The verbs — which include cut, copy, paste, print, and others you would expect to see — are listed in the [**MMC\_CONSOLE\_VERB**](/windows/win32/Mmc/ne-mmc-_mmc_console_verb?branch=master) enumeration. You can determine the state of a verb by using the [**GetVerbState**](/windows/win32/Mmc/nf-mmc-iconsoleverb-getverbstate?branch=master) method; you can set the state with the [**SetVerbState**](/windows/win32/Mmc/nf-mmc-iconsoleverb-setverbstate?branch=master) method.

An extension snap-in can add toolbar buttons and menu buttons for node types that it does not own (that is, node types added by a primary snap-in). MMC always calls an extension snap-in's implementation of the [**IExtendControlbar::SetControlBar**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar?branch=master) method if that snap-in implements the [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface. The extension snap-in can use the [**IControlbar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master) interface passed to it in **SetControlBar** to attach a toolbar or menu button control to a primary snap-in's control bar and then add buttons and manipulate them using the [**IToolbar**](/windows/win32/Mmc/nn-mmc-itoolbar?branch=master) or [**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master) interface.

Be aware that the extension snap-in manipulates a primary snap-in's control bar in the same way that the primary snap-in does. That is, programmatically the extension "owns" the control, so it need not consider any other snap-ins when dealing with issues such as the index values of bitmaps placed on the toolbar, or the command ID of items placed in a menu button. The only requirement for the extension snap-in is that it explicitly register itself as being a toolbar extension for items (scope or result) of the particular node type it wants to extend. For more information, see [Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md).

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Working with Toolbars: Implementation Details](working-with-toolbars-implementation-details.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




