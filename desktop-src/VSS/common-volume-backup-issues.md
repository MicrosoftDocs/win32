---
description: 'Any backup operation that attempts to copy a full and stable image of a system must deal with the following concerns:'
ms.assetid: 8ccdba6d-1097-4c1c-982c-f3d9cbdf06cd
title: Common Volume Backup Issues
ms.topic: article
ms.date: 05/31/2018
---

# Common Volume Backup Issues

Any backup operation that attempts to copy a full and stable image of a system must deal with the following concerns:

-   Inaccessible files during a backup. Running applications frequently need to keep files open in exclusive mode during a backup, preventing backup programs from copying them.
-   Inconsistent file state. Even if an application does not have its files open in exclusive mode, it is possible—because of the finite time needed to open, back up, and close a file—that files copied to storage media may not all reflect the same application state.
-   Need to minimize service interruptions. To ensure file accessibility and the integrity of the data being backed up can require the suspension and/or termination of all running programs during a volume backup. For large disk systems, this could be hours in duration.

    Recently, some storage vendors have attempted to address these problems by providing a volume capture mechanism—a means to capture an image of the files on disk at a given instant in time—using either a copy-on-write or "split mirror" mechanism. However, these solutions entail difficulties of their own:

    -   Incompatible vendor implementations of volume capture. Many providers of RAID devices provide volume capture mechanisms. However, each vendor has its own interface and each must get support from the backup vendors for their volume capture interfaces. This means that backup application vendors must support multiple volume capture implementations, which is undesirable.
    -   Lack of application coordination. Many devices that support a volume capture do not support the coordination of running applications with the freeze of data on disk. For those devices that do, as with the backup applications, each vendor has a different interface.
    -   Limited support for non-RAID devices. Few if any conventional disk vendors provide support for any sort of volume capture in their device drivers. This means that capture mechanisms are limited to certain disk systems, and cannot typically support the backup of system areas.
    -   Need to handle updates to disk during volume capture. Although storage-vendor-provided volume capture mechanisms can freeze the state of data on disk, they do not always interoperate with running applications. This frequently means that data sent to the volume while a storage device is undergoing volume capture may be lost.
    -   Consistent multivolume backup. The storage device executes these volume captures, so there is generally no mechanism for coordinating the timing of the data freeze. This is particularly true if the devices come from separate vendors. Therefore, if several storage volumes are involved in a backup with a volume capture, the time image preserved for each volume may not be consistent.

 

 



