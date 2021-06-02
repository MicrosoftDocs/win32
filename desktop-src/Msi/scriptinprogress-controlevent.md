---
description: The installer uses this event to display an informational string while the installation's execution script is being compiled.
ms.assetid: 088e91e0-734a-4f18-8ceb-cfa4f904f75c
title: ScriptInProgress ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# ScriptInProgress ControlEvent

The installer uses this event to display an informational string while the installation's execution script is being compiled. The informational string can be displayed on a dialog box by a [Text Control](text-control.md) that subscribes to this ControlEvent. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent can be handled by a user interface run at the [*basic UI*](b-gly.md), [*reduced UI*](r-gly.md), or [*full UI*](f-gly.md) levels. For information about UI levels, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

None.

## Action on Subscribers

A [Text control](text-control.md) subscribing to ScriptInProgress will display text string specified in [UIText table](uitext-table.md).

## Typical Use

While the execution script is being compiled, the installer displays a ProgressBar indicating the time remaining before the beginning of script execution. The package author can display a preliminary message at this time explaining the ProgressBar. To display a preliminary message, include a [Text control](text-control.md) on the same modeless dialog box as the ProgressBar. Specify that this Text control subscribe to the ScriptInProgress ControlEvent via the [EventMapping table](eventmapping-table.md). Include an entry in the [UIText table](uitext-table.md) with ScriptInProgress specified in the Key field. Specify the preliminary message as a text string in the Text field of the UIText table. Then during script compilation, the installer will display this string within the text control. The displayed text disappears as soon as the script compilation is finished.

The same text control that subscribes to the ScriptInProgress ControlEvent can also subscribe to the [TimeRemaining ControlEvent](timeremaining-controlevent.md). In this case, as text of the preliminary ScriptInProgress string disappears, it is replaced by the "Time Remaining: xx minutes" string.

 

 



