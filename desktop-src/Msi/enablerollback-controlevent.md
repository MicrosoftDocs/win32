---
Description: This ControlEvent can be used to turn on or turn off the installers rollback capabilities.
ms.assetid: 5279151c-a7cd-4f66-8d1b-d688b3b1cf82
title: EnableRollback ControlEvent
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EnableRollback ControlEvent

This ControlEvent can be used to turn on or turn off the installer's rollback capabilities.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md#-msi-full-ui-gly) level. This event will not work with a [*reduced UI*](r-gly.md#-msi-reduced-ui-gly) or [*basic UI*](b-gly.md#-msi-basic-ui-gly). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

False turns off the installer's rollback capabilities. True turns on the installer's rollback capabilities.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

Can be used to turn off rollback capabilities if the installer detects that there is insufficient disk space available to complete the installation. For this case, the ControlEvent should be used with the [**OutOfDiskSpace**](outofdiskspace.md), [**OutOfNoRbDiskSpace**](outofnorbdiskspace.md), and the [**PROMPTROLLBACKCOST**](promptrollbackcost.md) properties.

 

 



