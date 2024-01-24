---
description: The SpawnWaitDialog ControlEvent triggers the dialog box specified by the Argument column of the ControlEvent table, if the expression in the Condition column evaluates as FALSE.
ms.assetid: 38a5d896-2c11-4ce9-b829-104a882723b6
title: SpawnWaitDialog ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SpawnWaitDialog ControlEvent

The SpawnWaitDialog ControlEvent triggers the dialog box specified by the Argument column of the [ControlEvent table](controlevent-table.md), if the expression in the Condition column evaluates as FALSE. The dialog box remains up for as long as the conditional expression remains FALSE and is removed as soon as the condition evaluates TRUE.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A dialog box in the [Dialog table](dialog-table.md).

## Action on Subscribers

None.

## Typical Use

The SpawnWaitDialog ControlEvent can be used to wait for any background task the completion of which can be tested using a conditional expression such as the state of a property. For an example of using the SpawnWaitDialog ControlEvent, see the section [Authoring a Conditional "Please wait . . ." Message Box](authoring-a-conditional-please-wait-------message-box.md).

 

 



