---
description: The installer uses the SetProgress event to publish information on the installation's progress.
ms.assetid: be597c90-7222-4542-b0f7-e9f4cdfc08b9
title: SetProgress ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SetProgress ControlEvent

The installer uses the SetProgress event to publish information on the installation's progress. A [ProgressBar Control](progressbar-control.md) or [Billboard Control](billboard-control.md) should subscribe to the event via the [EventMapping table](eventmapping-table.md) by naming the Action whose progress is being indicated. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent can be handled by a user interface run at the [*basic UI*](b-gly.md), [*reduced UI*](r-gly.md), or [*full UI*](f-gly.md) levels. For information about UI levels, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [ProgressBar](progressbar-control.md) control on a modeless dialog box subscribes to this event using the [Progress](progress-control-attribute.md) attribute to receive the progress information.

 

 



