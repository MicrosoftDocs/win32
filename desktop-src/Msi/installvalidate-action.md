---
description: The InstallValidate action verifies that all volumes to which cost has been attributed have sufficient space for the installation. The InstallValidate action ends the installation with a fatal error if any volume is short of disk space.
ms.assetid: 1c55794d-1ecc-43bf-956f-96afc5f36964
title: InstallValidate Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallValidate Action

The InstallValidate action verifies that all [*volumes*](v-gly.md) to which [*cost*](c-gly.md) has been attributed have sufficient space for the installation. The InstallValidate action ends the installation with a fatal error if any volume is short of disk space.

The InstallValidate action also notifies the user if one or more files to be overwritten or removed are currently in use by an active process. For more information, see [System Reboots](system-reboots.md).

## Sequence Restrictions

The [CostFinalize](costfinalize-action.md) action and any UI dialog box sequences that allow the user to modify selection states and/or directories should be sequenced before the InstallValidate action.

[Custom actions](custom-actions.md) that change the installation state of features or components must be sequenced before the InstallValidate action.

## ActionData Messages

There are no ActionData messages.

## Remarks

Typically, an earlier UI dialog box sequence should perform the same verification as the InstallValidate action when the user attempts to initiate the copying of files. This UI dialog box sequence should present an **Out of Disk Space** dialog box if the volumes selected do not have enough space for the installation. The UI dialog boxes should be authored in a way to prevent the user from proceeding with the installation if there is insufficient disk space. In the case of a quiet installation, there is no user interface and the InstallValidate action terminates the installation if there is insufficient disk space. The cause of the premature termination is recorded in the log file if logging is enabled.

An entry is added to an internal FilesInUse table if any file is overwritten or removed while it is open for execution or modification by any process during file [*costing*](c-gly.md). The FilesInUse table contains columns for the name and full path of the file. When the InstallValidate action executes, the installer queries the FilesInUse table for entries and determines the name of the process using the file. The InstallValidate action adds one record to the [ListBox](listbox-table.md) user interface table for each unique process identified by this query. The record contains the following values in each column:

**Property**: FileInUseProcess

 

**Value**: *Name of process*

 

**Text**: *Text contained in the caption of the main window of the process*

The InstallValidate action then displays the **Files In Use** dialog box. This dialog box displays the processes that must be shut down to avoid the requirement of restarting the system to replace files in use.

The InstallValidate action queries the [Dialog](dialog-table.md) table for an authored dialog box with the reserved name [FilesInUse](filesinuse-dialog.md) dialog and displays it. This dialog box must contain a [ListBox](listbox-control.md) control that is tied to a property named FileInUseProcess. By convention, this dialog box has an **Exit**, **Retry**, or **Ignore** button, but this is up to the UI author. Each button should be tied to an [EndDialog](enddialog-controlevent.md) ControlEvent in the [ControlEvent](controlevent-table.md) table. The InstallValidate action responds as follows to the value returned by the [DoAction](doaction-controlevent.md) ControlEvent, as dictated by one of these [EndDialog](enddialog-controlevent.md) arguments associated with the button pushed by the user:

**Retry**: All values added to the [ListBox](listbox-table.md) table are cleared, and the entire file [*costing*](c-gly.md) procedure is repeated, rechecking for files that are still in use. If one or more processes are still identified as using files to be overwritten or deleted, the process repeats; otherwise, InstallValidate returns control to the installer with a status of msiDoActionStatusSuccess.

**Exit**: The InstallValidate action immediately returns control to the installer with a status of msiDoActionStatusUserExit. This terminates the installation.

**Any other return value**: The InstallValidate action immediately returns control to the installer with a status of msiDoActionStatusSuccess. In this case, since one or more files are still in use, the subsequent [InstallFiles](installfiles-action.md) and/or [InstallAdminPackage](installadminpackage-action.md) actions must schedule the in-use file(s) to be replaced or deleted when the system is restarted.

If there is no [ListBox](listbox-table.md) table in the database, InstallValidate exits silently without an error.

The semicolon is the list delimiter for transforms, sources, and patches, and should not be used in these file names or paths.

Files marked read-only in a read-only location are never considered in use by the installer.

A default **Out of Disk Space** dialog box containing **Abort** and **Retry** buttons is presented to the user if the user interface level is basic.

 

 



