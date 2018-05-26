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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Taskpads: Interfaces

Taskpads require the implementation of the following interfaces and methods:

-   [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master)
    -   [**IComponent::GetResultViewType**](/windows/win32/Mmc/nf-mmc-icomponent-getresultviewtype?branch=master)
-   [**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master)
    -   [**IExtendTaskPad::EnumTasks**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-enumtasks?branch=master)
    -   [**IExtendTaskPad::GetBackground**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getbackground?branch=master)
    -   [**IExtendTaskPad::GetDescriptiveText**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getdescriptivetext?branch=master)
    -   [**IExtendTaskPad::GetListPadInfo**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo?branch=master)
    -   [**IExtendTaskPad::GetTitle**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-gettitle?branch=master)
    -   [**IExtendTaskPad::TaskNotify**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-tasknotify?branch=master)
-   [**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master)
    -   [**IEnumTASK::Next**](/windows/win32/Mmc/nf-mmc-ienumtask-next?branch=master)
    -   [**IEnumTASK::Reset**](/windows/win32/Mmc/nf-mmc-ienumtask-reset?branch=master)

## Other Constructs

Taskpads use the following structures:

-   [**MMC\_LISTPAD\_INFO**](/windows/win32/Mmc/ns-mmc-_mmc_listpad_info?branch=master)
-   [**MMC\_TASK**](/windows/win32/Mmc/ne-mmc-_mmc_task_display_type?branch=master)
-   [**MMC\_TASK\_DISPLAY\_BITMAP**](/windows/win32/Mmc/ns-mmc-_mmc_task_display_bitmap?branch=master)
-   [**MMC\_TASK\_DISPLAY\_OBJECT**](/windows/win32/Mmc/ns-mmc-_mmc_task_display_object?branch=master)
-   [**MMC\_TASK\_DISPLAY\_SYMBOL**](/windows/win32/Mmc/ns-mmc-_mmc_task_display_symbol?branch=master)

Taskpads use the following enumerated types:

-   [**MMC\_ACTION\_TYPE**](/windows/win32/Mmc/ne-mmc-_mmc_action_type?branch=master)
-   [**MMC\_TASK\_DISPLAY\_TYPE**](/windows/win32/Mmc/ne-mmc-_mmc_task_display_type?branch=master)

Taskpads use the following notification:

-   [**MMCN\_LISTPAD**](mmcn-listpad.md)

## MMC Taskpad Controls and Objects

MMC has the following ActiveX® controls that are used on taskpad HTML pages:

<dl> <dt>

<span id="ListPad_control"></span><span id="listpad_control"></span><span id="LISTPAD_CONTROL"></span>[ListPad control](listpad-control.md)
</dt> <dd>

Displays a list-view control that contains items from an [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) result list. Used on list view taskpads only.

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

 

 




