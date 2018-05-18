---
title: Working with Toolbars Implementation Details
description: Working with Toolbars Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '53ad9866-0dd1-469c-acec-0277546c14e7'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["toolbars and menu buttons MMC , implementation details (toolbars)"]
---

# Working with Toolbars: Implementation Details

## To add toolbars using IExtendControlBar

1.  Implement the [**IExtendControlbar**](iextendcontrolbar.md) interface and its two methods, [**SetControlBar**](iextendcontrolbar-setcontrolbar.md) and [**ControlbarNotify**](iextendcontrolbar-controlbarnotify.md).

    The snap-in's [**IComponent**](icomponent.md) implementation should implement and expose the [**IExtendControlbar**](iextendcontrolbar.md) interface.

2.  In the snap-in's implementation of [**SetControlBar**](iextendcontrolbar-setcontrolbar.md):

    -   Cache the [**IControlBar**](icontrolbar.md) interface pointer that is passed into [**SetControlBar**](iextendcontrolbar-setcontrolbar.md). Use this interface pointer to call the **IControlBar** methods.
    -   Call [**IControlBar::Create**](icontrolbar-create.md) with the *nType* parameter set to **TOOLBAR** to create a new toolbar. The *pExtendControlbar* parameter specifies the snap-in's [**IExtendControlbar**](iextendcontrolbar.md) interface associated with the control. The *ppUnknown* parameter will hold a pointer to the address of the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface of the new toolbar control. Use this pointer to call the methods of the [**IToolbar**](itoolbar.md) interface associated with the new toolbar control.
    -   Add bitmaps by calling [**IToolbar::AddBitmap**](itoolbar-addbitmap.md). Call this method only once to add all the toolbar bitmaps at one time.
    -   Fill an [**MMCBUTTON**](mmcbutton.md) structure for each toolbar button that the snap-in adds and then add the buttons by calling [**IToolbar::AddButtons**](itoolbar-addbuttons.md) to add an array of buttons or [**IToolbar::InsertButton**](itoolbar-insertbutton.md) to add a single button.

3.  In the snap-in's implementation of [**ControlbarNotify**](iextendcontrolbar-controlbarnotify.md), handle the toolbar-specific notification messages that MMC sends during calls to the **ControlbarNotify** method. There are three such notifications: [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md), [**MMCN\_SELECT**](mmcn-select.md), and [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md).

    -   The [**MMCN\_SELECT**](mmcn-select.md) notification message is sent to the snap-in's [**ControlbarNotify**](iextendcontrolbar-controlbarnotify.md) method when an item is selected or deselected in either the scope pane or result pane. The snap-in can respond to this notification by attaching its toolbar to the toolbar control (using [**IControlbar::Attach**](icontrolbar-attach.md)) during selection of an item and then detaching the toolbar (using [**IControlbar::Detach**](icontrolbar-detach.md)) during deselection of that item.
    -   The [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) notification message is sent to the snap-in's [**ControlbarNotify**](iextendcontrolbar-controlbarnotify.md) implementation when a user clicks one of the snap-in's toolbar buttons. MMC sends this notification with the same command identifier (*idCommand*) that the snap-in assigned to the button in its [**MMCBUTTON**](mmcbutton.md) structure when it added the button. The snap-in can process the command and then return **S\_OK**.

4.  Implement a mechanism for setting the attributes of the toolbar buttons using the [**IToolbar::SetButtonState**](itoolbar-setbuttonstate.md) method.

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




