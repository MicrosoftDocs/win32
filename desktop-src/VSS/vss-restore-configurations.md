---
description: File restoration on a running system can be problematic. It is important that running applications (writers) indicate what to do when difficulties arise during restores, for instance, if the file being restored is currently in use.
ms.assetid: 2cb963a8-7077-4419-96d8-cba0fd011e4f
title: VSS Restore Configurations
ms.topic: article
ms.date: 05/31/2018
---

# VSS Restore Configurations

File restoration on a running system can be problematic. It is important that running applications (writers) indicate what to do when difficulties arise during restores, for instance, if the file being restored is currently in use.

Under VSS, writers have two complementary ways of managing restores—[*restore methods*](vssgloss-r.md) and [*restore targets*](vssgloss-r.md).

In addition, requesters can choose to restore files to previously unspecified locations and notify writers (see [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget)).

The restore method (also call the original restore target) is specified by a writer at a backup time, and sets a writer-wide definition of the method to be used to restore all its components in the future. All files and components managed by a writer share the same restore method.

Restore targets allow writers to change how specific components are to be restored at restore time. Unlike restore methods, restore targets are defined for a component set.

A detailed discussion of the usage of restore methods and restore targets is found in the topics listed below:

-   [VSS Restore State](vss-restore-state.md)
-   [Setting VSS Restore Methods](setting-vss-restore-methods.md)
-   [Setting VSS Restore Targets](setting-vss-restore-targets.md)
-   [Setting VSS Restore Options](setting-vss-restore-options.md)

(For information on restores that do not use these mechanisms, see [Restores without Writer Participation](restores-without-writer-participation.md).)

 

 



