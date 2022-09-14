---
title: Tape Backup
description: A tape volume consists of a recording medium and its physical carrier. Every tape volume has one or more partitions. Partitions are typically divided into sections by filemarks or setmarks. There are three types of filemarks.
ms.assetid: 2057e6e4-b674-4151-b3b6-bde5d87d10c1
keywords:
- backup Backup , tape
- tape backup Backup
ms.topic: article
ms.date: 05/31/2018
---

# Tape Backup

A *tape volume* consists of a recording medium and its physical carrier. The entire length of tape in a volume is not available for recording data. Short sections at the beginning and the end of the tape are reserved for attaching the tape to the hubs in the carrier. The first position on the tape where data can be recorded is the called the *beginning-of-medium marker*, and the last position is called the *end-of-medium marker*.

Every tape volume has one or more partitions. A partition is a portion of the volume, containing its own beginning and ending points, that does not overlap with any other portion of the volume. Each partition has three predefined positions. The first position in a partition where you can record data is called the *beginning-of-partition marker*, and the last is called *end-of-partition marker*. The *early-warning marker* is located immediately before the end-of-partition marker. The early-warning position notifies tape applications to transfer buffered data to the tape before reaching the end-of-partition marker.

The area between a partition's beginning and ending points is typically divided into sections by *filemarks* or *setmarks*. Filemarks and setmarks are special recorded elements that do not contain user data; they simply divide the partition into smaller areas to provide an address scheme. Filemarks and setmarks serve similar purposes, but setmarks provide faster positioning on high-capacity tape drives.

Typically, tape devices support filemarks and setmarks. Support of both enables tape data to be formatted such that setmarks separate data from different disk volumes and filemarks separate data from individual files on a disk volume.

Another recorded element that denotes locations on the tape is an *erase gap*, an area of erased tape or a pattern that the device does not recognize as a mark or as user data.

There are three types of filemarks. A *short filemark* contains a short erase gap that cannot be overwritten unless the write operation is performed from the beginning of the partition or from an earlier long filemark. A *long filemark* contains a long erase gap that enables an application to position the tape at the beginning of the filemark and to overwrite the filemark and the erase gap. A *normal filemark* does not contain an erase gap. Tape devices that use filemarks support either short and long filemarks or normal filemarks, but not all three.

The area on a partition between setmarks or filemarks is available for recording data. A unit of data written to or read from a tape is referred to as a block.

For more information, see the following topics:

-   [Tape Initialization](tape-initialization.md)
-   [Tape Input and Output](tape-input-and-output.md)
-   [Creating a Backup Application](creating-a-backup-application.md)
-   [Backing Up and Restoring Hard Links](backing-up-and-restoring-hard-links.md)

 

 




