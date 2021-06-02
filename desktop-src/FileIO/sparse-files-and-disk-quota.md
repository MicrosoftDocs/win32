---
description: A sparse file affects user quotas by the nominal size of the file, not the actual allocated amount of disk space.
ms.assetid: 7dbe1133-f5cb-4925-9448-5d40f1c553ff
title: Sparse Files and Disk Quotas
ms.topic: article
ms.date: 05/31/2018
---

# Sparse Files and Disk Quotas

A sparse file affects user quotas by the nominal size of the file, not the actual allocated amount of disk space. That is, creating a 50-MB file with all zero bytes consumes 50 MB of that user's quota. This means that as the user writes data to the sparse file, he need not worry about exceeding his hard quota limit, because he has already been charged for the space. System administrators should not count on the size of a sparse file remaining small. Therefore they should not grant their users hard quota limits that exceed the physical space available, despite the use of sparse files.

 

 



