---
title: Data Deduplication API Structures
description: The following structures are used by the Data Deduplication API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'C7999A9B-1543-4D96-9F4A-24F529326983'
ms.prod: 'windows-server-dev'
ms.technology:
- 'data-deduplication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Data Deduplication API Structures

The following structures are used by the Data Deduplication API.

## In this section

<dl> <dt>

[**DDP\_FILE\_EXTENT**](ddp-file-extent.md)
</dt> <dd>

[**DDP\_FILE\_EXTENT**](ddp-file-extent.md) represents the extent of data in a file that is to be read in a pending call to [**ReadBackupFile**](idedupreadfilecallback-readbackupfile.md).

</dd> <dt>

[**DEDUP\_CONTAINER\_EXTENT**](dedup-container-extent.md)
</dt> <dd>

A logical container file may be stored in a single segment or multiple segments in the backup store. [**DEDUP\_CONTAINER\_EXTENT**](dedup-container-extent.md) represents a single extent of a specific container file as stored in the backup store. The extent may be the full container file or a portion of the file.

</dd> </dl>

 

 




