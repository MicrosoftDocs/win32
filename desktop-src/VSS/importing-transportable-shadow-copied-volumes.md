---
description: It is sometimes desirable to create a shadow copy on one system, but use the shadow copy on a second system.
ms.assetid: 4ec63917-03c0-434e-892e-3d9d4c47740e
title: Importing Transportable Shadow Copied Volumes
ms.topic: article
ms.date: 05/31/2018
---

# Importing Transportable Shadow Copied Volumes

It is sometimes desirable to create a shadow copy on one system, but use the shadow copy on a second system.

Consider the case where data to be backed up is normally managed by a given system (*systemOne*) during normal operations, and that this data is physically stored on a storage array or an appliance.

To minimize any disruption to *systemOne* (because backup operations can be resource intensive), it is desirable to perform the backup using *systemTwo*, a backup server, which has access to the same storage array as *systemOne*.

To ensure a proper shadow copy—cooperating with the writers on *systemOne* and preserving the state appropriately for ongoing tasks—the shadow copy should be performed by *systemOne*.

Therefore, *systemOne* must create a [*transportable shadow copy*](vssgloss-t.md), which *systemTwo* will then import.

**Windows Server 2003, Standard Edition, Windows Server 2003, Web Edition and Windows XP:** Transportable shadow copy sets are not supported. All editions of Windows Server 2003 with Service Pack 1 (SP1) support transportable shadow copy sets.

A typical example of importing a transportable shadow copy can proceed in the following way:

1.  Initially, the logical unit (LUN) that is provided by the storage array is mounted as a volume on *systemOne* (say, F:).
2.  A requester that is running on *systemOne* instantiates an instance of [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) and proceeds as if it were preparing for a backup. (See [Overview of Backup Initialization](overview-of-backup-initialization.md), [Overview of the Backup Discovery Phase](overview-of-the-backup-discovery-phase.md), and [Overview of Pre-Backup Tasks](overview-of-pre-backup-tasks.md) for more information.)
3.  The requester on *systemOne* modifies the shadow copy context that is typically used for local backup operation (**VSS\_CTX\_APP\_BACKUP**) to indicate that a transportable shadow copy will be created (**VSS\_VOLSNAP\_ATTR\_TRANSPORTABLE**). The transportable attribute can be added to other shadow copy contexts as well.
4.  With a shadow copy context of **VSS\_CTX\_APP\_BACKUP** \| **VSS\_VOLSNAP\_ATTR\_TRANSPORTABLE**, the requester that is on *systemOne* creates a shadow copy by calling [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset).
5.  *SystemOne* uses [**IVssBackupComponents::SaveAsXML**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-saveasxml) to save the current state of the Backup Components Document and [**IVssExamineWriterMetadata::SaveAsXML**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-saveasxml) to save each writer's Writer Metadata Documents. The XML strings that contain these documents are then made available to a requester that is running on *systemTwo*.

    The requester transfers the Backup Components Document to *systemTwo*.

    Note that the requester on *systemOne* does not release its instance of [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) at this point if the purpose of the shadow copy is for backup. The interface should remain open until *systemTwo* successfully finishes its backup operations. Only then should the requester issue a [**BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) event since some writers will truncate logs and do other work after a successful backup. If the goal of the shadow copy is data mining or other purposes, then the interface can be closed at this step.

6.  The requester on *systemTwo* then calls [**IVssBackupComponents::ImportSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-importsnapshots) to get access to the shadow copy that was created by the requester on *systemOne*.
    > [!Note]  
    > The requester is responsible for serializing the import shadow copy operation. Also, if the call to [**IVssBackupComponents::ImportSnapshots**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-importsnapshots) fails, the VSS won't clean up LUNs on it's own. The requester has to initiate the cleanup of LUNs.

     

7.  The requester on *systemTwo* proceeds with the backup of the shadow copied material exactly as if it were backing up a shadow copy that it created by itself (see [Overview of Actual Backup Of Files](overview-of-actual-backup-of-files.md)).

    The requester on *systemTwo* obtains the shadow copy's [*device object*](vssgloss-d.md) using [**IVssBackupComponents::GetSnapshotProperties**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getsnapshotproperties) on the imported shadow copy and appends that to the beginning of the original file paths that were obtained from the metadata to access files to be backed up.

8.  After using the shadow copy, the requester on *systemTwo* must delete the shadow copy. As with non-transportable shadow copies, if the shadow copy context indicates auto-release shadow copies (for example, **VSS\_CTX\_BACKUP**), then releasing the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) on *systemTwo* will cause the VSS service to delete the shadow copy. Otherwise, if the context indicates a persistent shadow copy (for example, **VSS\_CTX\_APP\_ROLLBACK**), then the requester on *systemTwo* must explicitly delete the shadow copy.

    Then the requester on *systemTwo* signals the requester on *systemOne* that it has finished with the backup of the transportable shadow copy.

9.  After the requester on *systemOne* has received notification that the requester on *systemTwo* has finished the backup of the transportable shadow copy, it notifies the writers on its system by generating a [**BackupComplete**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) event with a call to **IVssBackupComponents::BackupComplete**. At this point, the requester on *systemOne* is free to release its instance of [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents).

**Transportable shadow copies in a cluster:** Transportable shadow copies must be imported from outside the cluster as long as the original volume is mounted within the cluster. For information about implementing a fast recovery in a cluster, see [Fast Recovery Using Transportable Shadow Copied Volumes](fast-recovery-using-transportable-shadow-copied-volumes.md).

 

 



