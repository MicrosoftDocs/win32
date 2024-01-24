---
description: 'The Windows Server 2003 release of the Volume Shadow Copy Service contains the following new functionality:'
ms.assetid: 3dcfcc01-3e3c-43e9-a933-5c72f331da9a
title: New Functionality Available in Windows Server 2003
ms.topic: article
ms.date: 05/31/2018
---

# New Functionality Available in Windows Server 2003

The Windows Server 2003 release of the Volume Shadow Copy Service contains the following new functionality:

-   Support for [*selectability for restore*](vssgloss-s.md) in addition to and on an equal basis with [*selectability for backup*](vssgloss-s.md) (previously just referred to as selectability). See [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md) for more information.
-   Introduction of a [*BackupShutdown*](vssgloss-b.md) event indicating that a VSS-compliant backup application (requester) has shut down, whether the backup attempt has properly completed or not. See [Handling BackupShutdown Events](handling-backupshutdown-events.md) for more information.
-   Support for explicit writer-component dependencies. A means for describing and supporting the situations where a component (and the component set it defines) managed by one writer cannot be backed up or restore independently of components managed by other writers. See [Dependencies between Components Managed by Different Writers](dependencies-between-components-managed-by-different-writers.md) for more information.
-   Full support for [*partial files*](vssgloss-p.md) operations. The backup and restore of segments of files by writers and requesters is now fully supported. See [Working with Partial Files](working-with-partial-files.md) for more information on partial file operations.
-   Introduction of [*differenced files*](vssgloss-d.md) to support incremental backup and restore operations. See [Incremental and Differential Backups](incremental-and-differential-backups.md) for more information.
-   Introduction of backup schemas as a concept indicating the level of writer support for types of backup operations. See [**VSS\_BACKUP\_SCHEMA**](/windows/desktop/api/Vss/ne-vss-vss_backup_schema) for more information.
-   Support for requester specification of new file restore destinations ([*new target locations*](vssgloss-n.md)) during restore operations. See [Working with New Targets during Restore](working-with-new-targets-during-restore.md) for more information.
-   Support for conditional restore at reboot time. See VSS\_RME\_RESTORE\_AT\_REBOOT\_IF\_CANNOT\_REPLACE ([**VSE\_RESTOREMETHOD\_ENUM**](/windows/desktop/api/VsWriter/ne-vswriter-vss_restoremethod_enum)) for more information.
-   Definition of a restore state and restore type. See [**VSS\_RESTORE\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_restore_type) and [VSS Restore State](vss-restore-state.md) for more information.
-   Support for writer queries about shadow copy state. See [**CVssWriter::GetContext**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-getcontext) and [**CVssWriter::GetSnapshotDeviceName**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-getsnapshotdevicename) for more information.
-   Support for transportable shadow copies in Windows Server 2003, Enterprise Edition and Windows Server 2003, Datacenter Edition. For more information, see [Importing Transportable Shadow Copied Volumes](importing-transportable-shadow-copied-volumes.md).

 

 



