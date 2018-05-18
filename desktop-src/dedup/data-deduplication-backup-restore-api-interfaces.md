---
title: Data Deduplication API Interfaces
description: The following interfaces are used by Data Deduplication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'FC9B67D5-2BA2-41AB-9A59-1360AA9828DA'
ms.prod: 'windows-server-dev'
ms.technology:
- 'data-deduplication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Data Deduplication API Interfaces

The following interfaces are used by Data Deduplication.

## In this section

<dl> <dt>

[**IDedupBackupSupport**](idedupbackupsupport.md)
</dt> <dd>

Provides a method for restoring a file from a backup store containing copies of Data Deduplication reparse points, metadata, and container files.

</dd> <dt>

[**IDedupReadFileCallback**](idedupreadfilecallback.md)
</dt> <dd>

A callback interface, implemented by backup applications, that enables Data Deduplication to read content from metadata and container files residing in a backup store and optionally improve restore efficiency.

</dd> </dl>

 

 




