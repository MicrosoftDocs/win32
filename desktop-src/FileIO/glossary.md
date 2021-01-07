---
description: Terminology used to describe Transactional NTFS (TxF).
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 44cb060c-e6a6-48d6-bbcf-d8dc1ae8ceb2
title: TxF Glossary
ms.topic: article
ms.date: 05/31/2018
---

# TxF Glossary

<dl> <dt>

<span id="fs.availability"></span><span id="FS.AVAILABILITY"></span>**availability**
</dt> <dd>

Availability means that a resource manager will abort transactions even if that would break consistency so that the system can continue to do new work. The default resource manager forces availability on the system volume. For example, if the transaction log is full, new transaction log space cannot be added, and an older transaction that would be aborted requires an outcome to be delivered from a superior resource manager in order for a distributed transaction to complete, the resource manager will not wait for the superior transaction manager and abort that transaction even though that potentially breaks consistency.

</dd> <dt>

<span id="fs.consistency"></span><span id="FS.CONSISTENCY"></span>**consistency**
</dt> <dd>

Consistency means that a resource manager will fail new transactions if it cannot make forward progress. For example, if the transaction log is full, new transaction log space cannot be added, and an older transaction that would be aborted requires an outcome to be delivered from a superior resource manager in order for a distributed transaction to complete, the resource manager will wait for that outcome.

</dd> <dt>

<span id="fs.miniversion"></span><span id="FS.MINIVERSION"></span>**miniversion**
</dt> <dd>

A miniversion is a version of a file that a transacted writer creates during a transaction. The miniversion can be opened later in the transaction with read-only access.

</dd> <dt>

<span id="fs.transacted_reader"></span><span id="FS.TRANSACTED_READER"></span>**transacted reader**
</dt> <dd>

A transacted reader is a transacted file handle opened with any permission that is a part of generic read access, but is not part of generic write access.

</dd> <dt>

<span id="fs.transacted_writer"></span><span id="FS.TRANSACTED_WRITER"></span>**transacted writer**
</dt> <dd>

A transacted writer is a transacted file handle opened with any permission that is not part of generic read access, but is part of generic write access.

</dd> </dl>

 

 



