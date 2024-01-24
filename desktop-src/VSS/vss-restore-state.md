---
description: During a restore operation, the requester can use the IVssBackupComponents::SetRestoreState method to define the type of restore operation in progress.
ms.assetid: f6bf1979-7604-450f-8988-2a17da6b82d7
title: VSS Restore State
ms.topic: article
ms.date: 05/31/2018
---

# VSS Restore State

During a restore operation, the requester can use the [**IVssBackupComponents::SetRestoreState**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestorestate) method to define the type of restore operation in progress. However, most restore operations will not need to override the default restore type (VSS\_RTYPE\_UNDEFINED). Writers should treat this restore type as if it were VSS\_RTYPE\_BY\_COPY. For more information about restore type values, see the [**VSS\_RESTORE\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_restore_type) enumeration.

 

 



