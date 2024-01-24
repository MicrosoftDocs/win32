---
description: When a VSS backup operation is conducted without the involvement of a writer, the shadow copy creation can still occur.
ms.assetid: 2058e894-bde5-4690-a7aa-849d2e9cdc71
title: Backups without Writer Participation
ms.topic: article
ms.date: 05/31/2018
---

# Backups without Writer Participation

When a VSS backup operation is conducted without the involvement of a writer, the shadow copy creation can still occur.

As noted elsewhere (see [Default Shadow Copy State](shadow-copies-and-shadow-copy-sets.md)), the result of this type of shadow copy is a volume reflecting the state of a disk at the time of the shadow copy: data on the shadow-copied volume may reflect incomplete or partial I/O operations and is described as being in a [*crash-consistent state*](vssgloss-c.md).

There are several situations that will require a backup application to work with crash consistent shadow copied data:

-   **Data is managed by VSS-unaware applications**

    Almost every system will have some applications—text editors, mail readers, word processors, and so forth—that are VSS unaware, so it is always likely that some of the data on a shadow copy will need to be thought of as being in a crash consistent state.

    This sort of data is not typically system- or service-critical, so backing it up should not be problematic, or at least no more problematic than during a conventional backup.

    As with preparations for conventional backups, if possible, backup operators should attempt to suspend or terminate such applications prior to starting a VSS backup job.

-   **System with no VSS-compatible writers**

    This situation may be relatively rare because most systems that can be backed up by a VSS backup application will have a VSS-enabled version of Windows, which should contain writers.

    However, there are certain circumstances where this problem could arise—for instance, if you are backing up a system without VSS support but the system uses a VSS-enabled networked appliance for its storage.

    Although backing up a system's state from a crash-consistent image is not optimal, it may be sufficient for a computer to reboot to an operational status. In many cases, the computer will recover from any incomplete I/O operations to the file systems and will operate normally.

-   **A requester choosing not to work with the system writers**

    This circumstance would occur if a requester chose to add no writer components, or disabling all writers.

    Performing backups in this way is generally discouraged. Although the shadow-copied volume to back up might be sufficient to restore a system to running, it is not desirable. In fact, given that the writers running on the system are designed with functionality to cooperate with VSS and shadow copies, backing up their data in this way might result in instability.

 

 



