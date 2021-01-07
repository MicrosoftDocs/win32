---
description: Providers manage running volumes and create the shadow copies of them on demand.
ms.assetid: '4e6b46b0-df9e-4458-b0ac-e237d7656337'
title: Providers
ms.topic: article
ms.date: 05/31/2018
---

# Providers

[*Providers*](vssgloss-p.md) manage running volumes and create the shadow copies of them on demand.

In response to a request from a requester, a provider generates COM events to signal applications of a coming shadow copy, then creates and maintains that copy until it is no longer needed.

While a shadow copy is in existence, the provider creates an environment where there are effectively two independent copies of any volume that has been shadow copied: one the running disk being used and updated as normal, the other a copy that is disk fixed and stable for backup.

While a default provider is supplied as part of Windows, other vendors are free to supply their own implementations that are optimized for their own storage hardware and software offerings.

From the point of view of an end-user or backup/restore application developer, all providers will have the same interface (see [Selecting Providers](selecting-providers.md)).

All providers must be able to do the following:

-   Intercept I/O requests between the file system and the underlying mass storage system.
-   Capture and retrieve the status of a volume at the time of shadow copy, maintaining a "point in time" view of the files on the disk with no partial I/O operations reflected in its state.
-   Use this "point in time" view to expose (minimally to VSS-enabled applications) a virtual volume containing the shadow copied data.

Depending on how this is done, a provider can be one of three types:

-   [System Provider](#system-provider)
-   [Software Providers](#software-providers)
-   [Hardware Providers](#hardware-providers)

## System Provider

One shadow copy provider, the [*system provider*](vssgloss-s.md), is supplied as a default part of a Windows operating system installation. Currently, the system provider is a particular instance of a software provider. However, this may change in the future.

To maintain a "point in time" view of a volume contained in the shadow copy, the system provider uses a copy-on-write technique. Copies of the sectors on disk that have been modified (called "diffs") since the beginning of the shadow copy creation are stored in a shadow copy storage area.

Therefore, the system provider can expose the live volume, which can be written to and read from normally, and apply the "diffs" to the live volume's data to effectively expose the frozen data of the shadow copy.

For the system provider, the shadow copy storage area must be on an NTFS volume. The volume to be shadow copied does not need to be an NTFS volume, but at least one volume mounted on the system must be an NTFS volume.

## Software Providers

Software shadow copy providers intercept and process I/O requests in a software layer between the file system and the volume manager software. These providers are implemented as a user-mode DLL component and at least one kernel-mode device driver, typically (but not necessarily) a storage filter driver. The work of creating these shadow copies is done in software.

A software shadow copy provider must maintain a "point-in-time" view of a volume by having access to a set of files that can be used to accurately re-create volume status prior to the shadow copy. An example of this is the copy-on-write technique of the system provider.

However, VSS places no restrictions on what technique that software providers use to create and maintain shadow copies, and third-party vendors are free to implement their software providers as they see fit.

In addition, VSS provides support for much of the functionality of software shadow copy providers, such as defining the point-in-time, data synchronization and flushing, providing a common interface for backup applications, and management of the shadow copy.

A software provider will, by definition, be applicable to a wider range of storage platforms than a hardware provider, and should be able to work with basic disks or logical volumes equally well. This generality sacrifices the performance that may be available by implementing shadow copies in hardware and does not make use of any vendor-specific volume capture or file mirroring features.

## Hardware Providers

Hardware shadow copy providers intercept I/O requests from the file system at the hardware level by working in conjunction with a hardware storage adapter or controller. The work of creating the shadow copy is performed by a host adapter, storage appliance, or RAID controller outside of the operating system.

These providers are implemented as a user-mode DLL component communicating with the hardware that will expose the shadow copy data: therefore, hardware shadow copy providers may need to call or create other kernel-mode components.

Hardware providers expose to VSS shadow copies of entire disks or logical units (LUNs). Requesters still deal with shadow copies of volumes; all the volume-to-disk mapping is handled internally by VSS. Shadow copies created by hardware providers of volumes that reside on dynamic disks have a specific requirement:  They cannot be imported onto the same system. They must be created transportable and imported on a second system.

While a hardware shadow copy provider makes use of VSS functionality that defines the point in time, allows data synchronization, manages the shadow copy, and provides a common interface with backup applications, VSS does not specify the underlying mechanism by which the hardware provider produces and maintains shadow copies.

 

 



