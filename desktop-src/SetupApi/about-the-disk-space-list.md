---
description: The disk-space list enables you to calculate the disk space required to complete the installation operations.
ms.assetid: 6514cbdd-2f23-4ab8-9e34-86d3837503dc
title: About the Disk-Space List
ms.topic: article
ms.date: 05/31/2018
---

# About the Disk-Space List

The disk-space list enables you to calculate the disk space required to complete the installation operations. After you create a disk-space list and add file operations to it, you can query the list to determine the target drives specified by the file operations, and the disk space required on each drive.

By comparing the space required to the space available on the target disks, you can programmatically determine whether sufficient space is available for the current installation.

You can add or remove file operations to the disk-space list and recalculate the disk space required. This functionality enables you to, for example, write a program that interacts with the user, allowing him or her to choose what components they want to install based on the disk space required.

The disk-space list functions automatically check for preexisting copies of files on the target disk. If a previous version of the file is found, the disk-space list functions calculate the additional space required to complete the file operations.

For example, if a copy operation specifies that a 6000-byte file be copied to drive C, and a 2000-byte version of that file already exists on the drive C, the disk space functions would return a required space of 4000 bytes. The additional space is used to replace the older version of the file with the newer version.

The disk-space list functions round file sizes to the disk cluster boundaries.

 

 



