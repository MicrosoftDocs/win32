---
title: Using Custom OCX Controls
description: This section covers how you can add functionality to your snap-in that enables it to launch a custom OCX control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6ae5910-30f7-467d-94db-c52d9e7a5e74
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- custom OCX controls MMC
- custom OCX controls MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Custom OCX Controls

This section covers how you can add functionality to your snap-in that enables it to launch a custom OCX control.

A snap-in can launch an OCX control in the result pane of an MMC console. The OCX control runs in the same thread as the snap-in, so snap-in developers only need to deal with threading issues if their OCX controls are multithreaded.

Be aware that custom OCX controls should be used sparingly, because they cannot be extended by other snap-ins. Additionally, MMC will not send Cut, Copy, Paste, or Rename notifications to OCX controls. Snap-ins should instead use list views where possible.

The MMC SDK specifies two interface methods and a number of other constructs for working with custom OCX controls. MMC calls the snap-in's implementation of [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) to display the result pane for a particular scope item. The snap-in uses the method to indicate to MMC that an OCX view should be launched and provides MMC with the CLSID of the OCX control. The snap-in can also specify whether a single instance of the OCX control should be cached and reused each time the scope item is selected, or whether MMC should instead destroy the cached OCX control and create a new custom control each time the item is selected. This is done using the MMC\_VIEW\_OPTIONS\_CREATENEW option.

The second method, [**IConsole2::QueryResultView**](iconsole2-queryresultview.md), can be used to query for the OCX control's [**IUnknown**](_com_iunknown) interface pointer. The snap-in can also acquire this pointer in a number of other ways, for example while handling the [**MMCN\_INITOCX**](mmcn-initocx.md) notification message.

MMC sends the snap-in an [**MMCN\_INITOCX**](mmcn-initocx.md) notification message with an interface pointer to the custom OCX control's **IUnknown** interface. The snap-in can use the pointer to perform any initialization of the OCX control before it is displayed in the result pane.

MMC sends the snap-in an [**MMCN\_SHOW**](mmcn-show.md) notification upon deselection of the result pane with the OCX view. The *arg* parameter of the notification is set to **FALSE**, indicating that the OCX view is going out of focus. At this time, the snap-in can do any necessary clean-up, such as ensuring that the OCX control is properly destroyed.

## Related topics

<dl> <dt>

[Using Custom OCX Controls: Interfaces](using-custom-ocx-controls-interfaces.md)
</dt> <dt>

[Using Custom OCX Controls: Implementation Details](using-custom-ocx-controls-implementation-details.md)
</dt> <dt>

[Using the MMC Message OCX Control](using-the-mmc-message-ocx-control.md)
</dt> </dl>

 

 




