---
description: File Replication Service (FRS) Is Deprecated in Windows Server 2008 R2
ms.assetid: 18a03469-737a-4905-9851-f7961c46b867
title: File Replication Service (FRS) Is Deprecated in Windows Server 2008 R2
ms.topic: article
ms.date: 05/31/2018
---

# File Replication Service (FRS) Is Deprecated in Windows Server 2008 R2

## Platform

 **Servers -** Windows Server 2008 R2  

## Feature Impact

 **Severity -** High  
**Frequency -** High  


## Description

In Windows Server 2008 R2, File Replication Service (FRS) cannot be used for replicating Distributed File System (DFS) folders or custom (non-SYSVOL) data. A Windows Server 2008 R2 domain controller can still use FRS to replicate the contents of the SYSVOL share in a domain that uses FRS for replicating the SYSVOL share between domain controllers. However, Windows Server 2008 R2 servers cannot use FRS to replicate the contents of any replica set apart from the SYSVOL share. The DFS Replication service is a replacement for FRS and can be used to replicate the contents of the SYSVOL share, DFS folders as well as other custom (non-SYSVOL) data. Migrate all non-SYSVOL FRS replica sets to DFS Replication. We also highly recommend that you migrate replication of the SYSVOL share from FRS to DFS Replication because DFS Replication is more robust, scalable and has better replication performance than FRS.

## Manifestation

FRS replication of custom data will break irreversibly upon in-place upgrade. The only way to recover from this situation would be to reinstall an older operating system on the server and reinitialize FRS replication. Servers that have been upgraded to Windows Server 2008 R2 are not allowed to participate in existing FRS replication groups.

## Mitigation of Impact

To prevent issues that might occur as a result of these changes, migrate custom FRS replication sets to DFS Replication. The DFS Replication service has many benefits over FRS, including improved management tools, higher performance, and delegated management.

## Links to Other Resources

-   [FRS Overview](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754297(v=ws.11))
-   [Distributed File System Replication: Frequently Asked Questions](/windows-server/storage/dfs-replication/dfsr-faq)
-   [SYSVOL Replication Migration Guide: FRS to DFS Replication](/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr)

 

 
