---
description: Writer participation in a VSS backup is designed to allow applications to control what and how their restore data is to be used.
ms.assetid: 076b2e6f-c2ca-4129-8827-1b18a655d634
title: Restores without Writer Participation
ms.topic: article
ms.date: 05/31/2018
---

# Restores without Writer Participation

Writer participation in a VSS backup is designed to allow applications to control what and how their restore data is to be used.

In general, if a writer is available on a system, it is never advisable to restore data to its original location without writer participation. Such a restore would likely encounter locked destination files and runs a significant risk of corrupting data.

However, there are reasons why a backup application might want or need to restore a VSS backup without writer participation:

-   Data is managed by VSS-unaware applications. Almost every system will have some applications—text editors, mail readers, word processors, and so forth—that are VSS unaware. This data cannot be restored using writer participation.

    Generally, this type of data is not system- or service-critical, and restoring it should not be problematic, or at least no more problematic than during a conventional restore.

    As with preparations for conventional restores, if possible, restore operators should attempt to suspend or terminate such applications prior to starting a VSS restore.

-   Missing VSS writers. This situation may be fairly common when restoring the state of a damaged system. A backup operation must determine whether it is desirable to restore files for missing writers. If restoration is desirable, the files can be restored just as a conventional backup would restore them.
-   A private restore of a writer's data. A requester may choose to restore the data of a running writer to some private location without notifying the writer. An example of this might be restoration of the writer's data to support offline comparison. In this sort of situation, a requester would not want to use the [*new target location*](vssgloss-n.md) while doing the restore, because it does not want the writer to access the data.
-   A writer does not want to be involved during restore. A writer indicates this by passing in VSS\_WRE\_NEVER for the *writerRestore* parameter of [**IVssCreateWriterMetadata::SetRestoreMethod**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setrestoremethod).
-   A writer requires a custom restore method. A writer indicates that it requires a custom restore by passing in VSS\_RME\_CUSTOM for the *method* parameter of [**IVssCreateWriterMetadata::SetRestoreMethod**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-setrestoremethod). In this case, this writer should not be involved in the restore process unless the custom-restore documentation for that writer indicates otherwise.

A requester involves a writer in the restore process by specifying one of that writer's components in a call to [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore). A writer's data can be restored without involving the writer by simply not specifying any of that writer's components in a call to **IVssBackupComponents::SetSelectedForRestore**. If a writer does not expect any restore events, involving that writer in the restore process can cause spurious errors to be reported for that writer.

 

 



