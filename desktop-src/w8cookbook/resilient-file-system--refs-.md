---
title: Resilient file system
description: Resilient file system
ms.assetid: 6E5532F9-64BC-4DD7-9873-3FE4E4DE2DD0
ms.topic: article
ms.date: 05/31/2018
---

# Resilient file system

## Platform

**Servers** – Windows Server 2012 

## Description

Resilient File System (ReFS) is a new local file system. It maximizes data availability, despite errors that would historically cause data loss or downtime. Data integrity ensures that business critical data is protected from errors and available when needed. Its architecture is designed to provide scalability and performance in an era of constantly growing data set sizes and dynamic workloads.

The key features of ReFS are:

-   **Integrity**: ReFS stores data so that it is protected from many of the common errors that can cause data loss. File system metadata is always protected. Optionally, user data can be protected on a per-volume, per-directory, or per-file basis. If corruption occurs, ReFS can detect and, when configured with Storage Spaces, automatically correct the corruption. In the event of a system error, ReFS is designed to recover from that error rapidly, with no loss of user data.
-   **Availability**: ReFS is designed to prioritize the availability of data. With ReFS, if corruption occurs, and it cannot be repaired automatically, the online salvage process is localized to the area of corruption, requiring no volume down-time. In short, if corruption occurs, ReFS will stay online.
-   **Scalability**: ReFS is designed for the data set sizes of today and the data set sizes of tomorrow; it’s optimized for high scalability.
-   **App Compatibility**: To maximize AppCompat, ReFS supports a subset of NTFS features plus Win32 APIs that are widely adopted.
-   **Proactive Error Identification**: The integrity capabilities of ReFS are leveraged by a data integrity scanner (a “scrubber”) that periodically scans the volume, attempts to identify latent corruption, and then proactively triggers a repair of that corrupt data.

## Resources

-   [Building Windows 8 Blog Post – Building the next generation file system for Windows: ReFS](/archive/blogs/b8/building-the-next-generation-file-system-for-windows-refs)
-   [Application Compatibility and ReFS](https://www.microsoft.com/download/en/details.aspx?id=29043)

 

 