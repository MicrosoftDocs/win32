---
Description: There are a number of different types of shadow copy a requester can create.
ms.assetid: a20570ea-e3eb-4d65-b8fa-9a27ce1a3e74
title: Simple Shadow Copy Creation for Backup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Simple Shadow Copy Creation for Backup

There are a number of different types of shadow copy a requester can create. However, for most backup applications, you would do the following:

1.  Call [**IVssBackupComponents::SetContext**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext?branch=master) with a context of VSS\_CTX\_BACKUP.
2.  Call [**IVssBackupComponents::GatherWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata?branch=master) to initialize communication with writers.
3.  Call [**IVssBackupComponents::AddComponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent?branch=master) to add file and database components to the backup.
4.  Call [**IVssBackupComponents::StartSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset?branch=master) to initialize the shadow copy mechanism.
5.  Call [**IVssBackupComponents::AddToSnapshotSet**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset?branch=master) to include volumes in the shadow copy.
6.  Call [**IVssBackupComponents::PrepareForBackup**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup?branch=master) to notify writers of backup operations.

 

 



