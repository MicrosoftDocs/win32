---
description: Windows Installer contains functionality to display a progress indicator in an action display dialog.
ms.assetid: cfc2d974-4f2d-4f52-9835-eab1dc091c9b
title: Authoring a ProgressBar Control
ms.topic: article
ms.date: 05/31/2018
---

# Authoring a ProgressBar Control

Windows Installer contains functionality to display a progress indicator in an action display dialog. The [ProgressBar control](progressbar-control.md) graphically represents the installation of individual components and reports either the total time elapsed relative to time remaining or the approximate total time remaining until the installation is complete.

To determine the total time anticipated for the installation, the installer tracks the total progress ticks anticipated by each action during generation of the execution script. When script generation is complete, the progress tick total is stored and the installation begins.

Progress messages detailing the elapsed number of progress ticks are sent to the active message handler as each action in the script is executed. On each progress message, the installer broadcasts a [SetProgress ControlEvent](setprogress-controlevent.md) to the currently active dialog box. The UI sequence should be authored to create the action display dialog box during script execution to receive the SetProgress ControlEvent messages from the installer.

When the action display dialog box receives a SetProgress ControlEvent, it checks the [EventMapping table](eventmapping-table.md) for any controls subscribing to the ControlEvent. The ProgressBar control on the action display dialog box is subscribed to with the Progress control attribute specified in the Attributes column. The Progress Control attribute specifies that the ProgressBar control will be passed "ticksSoFar" and "totalTicks" values along with the SetProgress ControlEvent. The progress bar control uses this information to advance the graphical bar from left to right for an installation and from right to left for a [rollback](rollback-installation.md) operation.

In addition, the installer broadcasts a [TimeRemaining ControlEvent](timeremaining-controlevent.md) on each progress message. The total time remaining for the installation is determined by first calculating the execution rate, which is the total number of ticks elapsed divided by the total time since the installation began. The total ticks remaining divided by the execution rate gives the approximate time remaining.

When the action display dialog box receives the TimeRemaining ControlEvent, it again looks in the EventMapping table for any controls that are subscribed. In order to display the time remaining, a [Text control](text-control.md) must be subscribed to the TimeRemaining ControlEvent with the [TimeRemaining control attribute](timeremaining-control-attribute.md) specified in the Attributes column.

The subscribed Text control queries the [UIText table](uitext-table.md) for a parameterized template string named "TimeRemaining". This string has two parameters, \[1\] for minutes, and \[2\] for seconds. The Text control converts each value to minutes and seconds, evaluates the TimeRemaining template string, and updates the text control with the new information.

If the UI display level is set to basic or lower, the installer displays a default dialog box containing a progress bar and TimeRemaining text field. For more information, see [User Interface Levels](user-interface-levels.md).

 

 



