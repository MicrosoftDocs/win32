---
description: ControlEvents are analogous to Microsoft Windows messages in Win32-based applications.
ms.assetid: ac62bb94-0605-4145-996a-e91fb1a42a77
title: ControlEvent Overview
ms.topic: article
ms.date: 05/31/2018
---

# ControlEvent Overview

ControlEvents are analogous to Microsoft Windows messages in Win32-based applications. However, rather than creating a callback function to receive Windows messages and sending Windows messages with the [SendMessage](/windows/win32/api/winuser/nf-winuser-sendmessage) function, the user interface (UI) installer and controls publish [ControlEvents](control-events.md). Other controls and the installer can be specified to subscribe to particular ControlEvents that will then change attributes of the subscribing control. To add working controls to dialog boxes, the author of the UI specifies the publication of ControlEvents in the [ControlEvent table](controlevent-table.md) and subscribes controls to ControlEvents in the [EventMapping table](eventmapping-table.md).

The installer will publish the following events to subscribing controls listed in the [EventMapping table](eventmapping-table.md). A [ProgressBar control](progressbar-control.md) or [Billboard control](billboard-control.md) typically subscribes to SetProgress, the rest are subscribed to by [Text controls](text-control.md).

[ActionData ControlEvent](actiondata-controlevent.md)

[ActionText ControlEvent](actiontext-controlevent.md)

[SetProgress ControlEvent](setprogress-controlevent.md)

[TimeRemaining ControlEvent](timeremaining-controlevent.md)

[ScriptInProgress ControlEvent](scriptinprogress-controlevent.md)

The following events are published by the control when the item selection is moved in a [SelectionTree control](selectiontree-control.md) or [DirectoryList Control](directorylist-control.md). Subscribing controls must be located on the same dialog box and listed in the EventMapping table.

[IgnoreChange ControlEvent](ignorechange-controlevent.md)

[SelectionDescription ControlEvent](selectiondescription-controlevent.md)

[SelectionSize ControlEvent](selectionsize-controlevent.md)

[SelectionPath ControlEvent](selectionpath-controlevent.md)

[SelectionAction ControlEvent](selectionaction-controlevent.md)

[SelectionNoItems ControlEvent](selectionnoitems-controlevent.md)

The following ControlEvents can be published at the discretion of a user by interacting with a [PushButton control](pushbutton-control.md) or [CheckBox control](checkbox-control.md) on a dialog box. The Checkbox control can only publish the AddLocal, AddSource, Remove, DoAction, and SetProperty events. With Windows Installer versions that shipped with Windows Server 2003 and later, the [SelectionTree control](selectiontree-control.md) can publish the DoAction, ControlEvent and SetProperty ControlEvents. The author of the UI should list the ControlEvent in the [ControlEvent table](controlevent-table.md). The UI handler of the installer is the subscriber to these events.

[AddLocal ControlEvent](addlocal-controlevent.md)

[AddSource ControlEvent](addsource-controlevent.md)

[CheckExistingTargetPath ControlEvent](checkexistingtargetpath-controlevent.md)

[CheckTargetPath ControlEvent](checktargetpath-controlevent.md)

[DoAction ControlEvent](doaction-controlevent.md)

[EnableRollback ControlEvent](enablerollback-controlevent.md)

[EndDialog ControlEvent](enddialog-controlevent.md)

[NewDialog ControlEvent](newdialog-controlevent.md)

[Reinstall ControlEvent](reinstall-controlevent.md)

[ReinstallMode ControlEvent](reinstallmode-controlevent.md)

[Remove ControlEvent](remove-controlevent.md)

[Reset ControlEvent](reset-controlevent.md)

[SetInstallLevel ControlEvent](setinstalllevel-controlevent.md)

[SetProperty ControlEvent](setproperty-controlevent.md)

[SetTargetPath ControlEvent](settargetpath-controlevent.md)

[SpawnDialog ControlEvent](spawndialog-controlevent.md)

[SpawnWaitDialog ControlEvent](spawnwaitdialog-controlevent.md)

[ValidateProductID ControlEvent](validateproductid-controlevent.md)

A [PushButton control](pushbutton-control.md) can publish the following events to a subscribing [SelectionTree control](selectiontree-control.md) or [DirectoryList control](directorylist-control.md) located in the same dialog box. The PushButton Control should be listed in the ControlEvent table and the subscribing controls should be listed in the EventMapping table.

[SelectionBrowse ControlEvent](selectionbrowse-controlevent.md)

[DirectoryListUp ControlEvent](directorylistup-controlevent.md)

[DirectoryListNew ControlEvent](directorylistnew-controlevent.md)

[DirectoryListOpen ControlEvent](directorylistopen-controlevent.md)

Control events generally require that the UI be run at the [*full UI*](f-gly.md) level. Most ControlEvents will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md) because these levels only display modeless dialog boxes. The ActionText, AddSource, SetProgress, TimeRemaining, and ScriptInProgress events are exceptions and will work in reduced or basic UI. For more information about UI levels, see [User Interface Levels](user-interface-levels.md).

You can run [custom actions](custom-actions.md) by publishing a ControlEvent from a [PushButton control](pushbutton-control.md) or [Checkbox control](checkbox-control.md). Add a record to the [ControlEvent table](controlevent-table.md) with the names of the dialog and the control publishing the ControlEvent. This control should publish a [DoAction ControlEvent](doaction-controlevent.md) notifying the installer to run the custom action. On Windows XP or earlier systems, you cannot run a custom action by publishing a ControlEvent from a [SelectionTree control](selectiontree-control.md).

For a more information about particular ControlEvents, see the list of standard [ControlEvents](control-events.md) in [User Interface Reference](user-interface-reference.md).

 

 
