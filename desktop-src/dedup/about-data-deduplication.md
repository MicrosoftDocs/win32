---
title: About Data Deduplication
description: Data deduplication finds and removes duplication within data on a volume while ensuring that the data remains correct and complete.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5E80486C-072A-4AC1-84C1-2BFEECACBCB4
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Data Deduplication API Data Deduplication API , about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# About Data Deduplication

Data deduplication finds and removes duplication within data on a volume while ensuring that the data remains correct and complete. This makes it possible to store more file data in less space on the volume.

-   [What Data Deduplication Does](#what-data-deduplication-does)
-   [Requirements for Data Deduplication](#requirements-for-data-deduplication)
-   [Best Practices for Data Deduplication](#best-practices-for-data-deduplication)

## What Data Deduplication Does

Data deduplication optimizes the file data on the volume by performing the following steps:

1.  Segment the data in each file into small variable-sized chunks.
2.  Identify duplicate chunks.
3.  Maintain a single copy of each chunk.
4.  Compress the chunks.
5.  Replace redundant copies of each chunk with a reference to a single copy.
6.  Replace each file with a reparse point containing references to its data chunks.

After a volume is data deduplication-enabled and optimized, it contains the following:

-   Unoptimized files that are not in policy (files that are skipped over by data deduplication)
-   Optimized files (stored as reparse points)
-   Chunk store (the optimized file data, stored as chunks packed into container files)
-   Additional free space (because the optimized files and chunk store occupy much less space than they did before they were optimized)

When new files are added to the volume, they are not optimized right away. Only files that have not been changed for a minimum amount of time are optimized. (This minimum amount of time is set by user-configurable policy.)

The chunk store consists of one or more chunk store container files. New chunks are appended to the current chunk store container. When its size reaches about 1 GB, that container file is sealed and a new container file is created.

When an optimized file is deleted from the data deduplication-enabled volume, its reparse point is deleted, but its data chunks are not immediately deleted from the chunk store. The data deduplication feature's garbage collection job reclaims the unreferenced chunks.

## Requirements for Data Deduplication

Data deduplication is supported only on the following:

-   Windows Server operating systems beginning with Windows Server 2012
-   NTFS data volumes
-   Cluster shared volume file system (CSVFS) supporting virtual desktop infrastructure (VDI) workloads beginning with Windows Server 2012 R2

Deduplication is not supported on:

-   System or boot volumes
-   Remote mapped or remote mounted drives
-   Cluster shared volume file system (CSVFS) for non-VDI workloads or any workloads on Windows Server 2012
-   Files approaching or larger than 1 TB in size.
-   Volumes approaching or larger than 64 TB in size.

Deduplication skips over the following files:

-   System-state files
-   Encrypted files
-   Files with extended attributes
-   Files whose size is less than 32 KB
-   Reparse points (that are not data deduplication reparse points)

## Best Practices for Data Deduplication

-   The first time deduplication is performed on a volume, a full backup should be performed immediately afterwards.
-   Garbage collection should be performed on the chunk store to remove no-longer-used chunks. This is configured by default to run weekly. After garbage collection, a full backup could be performed on the volume. This is because the garbage collection job may result in many changes in the chunk store, if there were many file deletions since the last garbage collection job ran.

 

 




