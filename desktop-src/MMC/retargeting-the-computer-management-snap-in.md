---
title: Retargeting the Computer Management Snap-in
description: The Computer Management snap-in can be retargeted by the user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aebc08ae-6a89-4370-b31c-9e88ba172a40
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Retargeting the Computer Management Snap-in

The Computer Management snap-in can be retargeted by the user. Accordingly, Computer Management snap-in extensions must recognize when the Computer Management snap-in is retargeted. Specifically, a namespace extension will receive the [**MMCN\_EXPAND**](mmcn-expand.md) notification when the extended node is expanded, and the [**MMCN\_REMOVE\_CHILDREN**](mmcn-remove-children.md) notification when the computer is retargeted. The following scenario provides details of what happens when a user starts the Computer Management snap-in and then retargets the managed computer. Although the scenario assumes your extension extends the System Tools scope node, the behavior is identical for extensions extending the Services and Applications or Storage scope nodes.

1.  The user starts the Computer Management snap-in, initially targeted at the local computer.
2.  The user then expands the Computer Management console root node. The Computer Management snap-in creates the System Tools scope item, targeted at the local computer.
3.  The user expands the System Tools scope item.

    Because there is currently no instance of your extension snap-in under the Computer Management console root node, MMC creates an instance of your extension. MMC then uses the CLSID of your extension to associate the extension instance with the console root node.

4.  Your extension's [**IComponentData::Notify**](icomponentdata-notify.md) method receives an [**MMCN\_EXPAND**](mmcn-expand.md) notification.

    The [**MMCN\_EXPAND**](mmcn-expand.md) notification includes the data object for the System Tools scope item. Using the data object, your extension calls the IDataObject::GetDataHere method to retrieve the [**MMC\_SNAPIN\_MACHINE\_NAME**](mmc-snapin-machine-name.md) clipboard format. The MMC\_SNAPIN\_MACHINE\_NAME clipboard format provides the machine name of the targeted computer. Your extension should store the machine name with your child scope items.

5.  The user retargets the Computer Management snap-in to another computer.

    The Computer Management snap-in deletes the System Tools scope item.

6.  Your extension's IComponentData::Notify method receives an [**MMCN\_REMOVE\_CHILDREN**](mmcn-remove-children.md) notification. Your extension should destroy all resources for the subtree that your extension added under the System Tools scope item.

    MMC removes the items from the scope pane, so your snap-in is not required to call [**IConsoleNameSpace2::DeleteItem**](iconsolenamespace2-deleteitem.md). Be aware that your [**IComponentData**](icomponentdata.md) instance is not released — MMC uses this instance for the lifetime of the Computer Management console root node.

7.  MMC creates a new System Tools scope item, targeted at the new computer.

    When the user expands the System Tools scope item, your snap-in's IComponentData::Notify method receives another [**MMCN\_EXPAND**](mmcn-expand.md) notification message. As in Step 4, your extension requests the MMC\_SNAPIN\_MACHINE\_NAME clipboard format, and your snap-in should store the machine name with your child scope items.

The scenario listed above uses the local computer as the initial target; the notifications would be the same if a remote computer was the initial target. Other types of Computer Management extensions, such as context menu extensions or property page extensions, should also associate the machine name with the IComponentData interface.

 

 




