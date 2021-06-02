---
title: Distributed File System (DFS) Functions
description: The Distributed File System (DFS) functions provide the ability to logically group shares on multiple servers and to transparently link shares into a single hierarchical namespace. DFS organizes shared resources on a network in a treelike structure.
ms.assetid: a29cde3e-483a-4658-94d4-27398f66abfb
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System (DFS) Functions

The Distributed File System (DFS) functions provide the ability to logically group shares on multiple servers and to transparently link shares into a single hierarchical namespace. DFS organizes shared resources on a network in a treelike structure.

DFS supports *stand-alone* DFS namespaces, those with one host server, and *domain-based* namespaces that have multiple host servers and high availability. The DFS *topology data* for domain-based namespaces is stored in Active Directory. The data includes the DFS root, DFS links, and DFS targets.

Each DFS tree structure has one or more *root targets*. The root target is a host server that runs the DFS service. A DFS tree structure can contain one or more *DFS links*. Each DFS link points to one or more shared folders on the network. You can add, modify and delete DFS links from a DFS namespace. When you remove the last target associated with a DFS link, DFS deletes the DFS link in the DFS namespace. (In earlier documentation, DFS links were called junction points.)

A DFS link can point to one or more shared folders; the folders are called *targets*. When users access a DFS link, the DFS server selects a set of targets based on a client's site information. The client accesses the first available target in the set. This helps to distribute client requests across the possible targets and can provide continued accessibility for users even when some servers fail.

An application can use the DFS functions to:

- Add a DFS link to a DFS root.
- Create or remove stand-alone and domain-based DFS namespaces.
- Add targets to an existing DFS link.
- Remove a DFS link from a DFS root.
- Remove a target from a DFS link.
- View and configure information about DFS roots and links.

For a list of the DFS functions, see [Distributed File System Functions](distributed-file-system-functions.md).

For a list of the DFS structures, see [Distributed File System Structures](distributed-file-system-structures.md).

Targets on computers that are running Microsoft Windows can be published in a DFS namespace. You can also publish any non-Microsoft shares for which client redirectors are available in a DFS namespace. However, unlike a share that is published on a server that is running Windows Server, they cannot host a DFS root or provide referrals to other DFS targets.

DFS uses the Windows Server file replication service to copy changes between replicated targets. Users can modify files stored on one target, and the file replication service propagates the changes to the other designated targets. The service preserves the most recent change to a document or files.
