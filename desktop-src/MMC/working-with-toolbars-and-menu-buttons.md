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

MMC creates it easy to use toolbars and menu buttons — two of the most frequently included features in today's applications. There are several interfaces related to these features, beginning with [**IControlbar**](icontrolbar.md). This interface allows for creating and manipulating a control bar to hold toolbars and other controls. This interface's methods include [**Create**](icontrolbar-create.md), which is used to create and return the requested control — either a toolbar or a drop-down menu. The other **IControlbar** methods are [**Attach**](icontrolbar-attach.md), which associates a control with the control bar, and [**Detach**](icontrolbar-detach.md), which breaks that association. You should also use these methods to display or hide a toolbar or menu button.

The [**IExtendControlbar**](iextendcontrolbar.md) interface enables a snap-in to add toolbars and menu buttons by using a callback interface, and has two methods. The first is [**SetControlBar**](iextendcontrolbar-setcontrolbar.md), which gets a pointer to the [**IControlbar**](icontrolbar.md) interface implemented by the console. The second method, [**ControlbarNotify**](iextendcontrolbar-controlbarnotify.md), is the mechanism that allows the snap-in to respond to user actions such as mouse-button clicks. When the user causes an event, MMC sends a notification message to the snap-in. All notifications applicable to toolbars and menu buttons are listed in the documentation of the **ControlbarNotify** method.

The [**IToolbar**](itoolbar.md) interface is implemented by the console. It allows your snap-in to perform a variety of actions related to toolbars, including creating them, adding items to them, extending them, and that displays them. The [**AddBitmap**](itoolbar-addbitmap.md) method allows you to add images to the toolbar, and the [**AddButtons**](itoolbar-addbuttons.md) method provides a way to add an array of buttons to the toolbar. To add a single button, you can use the [**InsertButton**](itoolbar-insertbutton.md) method; to remove one, you can use the [**DeleteButton**](itoolbar-deletebutton.md) method. Finally, you can get an attribute of a button by using the [**GetButtonState**](itoolbar-getbuttonstate.md) method and set an attribute with the [**SetButtonState**](itoolbar-setbuttonstate.md) method.

The [**IMenuButton**](imenubutton.md) interface is also implemented by the console. The interface enables a snap-in to add menu buttons to the console's menu bar. MMC provides one menu bar per view; when a snap-in has the focus you can add one or more menu buttons for the view to this bar. These buttons are always added by appending them to the buttons already in the menu bar.

The [**IMenuButton**](imenubutton.md) interface has three methods. These methods allow you to add and set the attributes and states of menu buttons. The [**AddButton**](imenubutton-addbutton.md) method enables you to add a button to the MMC menu bar for a particular view. The [**SetButton**](imenubutton-setbutton.md) method can then be used to set the text attributes of a button in the menu bar. Finally, the [**SetButtonState**](imenubutton-setbuttonstate.md) method enables you to change the state of a menu button.

The last interface you have to consider when working with toolbars is [**IConsoleVerb**](iconsoleverb.md). The verbs — which include cut, copy, paste, print, and others you would expect to see — are listed in the [**MMC\_CONSOLE\_VERB**](mmc-console-verb.md) enumeration. You can determine the state of a verb by using the [**GetVerbState**](iconsoleverb-getverbstate.md) method; you can set the state with the [**SetVerbState**](iconsoleverb-setverbstate.md) method.

An extension snap-in can add toolbar buttons and menu buttons for node types that it does not own (that is, node types added by a primary snap-in). MMC always calls an extension snap-in's implementation of the [**IExtendControlbar::SetControlBar**](iextendcontrolbar-setcontrolbar.md) method if that snap-in implements the [**IExtendControlbar**](iextendcontrolbar.md) interface. The extension snap-in can use the [**IControlbar**](icontrolbar.md) interface passed to it in **SetControlBar** to attach a toolbar or menu button control to a primary snap-in's control bar and then add buttons and manipulate them using the [**IToolbar**](itoolbar.md) or [**IMenuButton**](imenubutton.md) interface.

Be aware that the extension snap-in manipulates a primary snap-in's control bar in the same way that the primary snap-in does. That is, programmatically the extension "owns" the control, so it need not consider any other snap-ins when dealing with issues such as the index values of bitmaps placed on the toolbar, or the command ID of items placed in a menu button. The only requirement for the extension snap-in is that it explicitly register itself as being a toolbar extension for items (scope or result) of the particular node type it wants to extend. For more information, see [Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md).

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Working with Toolbars: Implementation Details](working-with-toolbars-implementation-details.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




