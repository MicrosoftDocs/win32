---
Description: 'There are a number of different types of shadow copy a requester can create.'
ms.assetid: 'a20570ea-e3eb-4d65-b8fa-9a27ce1a3e74'
title: Simple Shadow Copy Creation for Backup
---

# Simple Shadow Copy Creation for Backup

There are a number of different types of shadow copy a requester can create. However, for most backup applications, you would do the following:

1.  Call [**IVssBackupComponents::SetContext**](ivssbackupcomponents-setcontext.md) with a context of VSS\_CTX\_BACKUP.
2.  Call [**IVssBackupComponents::GatherWriterMetadata**](ivssbackupcomponents-gatherwritermetadata.md) to initialize communication with writers.
3.  Call [**IVssBackupComponents::AddComponent**](ivssbackupcomponents-addcomponent.md) to add file and database components to the backup.
4.  Call [**IVssBackupComponents::StartSnapshotSet**](ivssbackupcomponents-startsnapshotset.md) to initialize the shadow copy mechanism.
5.  Call [**IVssBackupComponents::AddToSnapshotSet**](ivssbackupcomponents-addtosnapshotset.md) to include volumes in the shadow copy.
6.  Call [**IVssBackupComponents::PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md) to notify writers of backup operations.

 

 



