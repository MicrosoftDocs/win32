---
Description: Restoring an incremental or differential backup under VSS is not significantly different from any other VSS restore operation.
ms.assetid: 67143f6f-0bb8-4740-9289-8bbfeb7caadf
title: Restoring Incremental and Differential Backups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Restoring Incremental and Differential Backups

Restoring an incremental or differential backup under VSS is not significantly different from any other VSS restore operation.

A writer can modify restore targets or request directed targeting, and a requester must handle alternate location mappings and new targets, just as with any other restore. There are, however, two significant issues to be aware of in handling the restore of an incremental or differential backup: additional restores and backup stamps.

## Additional Restores

The first issue is that of additional restores. A backup operator may need to run several restore operations using an initial full and subsequent incremental or differential backup media as a source.

Some writers, typically as part of their handling of a [*PostRestore*](vssgloss-p.md#base-vssgloss-postrestore-event) event using [**CVssWriter::OnPostRestore**](/windows/win32/VsWriter/nf-vswriter-cvsswriter-onpostrestore?branch=master), use restored files to perform updates of data currently on disk. For some of these writers it is inefficient—or dangerous—to repeatedly update on-disk data from restored files.

Therefore, it is important that backup applications indicate when a component or component set may require subsequent restores by calling [**IVssBackupComponents::SetAdditionalRestores**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores?branch=master).

A writer would call [**IVssComponent::GetAdditionalRestores**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getadditionalrestores?branch=master) to determine whether the backup operator planned more restores of the component or component set.

If the requester had not called [**IVssBackupComponents::SetAdditionalRestores**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores?branch=master), then [**IVssComponent::GetAdditionalRestores**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getadditionalrestores?branch=master) returns false, and the writer can perform any post-restore processing it needs to.

If [**IVssBackupComponents::SetAdditionalRestores**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores?branch=master) had been called, then [**IVssComponent::GetAdditionalRestores**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getadditionalrestores?branch=master) returns **true**, and a writer should decide how to handle post-restore operations—for instance, the writer may choose not to update its on-disk data.

## Backup Stamps

As part of the previous full backup operation, a writer may have stored a backup stamp in the requester's Backup Components Document.

The backup stamp is stored as a string, and its format and information are not intelligible to the requester. Therefore, the requester cannot make direct use of the backup stamp information.

Instead, its task is to make that information available to the writer, by calling the [**IVssBackupComponents::SetPreviousBackupStamp**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setpreviousbackupstamp?branch=master) method prior to the generation of a [**PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master) event for an incremental backup.

The requester does this on a component-by-component basis. A requester examines stored component or component set backup stamp information using [**IVssComponent::GetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp?branch=master).

If backup stamp information is appropriate to the type of restore the requester is undertaking, it makes it available as the time stamp of the last backup of a component with the [**IVssBackupComponents::SetPreviousBackupStamp**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setpreviousbackupstamp?branch=master) method.

A writer recovers the backup stamp information using [**IVssComponent::GetPreviousBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpreviousbackupstamp?branch=master). A writer of this class generated the initial backup stamp, so the writer is able to decode this stamp and use the information. Based on this, while handling a [**PreRestore**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore?branch=master) event, a writer may choose to take actions such as changing restore targets or requesting directed targeting.

 

 



