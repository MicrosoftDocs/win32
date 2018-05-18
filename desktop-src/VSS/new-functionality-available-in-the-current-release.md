---
Description: 'The Windows Server 2003 release of the Volume Shadow Copy Service contains the following new functionality:'
ms.assetid: '3dcfcc01-3e3c-43e9-a933-5c72f331da9a'
title: New Functionality Available in Windows Server 2003
---

# New Functionality Available in Windows Server 2003

The Windows Server 2003 release of the Volume Shadow Copy Service contains the following new functionality:

-   Support for [*selectability for restore*](vssgloss-s.md#base-vssgloss-selectability-for-restore) in addition to and on an equal basis with [*selectability for backup*](vssgloss-s.md#-win32-vssgloss-selectability-for-backup) (previously just referred to as selectability). See [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md) for more information.
-   Introduction of a [*BackupShutdown*](vssgloss-b.md#base-vssgloss-backupshutdown-event) event indicating that a VSS-compliant backup application (requester) has shut down, whether the backup attempt has properly completed or not. See [Handling BackupShutdown Events](handling-backupshutdown-events.md) for more information.
-   Support for explicit writer-component dependencies. A means for describing and supporting the situations where a component (and the component set it defines) managed by one writer cannot be backed up or restore independently of components managed by other writers. See [Dependencies between Components Managed by Different Writers](dependencies-between-components-managed-by-different-writers.md) for more information.
-   Full support for [*partial files*](vssgloss-p.md#base-vssgloss-partial-file-support) operations. The backup and restore of segments of files by writers and requesters is now fully supported. See [Working with Partial Files](working-with-partial-files.md) for more information on partial file operations.
-   Introduction of [*differenced files*](vssgloss-d.md#base-vssgloss-differenced-files) to support incremental backup and restore operations. See [Incremental and Differential Backups](incremental-and-differential-backups.md) for more information.
-   Introduction of backup schemas as a concept indicating the level of writer support for types of backup operations. See [**VSS\_BACKUP\_SCHEMA**](vss-backup-schema.md) for more information.
-   Support for requester specification of new file restore destinations ([*new target locations*](vssgloss-n.md#base-vssgloss-new-target-location)) during restore operations. See [Working with New Targets during Restore](working-with-new-targets-during-restore.md) for more information.
-   Support for conditional restore at reboot time. See VSS\_RME\_RESTORE\_AT\_REBOOT\_IF\_CANNOT\_REPLACE ([**VSE\_RESTOREMETHOD\_ENUM**](vss-restoremethod-enum.md)) for more information.
-   Definition of a restore state and restore type. See [**VSS\_RESTORE\_TYPE**](vss-restore-type.md) and [VSS Restore State](vss-restore-state.md) for more information.
-   Support for writer queries about shadow copy state. See [**CVssWriter::GetContext**](cvsswriter-getcontext.md) and [**CVssWriter::GetSnapshotDeviceName**](cvsswriter-getsnapshotdevicename.md) for more information.
-   Support for transportable shadow copies in Windows Server 2003, Enterprise Edition and Windows Server 2003, Datacenter Edition. For more information, see [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md).

 

 



