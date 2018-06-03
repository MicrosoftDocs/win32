---
title: Working with Toolbars Implementation Details
description: Working with Toolbars Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53ad9866-0dd1-469c-acec-0277546c14e7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- toolbars and menu buttons MMC , implementation details (toolbars)
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with Toolbars: Implementation Details

## To add toolbars using IExtendControlBar

1.  Implement the [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface and its two methods, [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar) and [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify).

    The snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation should implement and expose the [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface.

2.  In the snap-in's implementation of [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar):

    -   Cache the [**IControlBar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar) interface pointer that is passed into [**SetControlBar**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar). Use this interface pointer to call the **IControlBar** methods.
    -   Call [**IControlBar::Create**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-create) with the *nType* parameter set to **TOOLBAR** to create a new toolbar. The *pExtendControlbar* parameter specifies the snap-in's [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) interface associated with the control. The *ppUnknown* parameter will hold a pointer to the address of the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface of the new toolbar control. Use this pointer to call the methods of the [**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar) interface associated with the new toolbar control.
    -   Add bitmaps by calling [**IToolbar::AddBitmap**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbitmap). Call this method only once to add all the toolbar bitmaps at one time.
    -   Fill an [**MMCBUTTON**](/windows/desktop/api/Mmc/ns-mmc-_mmcbutton) structure for each toolbar button that the snap-in adds and then add the buttons by calling [**IToolbar::AddButtons**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbuttons) to add an array of buttons or [**IToolbar::InsertButton**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-insertbutton) to add a single button.

3.  In the snap-in's implementation of [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify), handle the toolbar-specific notification messages that MMC sends during calls to the **ControlbarNotify** method. There are three such notifications: [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md), [**MMCN\_SELECT**](mmcn-select.md), and [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md).

    -   The [**MMCN\_SELECT**](mmcn-select.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) method when an item is selected or deselected in either the scope pane or result pane. The snap-in can respond to this notification by attaching its toolbar to the toolbar control (using [**IControlbar::Attach**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-attach)) during selection of an item and then detaching the toolbar (using [**IControlbar::Detach**](/windows/desktop/api/Mmc/nf-mmc-icontrolbar-detach)) during deselection of that item.
    -   The [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify) implementation when a user clicks one of the snap-in's toolbar buttons. MMC sends this notification with the same command identifier (*idCommand*) that the snap-in assigned to the button in its [**MMCBUTTON**](/windows/desktop/api/Mmc/ns-mmc-_mmcbutton) structure when it added the button. The snap-in can process the command and then return **S\_OK**.

4.  Implement a mechanism for setting the attributes of the toolbar buttons using the [**IToolbar::SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-setbuttonstate) method.

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




