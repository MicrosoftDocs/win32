---
title: Failover Cluster Administrator
description: Administrators use cluster management applications to configure, control, and monitor clusters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d89c4b8-0554-4672-9e06-2ce7c5d15d5f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- administration interfaces Failover Cluster ,Failover Cluster Administrator
- Failover Cluster Administrator Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Administrator

\[Support for the Failover Cluster Administrator was removed in Windows Server 2008.\]

Administrators use [cluster management applications](cluster-management-applications.md) to configure, control, and monitor [*clusters*](c-gly.md#-wolf-cluster-gly). Failover Cluster Administrator is an example of a cluster management application. Any system, regardless of whether it is a cluster [node](nodes.md), can install Failover Cluster Administrator.

Failover Cluster Administrator allows administrators to manage cluster [objects](cluster-objects.md), establish [groups](groups.md), initiate [*failover*](f-gly.md#-wolf-failover-gly), handle maintenance, and monitor cluster activity through a convenient graphical interface. Third-party developers can extend the functionality of Failover Cluster Administrator by implementing [extension DLLs](cluster-administrator-extension-dlls.md).

**Note**  When you use Failover Cluster Administrator to create a new File Share resource, permissions for the Everyone group for that file share are set to read-only by default. You can change the default permissions by modifying the [Security Property for File Shares](file-shares-security.md).

For more information on Failover Cluster Administrator, see the documentation included with the operating system.

 

 




