---
title: Changing Object States
description: Initiating state changes allows you to test failover performance and to perform rolling upgrades. The following functions initiate state changes in various objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 97050a69-5cee-4c27-8b66-67bee0c2ab66
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,changing states
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Changing Object States

Initiating state changes allows you to test [failover](failover.md) performance and to perform rolling upgrades. The following functions initiate state changes in various objects.



| Object                                   | Function                                                 |
|------------------------------------------|----------------------------------------------------------|
| bring a [group](groups.md) online       | [**OnlineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_group)         |
| bring a [resource](resources.md) online | [**OnlineClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_resource)   |
| fail a resource                          | [**FailClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_fail_cluster_resource)       |
| pause a [node](nodes.md)                | [**PauseClusterNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node)             |
| resume a node                            | [**ResumeClusterNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node)           |
| take a group offline                     | [**OfflineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group)       |
| take a resource offline                  | [**OfflineClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource) |



 

 

 




