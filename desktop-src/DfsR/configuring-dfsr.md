---
title: DFSR Configuration Modes
description: The Distributed File System Replication (DFSR) service supports two configuration modes a WMI-based configuration mode and an Active Directory-based configuration mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed4f9d8e-a643-4026-a3ac-1f7c3d1995c0
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Files , configuring
- configuring Distributed File System Replication Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DFSR Configuration Modes

The Distributed File System Replication (DFSR) service supports two configuration modes: a WMI-based configuration mode and an Active Directory–based configuration mode. The WMI-based configuration is used only for certain server specific configurations.

DFSR caches configuration information stored in Active Directory in XML files. The configuration manager owns and manages the following configuration files:

-   Service-wide configuration.
-   Volume configuration for each volume. Each file contains a list of replicated folders on the volume as well as volume-wide settings.
-   Replication group configuration for every replication group where the computer is a member. Each file contains topology information.

The configuration information stored in the Active Directory is similar to the information stored for the File Replication Service (FRS) in previous versions of Windows.

The DFSR WMI provider provides the following classes for configuring DFSR.



| Class                                                            | Description                                                                                                                                |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**DfsrConfig**](dfsrconfig.md)                                 | Controls service-wide configuration. Primarily provides versioning information and the ability to force DFSR to refresh its configuration. |
| [**DfsrConnectionConfig**](dfsrconnectionconfig.md)             | Represents the directional connection configuration, along with schedule and bandwidth information.                                        |
| [**DfsrLocalMemberConfig**](dfsrlocalmemberconfig.md)           | Represents the membership of the local computer in the group.                                                                              |
| [**DfsrMachineConfig**](dfsrmachineconfig.md)                   | Reads and writes computer-wide configuration information.                                                                                  |
| [**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md) | Controls the configuration of a replicated folder, which is the unit of replication in DFSR.                                               |
| [**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md) | Provides a subset of the full information for replication group members from the Active Directory.                                         |
| [**DfsrVolumeConfig**](dfsrvolumeconfig.md)                     | Enables the user to configure volume-wide parameters such as the minimum size of the NTFS change journal.                                  |



 

 

 




