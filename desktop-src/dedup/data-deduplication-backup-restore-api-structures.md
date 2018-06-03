---
title: Data Deduplication API Structures
description: The following structures are used by the Data Deduplication API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C7999A9B-1543-4D96-9F4A-24F529326983
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data Deduplication API Structures

The following structures are used by the Data Deduplication API.

## In this section

<dl> <dt>

[**DDP\_FILE\_EXTENT**](/previous-versions/windows/desktop/api/DdpBackup/ns-ddpbackup-_ddp_file_extent)
</dt> <dd>

[**DDP\_FILE\_EXTENT**](/previous-versions/windows/desktop/api/DdpBackup/ns-ddpbackup-_ddp_file_extent) represents the extent of data in a file that is to be read in a pending call to [**ReadBackupFile**](/previous-versions/windows/desktop/api/DdpBackup/nf-ddpbackup-idedupreadfilecallback-readbackupfile).

</dd> <dt>

[**DEDUP\_CONTAINER\_EXTENT**](/previous-versions/windows/desktop/api/DdpBackup/ns-ddpbackup-_dedup_container_extent)
</dt> <dd>

A logical container file may be stored in a single segment or multiple segments in the backup store. [**DEDUP\_CONTAINER\_EXTENT**](/previous-versions/windows/desktop/api/DdpBackup/ns-ddpbackup-_dedup_container_extent) represents a single extent of a specific container file as stored in the backup store. The extent may be the full container file or a portion of the file.

</dd> </dl>

 

 




