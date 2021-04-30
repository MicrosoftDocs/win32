---
description: Both writers and requesters maintain information necessary to a backup or restore operation in their own metadata documents.
ms.assetid: 1ce56374-cfbf-4ee4-b942-8a7391911a38
title: VSS Metadata
ms.topic: article
ms.date: 05/31/2018
---

# VSS Metadata

Both writers and requesters maintain information necessary to a backup or restore operation in their own metadata documents.

These documents, the [*Writer Metadata Document*](vssgloss-w.md) and the [*Backup Components Document*](vssgloss-b.md), respectively, are used as the basis for writer and requester communication and coordination during backup and restore activities.

The metadata is represented in XML format using a proprietary schema. Metadata can be copied to disk, tape, or any other mass storage device. It should always be saved to the backup media during a backup operation, and will need to be retrieved from that media in the course of a restore operation.

**Caution:** The specific details of the format and schema are for system use only. Developers should not attempt to modify or directly use the XML representation of the metadata.

Writers and requesters are provided with a variety of query and set methods to access and modify the Backup Components and Writer Metadata documents:

-   [Working with the Writer Metadata Document](working-with-the-writer-metadata-document.md)
-   [Working with the Backup Components Document](working-with-the-backup-components-document.md)
-   [VSS Metadata Components](vss-metadata-components.md)

 

 



