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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with Toolbars: Implementation Details

## To add toolbars using IExtendControlBar

1.  Implement the [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface and its two methods, [**SetControlBar**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar?branch=master) and [**ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master).

    The snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation should implement and expose the [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface.

2.  In the snap-in's implementation of [**SetControlBar**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar?branch=master):

    -   Cache the [**IControlBar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master) interface pointer that is passed into [**SetControlBar**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-setcontrolbar?branch=master). Use this interface pointer to call the **IControlBar** methods.
    -   Call [**IControlBar::Create**](/windows/win32/Mmc/nf-mmc-icontrolbar-create?branch=master) with the *nType* parameter set to **TOOLBAR** to create a new toolbar. The *pExtendControlbar* parameter specifies the snap-in's [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface associated with the control. The *ppUnknown* parameter will hold a pointer to the address of the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface of the new toolbar control. Use this pointer to call the methods of the [**IToolbar**](/windows/win32/Mmc/nn-mmc-itoolbar?branch=master) interface associated with the new toolbar control.
    -   Add bitmaps by calling [**IToolbar::AddBitmap**](/windows/win32/Mmc/nf-mmc-itoolbar-addbitmap?branch=master). Call this method only once to add all the toolbar bitmaps at one time.
    -   Fill an [**MMCBUTTON**](/windows/win32/Mmc/ns-mmc-_mmcbutton?branch=master) structure for each toolbar button that the snap-in adds and then add the buttons by calling [**IToolbar::AddButtons**](/windows/win32/Mmc/nf-mmc-itoolbar-addbuttons?branch=master) to add an array of buttons or [**IToolbar::InsertButton**](/windows/win32/Mmc/nf-mmc-itoolbar-insertbutton?branch=master) to add a single button.

3.  In the snap-in's implementation of [**ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), handle the toolbar-specific notification messages that MMC sends during calls to the **ControlbarNotify** method. There are three such notifications: [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md), [**MMCN\_SELECT**](mmcn-select.md), and [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md).

    -   The [**MMCN\_SELECT**](mmcn-select.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) method when an item is selected or deselected in either the scope pane or result pane. The snap-in can respond to this notification by attaching its toolbar to the toolbar control (using [**IControlbar::Attach**](/windows/win32/Mmc/nf-mmc-icontrolbar-attach?branch=master)) during selection of an item and then detaching the toolbar (using [**IControlbar::Detach**](/windows/win32/Mmc/nf-mmc-icontrolbar-detach?branch=master)) during deselection of that item.
    -   The [**MMCN\_BTN\_CLICK**](mmcn-btn-click.md) notification message is sent to the snap-in's [**ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) implementation when a user clicks one of the snap-in's toolbar buttons. MMC sends this notification with the same command identifier (*idCommand*) that the snap-in assigned to the button in its [**MMCBUTTON**](/windows/win32/Mmc/ns-mmc-_mmcbutton?branch=master) structure when it added the button. The snap-in can process the command and then return **S\_OK**.

4.  Implement a mechanism for setting the attributes of the toolbar buttons using the [**IToolbar::SetButtonState**](/windows/win32/Mmc/nf-mmc-itoolbar-setbuttonstate?branch=master) method.

## Related topics

<dl> <dt>

[Working with Toolbars and Menu Buttons: Interfaces](working-with-toolbars-and-menu-buttons-interfaces.md)
</dt> <dt>

[Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
</dt> </dl>

 

 




