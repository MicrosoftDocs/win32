---
description: A writer's participation in a backup or restore operation, and which of its data are saved, depends on which of its components are explicitly included as part of a requester's Backup Components Document and the relationship between those components and the logical path of other components within the Writer Metadata Document.
ms.assetid: e8920cca-d944-437f-bf6a-7ce8d518746a
title: Working with Selectability and Logical Paths
ms.topic: article
ms.date: 05/31/2018
---

# Working with Selectability and Logical Paths

A writer's participation in a backup or restore operation, and which of its data are saved, depends on which of its components are [*explicitly included*](vssgloss-e.md) as part of a requester's Backup Components Document and the relationship between those components and the logical path of other components within the Writer Metadata Document.

Writers with no components added to a requester's Backup Component Document prior to the generation of a [*PrepareForBackup*](vssgloss-p.md) event (in the case of backup operations) or of a [**PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) event (in the case of restore operations) receive no events after this point and will not participate in the backup or restore operation.

However, a requester's freedom to include or exclude any given component in a backup or restore is governed by the following:

-   Any hierarchy that exists between the components managed by a writer and expressed by [*logical paths*](vssgloss-l.md)
-   Whether the component is designated as being [*selectable for backup*](vssgloss-s.md)
-   Whether it is designated as being [*selectable for restore*](vssgloss-s.md)
-   Whether an explicit dependency exists between a given component in a given writer and other components in other writers

More information on these issues is in the following topics:

-   [Logical Pathing of Components](logical-pathing-of-components.md)
-   [Working with Selectability for Backup](working-with-selectability-for-backup.md)
-   [Working with Selectability For Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md)
-   [Selectability and Working with Component Properties](selectability-and-working-with-component-properties.md)
-   [Dependencies between Components Managed by Different Writers](dependencies-between-components-managed-by-different-writers.md)

 

 



