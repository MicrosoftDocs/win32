---
description: A ControlEvent specifies an action to be taken by the installer or a change in the attributes of one or more controls in a dialog box. For more information about ControlEvents, see ControlEvent Overview.
ms.assetid: 8768acaa-884b-428f-a14e-3f39f8ea4ad5
title: Control Events (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Control Events (Windows Installer)

A ControlEvent specifies an action to be taken by the installer or a change in the attributes of one or more controls in a dialog box. For more information about ControlEvents, see [ControlEvent Overview](controlevent-overview.md).

The following table provides links to more information about particular ControlEvents.



| Control event                                                       | Brief description of ControlEvent                                                                                                                                                                             |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionData](actiondata-controlevent.md)                           | Publishes data on the latest action.                                                                                                                                                                          |
| [ActionText](actiontext-controlevent.md)                           | Publishes the name of the present action.                                                                                                                                                                     |
| [AddLocal](addlocal-controlevent.md)                               | Notifies the installer to run features locally.                                                                                                                                                               |
| [AddSource](addsource-controlevent.md)                             | Notifies the installer to run features from their source.                                                                                                                                                     |
| [CheckExistingTargetPath](checkexistingtargetpath-controlevent.md) | Notifies the installer to verify that the path can be written.                                                                                                                                                |
| [CheckTargetPath](checktargetpath-controlevent.md)                 | Notifies the installer to verify that the path is valid.                                                                                                                                                      |
| [DirectoryListNew](directorylistnew-controlevent.md)               | Notifies the DirectoryList control to create a new folder.                                                                                                                                                    |
| [DirectoryListOpen](directorylistopen-controlevent.md)             | Selects the directory in the DirectoryList control.                                                                                                                                                           |
| [DirectoryListUp](directorylistup-controlevent.md)                 | Notifies the DirectoryList control to select the parent of the present directory.                                                                                                                             |
| [DoAction](doaction-controlevent.md)                               | Dialog box notifies the installer to execute a custom action.                                                                                                                                                 |
| [EnableRollback](enablerollback-controlevent.md)                   | Used to turn rollback capabilities off and on.                                                                                                                                                                |
| [EndDialog](enddialog-controlevent.md)                             | Notifies the installer to remove a modal dialog box.                                                                                                                                                          |
| [IgnoreChange](ignorechange-controlevent.md)                       | Published by the DirectoryList control when a folder is highlighted but not opened.                                                                                                                           |
| [MsiLaunchApp](msilaunchapp-controlevent.md)                       | This control event runs a specified file.**[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/>                                                       |
| [MsiPrint](msiprint-controlevent.md)                               | Enables the user to print the contents of [ScrollableText Control](scrollabletext-control.md).**[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** Not supported.<br/> |
| [NewDialog](newdialog-controlevent.md)                             | Notifies the installer to change a modal dialog box into another dialog box.                                                                                                                                  |
| [Reinstall](reinstall-controlevent.md)                             | Initiates a reinstallation of features.                                                                                                                                                                       |
| [ReinstallMode](reinstallmode-controlevent.md)                     | Specifies the validation mode during a reinstallation.                                                                                                                                                        |
| [Remove](remove-controlevent.md)                                   | Notifies the installer when features are selected for removal.                                                                                                                                                |
| [Reset](reset-controlevent.md)                                     | Resets all the property values to the default values used when the dialog box was created.                                                                                                                    |
| [RmShutdownAndRestart](rmshutdownandrestart-controlevent.md)       | Use the [Restart Manager](/windows/desktop/RstMgr/restart-manager-portal) to shutdown all applications that have files in use and to restart them at the end of the installation.                                                              |
| [ScriptInProgress](scriptinprogress-controlevent.md)               | Displays a string while the execution script is compiled.                                                                                                                                                     |
| [SelectionAction](selectionaction-controlevent.md)                 | Published by SelectionTree to describe an item.                                                                                                                                                               |
| [SelectionBrowse](selectionbrowse-controlevent.md)                 | Published by SelectionTree to spawn a dialog box.                                                                                                                                                             |
| [SelectionDescription](selectiondescription-controlevent.md)       | Published by SelectionTree to provide a string in the Description field of the Feature Table.                                                                                                                 |
| [SelectionNoItems](selectionnoitems-controlevent.md)               | Used by SelectionTree to delete text or disable buttons.                                                                                                                                                      |
| [SelectionPath](selectionpath-controlevent.md)                     | Published by SelectionTree to provide the path of an item.                                                                                                                                                    |
| [SelectionPathOn](selectionpathon-controlevent.md)                 | Published by SelectionTree to indicate whether there is a path associated with a feature.                                                                                                                     |
| [SelectionSize](selectionsize-controlevent.md)                     | Published by SelectionTree control to provide the size of an item.                                                                                                                                            |
| [SetInstallLevel](setinstalllevel-controlevent.md)                 | The installer changes installation level to a specified value.                                                                                                                                                |
| [SetProgress](setprogress-controlevent.md)                         | Published by the installer to provide installation progress.                                                                                                                                                  |
| [SetProperty](setproperty-controlevent.md)                         | Sets a specified property.                                                                                                                                                                                    |
| [SetTargetPath](settargetpath-controlevent.md)                     | Notifies the installer to check and set a path.                                                                                                                                                               |
| [SpawnDialog](spawndialog-controlevent.md)                         | Notifies the installer to create a child of a modal box.                                                                                                                                                      |
| [SpawnWaitDialog](spawnwaitdialog-controlevent.md)                 | Triggers a specified dialog box.                                                                                                                                                                              |
| [TimeRemaining](timeremaining-controlevent.md)                     | Published by the installer to provide the time remaining in the progress sequence.                                                                                                                            |
| [ValidateProductID](validateproductid-controlevent.md)             | Sets ProductID to the full Product ID.                                                                                                                                                                        |



 

 

