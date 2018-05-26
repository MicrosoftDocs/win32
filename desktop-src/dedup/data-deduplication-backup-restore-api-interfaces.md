---
title: Data Deduplication API Interfaces
description: The following interfaces are used by Data Deduplication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FC9B67D5-2BA2-41AB-9A59-1360AA9828DA
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Data Deduplication API Interfaces

The following interfaces are used by Data Deduplication.

## In this section

<dl> <dt>

[**IDedupBackupSupport**](/windows/previous-versions/DdpBackup/nn-ddpbackup-idedupbackupsupport?branch=master)
</dt> <dd>

Provides a method for restoring a file from a backup store containing copies of Data Deduplication reparse points, metadata, and container files.

</dd> <dt>

[**IDedupReadFileCallback**](/windows/previous-versions/DdpBackup/nn-ddpbackup-idedupreadfilecallback?branch=master)
</dt> <dd>

A callback interface, implemented by backup applications, that enables Data Deduplication to read content from metadata and container files residing in a backup store and optionally improve restore efficiency.

</dd> </dl>

 

 




