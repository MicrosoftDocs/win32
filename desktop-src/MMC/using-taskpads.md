---
title: Using Taskpads
description: This section discusses how to implement snap-in taskpads. For more information and an overview of taskpads, see Using Different Result Pane View Types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ef0fdca7-f52e-48b9-98a1-d4516c9089d4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- taskpads MMC
- taskpads MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Taskpads

This section discusses how to implement snap-in taskpads. For more information and an overview of taskpads, see [Using Different Result Pane View Types](using-different-result-pane-view-types.md).

Snap-in taskpads are introduced in MMC 1.1. In MMC 1.2, use [console taskpads](console-taskpads.md) rather than snap-in taskpads. This section discusses how to implement snap-in taskpads in snap-ins that must be backward compatible. Be aware that in the discussion the term "taskpad" is used in place of "snap-in taskpad."

The MMC SDK specifies a number of interfaces and other constructs for working with taskpads. MMC calls the snap-in's implementation of [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master) to display the result pane for a particular scope item. The snap-in uses the method to provide MMC with the address of a string that contains the resource path to the taskpad template or HTML file and a group name that identifies the taskpad.

The [**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master) interface enables the snap-in to set up a taskpad and receive notifications from the taskpad. When the taskpad DHTML page is loaded, the [**MMCCtrl**](mmcctrl-control.md) control on that page calls methods in MMC. In turn, MMC attempts to get the **IExtendTaskPad** interface from the [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) object and calls the methods required to provide the MMCCtrl control with the data required to render the taskpad's general elements: title text, banner image, and background image.

If the taskpad is a list view taskpad, MMC calls [**IExtendTaskPad::GetListPadInfo**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo?branch=master) to get the title text for the list control, text for an optional button, and the command ID passed to [**IExtendTaskPad::TaskNotify**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-tasknotify?branch=master) when the button is clicked.

MMC calls the [**IExtendTaskPad::EnumTasks**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-enumtasks?branch=master) method to get a pointer to the [**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master) interface of an object that specifies the tasks the snap-in must add to the taskpad.

The [**IEnumTASK::Next**](/windows/win32/Mmc/nf-mmc-ienumtask-next?branch=master) method enables MMC to retrieve the next task in the snap-in's list of tasks. MMC calls this method until it returns **S\_FALSE** to indicate there are no more tasks for the snap-in to add to the taskpad. The [**IEnumTASK::Reset**](/windows/win32/Mmc/nf-mmc-ienumtask-reset?branch=master) method enables MMC to reset the enumeration to the beginning of the snap-in's task list.

MMC calls the [**IExtendTaskPad::TaskNotify**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-tasknotify?branch=master) method to notify the snap-in when the user clicks a task or a list view button. The list view button applies only to list view taskpads.

The [**IEnumTASK::Skip**](/windows/win32/Mmc/nf-mmc-ienumtask-skip?branch=master) and [**IEnumTASK::Clone**](/windows/win32/Mmc/nf-mmc-ienumtask-clone?branch=master) methods are included in the MMC SDK for completeness, but are not used by MMC. Snap-ins can simply return E\_NOTIMPL in their implementation of these two methods.

 

 




