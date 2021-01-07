---
description: There are a number of different types of shadow copy a requester can create.
ms.assetid: a20570ea-e3eb-4d65-b8fa-9a27ce1a3e74
title: Simple Shadow Copy Creation for Backup
ms.topic: article
ms.date: 05/31/2018
---

# Simple Shadow Copy Creation for Backup

There are a number of different types of shadow copy a requester can create. However, for most backup applications, you would do the following:

1.  Call [**IVssBackupComponents::SetContext**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext) with a context of VSS\_CTX\_BACKUP.
2.  Call [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) to initialize communication with writers.
3.  Call [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) to add file and database components to the backup.
4.  Call [**IVssBackupComponents::StartSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset) to initialize the shadow copy mechanism.
5.  Call [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset) to include volumes in the shadow copy.
6.  Call [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup) to notify writers of backup operations.

 

 



