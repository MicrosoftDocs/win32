---
description: A shadow copy is a snapshot of a volume that duplicates all of the data that is held on that volume at one well-defined instant in time. VSS identifies each shadow copy by a persistent GUID.
ms.assetid: 8ef2478a-c8bc-4517-9a14-e1d9226ec4cd
title: Shadow Copies and Shadow Copy Sets
ms.topic: article
ms.date: 05/31/2018
---

# Shadow Copies and Shadow Copy Sets

A [*shadow copy*](vssgloss-s.md) is a snapshot of a volume that duplicates all of the data that is held on that volume at one well-defined instant in time. VSS identifies each shadow copy by a persistent GUID.

A [*shadow copy set*](vssgloss-s.md) is a collection of shadow copies of various volumes all taken at the same time. VSS identifies each shadow copy set by a persistent GUID.

How a particular hardware or software vendor chooses to implement shadow copies is completely at its discretion. Once a shadow copy is created, there are effectively two images of the shadow-copied volume available to the system: the original volume, which can be accessed conventionally; and the copied data, which can be accessed through the VSS API.

This allows two sets of activities to take place at the same time:

-   Ordinary applications on the system can quickly continue or resume using the original volume, updating data on the disk.
-   Applications that are using the VSS requester API to access the shadow-copied volume can perform backups or similar operations.

Shadow copies need not be implemented in the same way for every file, directory, or volume. Different implementations of the shadow copy mechanism ([*providers*](vssgloss-p.md)) may use different approaches to creating a shadow copy. However, to all applications that are using the VSS API, all shadow copies should appear the same.

For information on the default Windows provider implementation, see [System Provider](providers.md).

## Default Shadow Copy State

Even though the file system flushes all I/O buffers prior to creating a shadow copy, this will not ensure that incomplete I/O is properly handled.

Therefore, assuming that the system has no VSS-enabled applications, the data in a shadow copy is said to be in a [*crash-consistent state*](vssgloss-c.md). A shadow copy in a crash-consistent state contains an image of the disk that is the same as that which would exist following a catastrophic system shutdown. All files that were open will still exist on the volume, but they are not guaranteed to be free of incomplete I/O operations or data corruption.

While the crash-consistent state does not fully deal with all the issues associated with defining a stable backup set (see [Common Volume Backup Issues](common-volume-backup-issues.md)), it has several advantages over the backup set that conventional backup operations would have to use:

-   A volume contained in a shadow copy, even in a crash-consistent state, still contains all files. A backup set created without a shadow copy would not contain all files open at the time of the backup. Files held open at the time of the backup operation are excluded from the backup.
-   The shadow copy of the volume is created at one instant in time, and not by traversing an active file system, which typically requires much more time.

Applications on a system that are not VSS-aware—word processors, editors, and so on—will likely have their files left in a crash-consistent state. However, VSS-aware applications (writers) can coordinate their actions so that the state of their files in the shadow copy is well defined and consistent.

## Shadow Copy Freeze and Thaw

The creation of every VSS shadow copy operation is bracketed by [*Freeze*](vssgloss-f.md) and [*Thaw*](vssgloss-t.md) events, which writers use to put their files in a stable state prior to shadow copy.

Having Freeze and Thaw events as part of the VSS model means:

-   Handling the Freeze event means that those who are developing writers must have a clearly delineated point in the backup cycle where they ensure that all write operations to the disk are stopped and that files are in a well-defined state for backup.
-   Handling the Thaw event provides the mechanism for writers to resume writes to the disk and clean up any temporary files or other temporary state information that were created in association with the shadow copy.
-   The default window between the Freeze and Thaw events is short (typically 60 seconds); therefore, actual interruption of any service that a writer provides can be minimized.
-   Handling of other events (such as PrepareForSnapshot) preceding and following the Freeze and Thaw events, respectively, provides the necessary flexibility to allow writers to complete complicated operations to support shadow copies.

 

 



