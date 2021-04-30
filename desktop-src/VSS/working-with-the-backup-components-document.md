---
description: A requester creates a Backup Components Document at the start of performing a backup.
ms.assetid: 5e40e45d-6afa-401a-a6b4-7bec460cb9ec
title: Working with the Backup Components Document
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Backup Components Document

A requester creates a Backup Components Document at the start of performing a backup. The document initially contains only a description of the state of the backup operation. During restore, the document should provide instructions on how a requester should proceed in copying files back to disk. In the course of the restore operation, the Backup Components Document is modified and contains the state of that operation.

Unlike the Writer Metadata Document, which is read-only, there is a window in which the Backup Components Document can be modified by both requesters and writers. The document can be updated until the generation of a [*BackupComplete*](vssgloss-b.md) or [*BackupShutdown*](vssgloss-b.md) event during backup operations, and until a [*PostRestore*](vssgloss-p.md) event during restores.

To use a requester's Backup Components Document requires an understanding of the following topics:

-   [Backup Components Document Life Cycle](backup-components-document-life-cycle.md)
-   [Backup Components Document Contents](backup-components-document-contents.md)

 

 



