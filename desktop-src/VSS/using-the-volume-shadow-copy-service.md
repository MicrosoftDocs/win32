---
description: VSS backup and restore operations each use a protocol for the interaction of the systems that use mass storage (writers) and those that back it up (requesters).
ms.assetid: c4dae5ce-0dfa-46ec-909f-8ae79d50a9cb
title: Using the Volume Shadow Copy Service
ms.topic: article
ms.date: 05/31/2018
---

# Using the Volume Shadow Copy Service

VSS backup and restore operations each use a protocol for the interaction of the systems that use mass storage (writers) and those that back it up (requesters).

Both backup and restore operations are primarily driven by the requester, which controls writer and provider behavior by generating systemwide COM events for the writer to process. Because event-generating methods are asynchronous, writers do have limited control into the requester's state through the asynchronous handlers available to VSS (see [**IVssAsync**](/windows/desktop/api/Vss/nn-vss-ivssasync)).

This interaction requires basic data structures describing files and groups of files ([*components*](vssgloss-c.md)), as well as a metadata model to allow the storage of backup information and to permit writer/requester communication.

-   [VSS Application Compatibility](usage-conventions.md)
-   [Configuring VSS](configuring-vss.md)
-   [VSS Metadata](vss-metadata.md)
-   [Working with Selectability and Logical Paths](working-with-selectability-and-logical-paths.md)
-   [Overview of Processing a Backup Under VSS](overview-of-processing-a-backup-under-vss.md)
-   [Overview of Processing a Restore Under VSS](overview-of-processing-a-restore-under-vss.md)

 

 



