---
Description: VSS is designed to address the problems described in Common Volume Backup Issues.
ms.assetid: f9a3efea-d6e8-40df-92ac-f6faaa4fca60
title: The VSS Model
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The VSS Model

VSS is designed to address the problems described in [Common Volume Backup Issues](common-volume-backup-issues.md).

The VSS model includes the following:

-   The shadow copy mechanism. VSS provides fast volume capture of the state of a disk at one instant in time—a [*shadow copy*](https://www.bing.com/search?q=*shadow copy*) of the volume. This volume copy exists side by side with the live volume, and contains copies of all files on disk effectively saved and available as a separate device.
-   Consistent file state via application coordination. VSS provides a COM-based, event-driven interprocess communication mechanism that participating processes can use to determine system state with respect to backup, restore, and shadow copy (volume capture) operations. These events define stages by which applications modifying data on disk ([*writers*](https://www.bing.com/search?q=*writers*)) can bring all their files into a consistent state prior to the creation of the shadow copy.
-   Minimizing application downtime. The VSS shadow copy exists in parallel with a live copy of the volume to be backed up, so except for the brief period of the shadow copy's preparation and creation, an application can continue its work. The time needed to actually create a shadow copy, which occurs between [*Freeze*](https://www.bing.com/search?q=*Freeze*) and [*Thaw*](https://www.bing.com/search?q=*Thaw*) events, typically takes about one minute.

    While a writer's preparation for a shadow copy, including flushing I/O and saving state (see [Overview of Pre-Backup Tasks](overview-of-pre-backup-tasks.md)), may be nontrivial, it is significantly shorter than the time required to actually back up a volume—which for large volumes may take hours.

-   Unified interface to VSS. VSS abstracts the shadow copy mechanisms within a common interface while enabling a hardware vendor to add and manage the unique features of its own providers. Any backup application ([*requester*](https://www.bing.com/search?q=*requester*)) and any writer should be able to run on any disk storage system that supports the VSS interface.
-   Multivolume backup. VSS supports [*shadow copy sets*](https://www.bing.com/search?q=*shadow copy sets*), which are collections of shadow copies, across multiple types of disk volumes from multiple vendors. All shadow copies in a shadow copy set will be created with the same time stamp and will present the same disk state for a multivolume disk state.
-   Native shadow copy support. Beginning with Windows XP, shadow copy support is available through VSS as a native part of the Windows operating system. As long as at least one NTFS disk is present on a system, these systems can be configured to support shadow copies of all disk systems mounted on them.

 

 



