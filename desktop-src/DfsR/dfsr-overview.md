---
title: DFSR Overview
description: The Distributed File System Replication (DFSR) service is a multi-master replication engine used to keep folders synchronized on multiple servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '34a92c66-09a1-4600-9406-d1e36a45f2c7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Distributed File System Replication Files , overview"]
---

# DFSR Overview

The Distributed File System Replication (DFSR) service is a new multi-master replication engine that is used to keep folders synchronized on multiple servers.

Replicating data to multiple servers increases data availability and gives users in remote sites fast, reliable access to files. DFSR uses a new compression algorithm called Remote Differential Compression (RDC). RDC is a "diff over the wire" protocol that can be used to efficiently update files over a limited-bandwidth network. RDC detects insertions, removals, and rearrangements of data in files, enabling DFSR to replicate only the deltas (changes) when files are updated.

The DFSR service uses RPC to communicate between servers. It replicates a folder scope defined by the replicated folder path. The set of computers participating in replication is defined by a configured topology of connections and is called a replication group. Multiple replicated folders can be included in a replication group, with memberships selectively enabling or disabling specific replicated folders. The DFSR service uses WMI to configure server-wide parameters, while global parameters and certain replicated folder-specific parameters are configured using Active Directory. DFSR also uses WMI to expose monitoring information regarding specific objects such as replicated folders and connections.

For more information about the replication process, see [DFS Namespaces and DFS Replication Overview](https://TechNet.Microsoft.Com/library/jj127250.aspx).

 

 




