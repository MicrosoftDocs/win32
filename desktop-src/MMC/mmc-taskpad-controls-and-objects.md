---
title: MMC 2.0 Taskpad Controls and Objects
description: MMC taskpad controls and objects are introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c27f58d4-02bb-4aba-a3f9-e8f72fbc6eb1
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- taskpad controls and objects MMC 2.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC 2.0 Taskpad Controls and Objects

MMC taskpad controls and objects are introduced in MMC 1.1.

MMC has the following ActiveX controls that are used on taskpad HTML pages.

<dl> <dt>

<span id="ListPad_control"></span><span id="listpad_control"></span><span id="LISTPAD_CONTROL"></span>[ListPad control](listpad-control.md)
</dt> <dd>

Displays a list-view control that contains items from an IResultData result list. Used on list view taskpads only.

</dd> <dt>

<span id="MMCCtrl_control"></span><span id="mmcctrl_control"></span><span id="MMCCTRL_CONTROL"></span>[**MMCCtrl control**](mmcctrl-control.md)
</dt> <dd>

Gets the taskpad configuration information (text, graphics, and tasks) from the snap-in and communicates data back to the snap-in.

</dd> <dt>

<span id="SysColorCtrl_control"></span><span id="syscolorctrl_control"></span><span id="SYSCOLORCTRL_CONTROL"></span>[**SysColorCtrl control**](syscolorctrl-control.md)
</dt> <dd>

Gets system color settings, used on a taskpad DHTML page, that can be applied to the taskpad. The control also has methods to derive colors based one or more specified colors.

</dd> </dl>

Taskpads also use the following objects (created by methods in the MMCCtrl control).

<dl> <dt>

<span id="MMCDisplayObject_object"></span><span id="mmcdisplayobject_object"></span><span id="MMCDISPLAYOBJECT_OBJECT"></span>[**MMCDisplayObject object**](mmcdisplayobject-object.md)
</dt> <dd>

Specifies the type of image and all the data required to use that image to display a task or the background on a taskpad.

</dd> <dt>

<span id="MMCListPadInfo_object"></span><span id="mmclistpadinfo_object"></span><span id="MMCLISTPADINFO_OBJECT"></span>[**MMCListPadInfo object**](mmclistpadinfo-object.md)
</dt> <dd>

Represents a label and a button for the ListPad control to be added to the taskpad page. Should be used on list view taskpads only.

</dd> <dt>

<span id="MMCTask_object"></span><span id="mmctask_object"></span><span id="MMCTASK_OBJECT"></span>[**MMCTask object**](mmctask-object.md)
</dt> <dd>

Represents a task to be added to the taskpad.

</dd> </dl>

 

 




