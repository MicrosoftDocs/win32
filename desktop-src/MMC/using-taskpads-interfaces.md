---
title: Using Taskpads Interfaces
description: Taskpads require the implementation of the following interfaces and methods
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f9b9101d-f0ed-4e9d-ab7f-cba038a86ecd
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- taskpads MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Taskpads: Interfaces

Taskpads require the implementation of the following interfaces and methods:

-   [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent)
    -   [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype)
-   [**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad)
    -   [**IExtendTaskPad::EnumTasks**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-enumtasks)
    -   [**IExtendTaskPad::GetBackground**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-getbackground)
    -   [**IExtendTaskPad::GetDescriptiveText**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-getdescriptivetext)
    -   [**IExtendTaskPad::GetListPadInfo**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo)
    -   [**IExtendTaskPad::GetTitle**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-gettitle)
    -   [**IExtendTaskPad::TaskNotify**](/windows/desktop/api/Mmc/nf-mmc-iextendtaskpad-tasknotify)
-   [**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask)
    -   [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next)
    -   [**IEnumTASK::Reset**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-reset)

## Other Constructs

Taskpads use the following structures:

-   [**MMC\_LISTPAD\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_mmc_listpad_info)
-   [**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type)
-   [**MMC\_TASK\_DISPLAY\_BITMAP**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_bitmap)
-   [**MMC\_TASK\_DISPLAY\_OBJECT**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_object)
-   [**MMC\_TASK\_DISPLAY\_SYMBOL**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_symbol)

Taskpads use the following enumerated types:

-   [**MMC\_ACTION\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_action_type)
-   [**MMC\_TASK\_DISPLAY\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type)

Taskpads use the following notification:

-   [**MMCN\_LISTPAD**](mmcn-listpad.md)

## MMC Taskpad Controls and Objects

MMC has the following ActiveX® controls that are used on taskpad HTML pages:

<dl> <dt>

<span id="ListPad_control"></span><span id="listpad_control"></span><span id="LISTPAD_CONTROL"></span>[ListPad control](listpad-control.md)
</dt> <dd>

Displays a list-view control that contains items from an [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata) result list. Used on list view taskpads only.

</dd> <dt>

<span id="MMCCtrl_control"></span><span id="mmcctrl_control"></span><span id="MMCCTRL_CONTROL"></span>[**MMCCtrl control**](mmcctrl-control.md)
</dt> <dd>

Gets the taskpad configuration information (text, graphics, tasks) from the snap-in and communicates data back to the snap-in.

</dd> <dt>

<span id="SysColorCtrl_control"></span><span id="syscolorctrl_control"></span><span id="SYSCOLORCTRL_CONTROL"></span>[**SysColorCtrl control**](syscolorctrl-control.md)
</dt> <dd>

Is used on a taskpad DHTML page to get system color settings that can be applied to the taskpad. The control also has methods to derive colors based on one or more specified colors.

</dd> </dl>

Taskpads also use the following objects (which are created by methods in the [**MMCCtrl control**](mmcctrl-control.md)):

<dl> <dt>

<span id="MMCDisplayObject_object"></span><span id="mmcdisplayobject_object"></span><span id="MMCDISPLAYOBJECT_OBJECT"></span>[**MMCDisplayObject object**](mmcdisplayobject-object.md)
</dt> <dd>

A value that specifies the type of image and all the data required to use that image to display a task or the background on a taskpad.

</dd> <dt>

<span id="MMCListPadInfo_object"></span><span id="mmclistpadinfo_object"></span><span id="MMCLISTPADINFO_OBJECT"></span>[**MMCListPadInfo object**](mmclistpadinfo-object.md)
</dt> <dd>

Represents a label and a button for the **ListPad** control to be added to the taskpad page. Should be used on list view taskpads only.

</dd> <dt>

<span id="MMCTask_object"></span><span id="mmctask_object"></span><span id="MMCTASK_OBJECT"></span>[**MMCTask object**](mmctask-object.md)
</dt> <dd>

Represents a task to be added to the taskpad.

</dd> </dl>

## Related topics

<dl> <dt>

[Using Taskpads: Implementation Details](using-taskpads-implementation-details.md)
</dt> </dl>

 

 




