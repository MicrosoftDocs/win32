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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Changing Object States

Initiating state changes allows you to test [failover](failover.md) performance and to perform rolling upgrades. The following functions initiate state changes in various objects.



| Object                                   | Function                                                 |
|------------------------------------------|----------------------------------------------------------|
| bring a [group](groups.md) online       | [**OnlineClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_online_cluster_group?branch=master)         |
| bring a [resource](resources.md) online | [**OnlineClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_online_cluster_resource?branch=master)   |
| fail a resource                          | [**FailClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_fail_cluster_resource?branch=master)       |
| pause a [node](nodes.md)                | [**PauseClusterNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_pause_cluster_node?branch=master)             |
| resume a node                            | [**ResumeClusterNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node?branch=master)           |
| take a group offline                     | [**OfflineClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group?branch=master)       |
| take a resource offline                  | [**OfflineClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource?branch=master) |



 

 

 




