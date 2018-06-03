---
title: Working with Toolbars and Menu Buttons
description: MMC creates it easy to use toolbars and menu buttons \ 8212; two of the most frequently included features in today's applications.
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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with Toolbars and Menu Buttons

MMC creates it easy to use toolbars and menu buttons — two of the most frequently included features in today's applications. There are several interfaces related to these features, beginning with [**IControlbar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar). This interface allows for creating and manipulating a control bar to hold toolbars and other controls. This interface's methods include [**Create**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-create), which is used to create and return the requested control — either a toolbar or a drop-down menu. The other **IControlbar** methods are [**Attach**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-attach), which associates a control with the control bar, and [**Detach**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-detach), which breaks that association. You should also use these methods to display or hide a toolbar or menu button.

The [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface enables a snap-in to add toolbars and menu buttons by using a callback interface, and has two methods. The first is [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar), which gets a pointer to the [**IControlbar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar) interface implemented by the console. The second method, [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify), is the mechanism that allows the snap-in to respond to user actions such as mouse-button clicks. When the user causes an event, MMC sends a notification message to the snap-in. All notifications applicable to toolbars and menu buttons are listed in the documentation of the **ControlbarNotify** method.

The [**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar) interface is implemented by the console. It allows your snap-in to perform a variety of actions related to toolbars, including creating them, adding items to them, extending them, and that displays them. The [**AddBitmap**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbitmap) method allows you to add images to the toolbar, and the [**AddButtons**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbuttons) method provides a way to add an array of buttons to the toolbar. To add a single button, you can use the [**InsertButton**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-insertbutton) method; to remove one, you can use the [**DeleteButton**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-deletebutton) method. Finally, you can get an attribute of a button by using the [**GetButtonState**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-getbuttonstate) method and set an attribute with the [**SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-setbuttonstate) method.

The [**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton) interface is also implemented by the console. The interface enables a snap-in to add menu buttons to the console's menu bar. MMC provides one menu bar per view; when a snap-in has the focus you can add one or more menu buttons for the view to this bar. These buttons are always added by appending them to the buttons already in the menu bar.

The [**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton) interface has three methods. These methods allow you to add and set the attributes and states of menu buttons. The [**AddButton**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-addbutton) method enables you to add a button to the MMC menu bar for a particular view. The [**SetButton**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-setbutton) method can then be used to set the text attributes of a button in the menu bar. Finally, the [**SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-imenubutton-setbuttonstate) method enables you to change the state of a menu button.

The last interface you have to consider when working with toolbars is [**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb). The verbs — which include cut, copy, paste, print, and others you would expect to see — are listed in the [**MMC\_CONSOLE\_VERB**](/windows/desktop/api/Mmc/ne-mmc-_mmc_console_verb) enumeration. You can determine the state of a verb by using the [**GetVerbState**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-getverbstate) method; you can set the state with the [**SetVerbState**](/windows/desktop/api/Mmc/nf-mmc-iconsoleverb-setverbstate) method.

An extension snap-in can add toolbar buttons and menu buttons for node types that it does not own (that is, node types added by a primary snap-in). MMC always calls an extension snap-in's implementation of the [**IExtendControlbar::SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar) method if that snap-in implements the [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface. The extension snap-in can use the [**IControlbar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar) interface passed to it in **SetControlBar** to attach a toolbar or menu button control to a primary snap-in's control bar and then add buttons and manipulate them using the [**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar) or [**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton) interface.

Be aware that the extension snap-in manipulates a primary snap-in's control bar in the same way that the primary snap-in does. That is, programmatically the extension "owns" the control, so it need not consider any other snap-ins when dealing with issues such as the index values of bitmaps placed on the toolbar, or the command ID of items placed in a menu button. The only requirement for the extension snap-in is that it explicitly register itself as being a toolbar extension for items (scope or result) of the particular node type it wants to extend. For more information, see [Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md).

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Working with Toolbars: Implementation Details](working-with-toolbars-implementation-details.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




