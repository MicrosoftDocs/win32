---
description: In processing a backup under VSS, requesters and writers worked together to produce a stable system image from which to back up data, which required coordination and the creation of a shadow copy of the current system.
ms.assetid: 1cefb6ac-f2bb-464b-a62f-05be91ae56f7
title: Overview of Processing a Restore Under VSS
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Processing a Restore Under VSS

In processing a backup under VSS, requesters and writers worked together to produce a stable system image from which to back up data, which required coordination and the creation of a shadow copy of the current system.

In contrast to a VSS backup, where the purpose of requester and writers coordination is to produce a stable system image from which to copy data, the objective of a VSS-based restore is to return files to disk in a manner most useful to applications (writers) currently running on the system. This does not require a stable system image, so no shadow copy is necessary.

Instead, attention is focused on avoiding disruption of writer activity, preventing the creation of inconsistent data sets on disk, and allowing writers the necessary scope to evaluate and merge data when necessary.

Like a backup operation, a VSS restore requires access to both a Backup Components Document and to Writer Metadata Documents. These documents are not generally obtained by querying running applications, but instead are retrieved from versions stored as XML documents on backup media.

As is the case during backup operations, the Writer Metadata Documents remain read-only objects, and (once retrieved) the Backup Components Document can still be modified. Modifications of the Backup Components Document allow writers and requester to communicate about the following:

-   Overriding [*restore methods*](vssgloss-r.md) with [*restore targets*](vssgloss-r.md)
-   Using [*alternate location mappings*](vssgloss-a.md)
-   Restoring files to new locations on disk
-   Using different selection rules from those used during backup

To more fully understand the basic tasks involved in performing a restore, it is useful to break down this overview into the following topics:

-   [Overview of Restore Initialization](overview-of-restore-initialization.md)
-   [Overview of Preparing for Restore](overview-of-preparing-for-restore.md)
-   [Overview of Actual File Restoration](overview-of-actual-file-restoration.md)
-   [Overview of Restore Clean up and Termination](overview-of-restore-clean-up-and-termination.md)

 

 



