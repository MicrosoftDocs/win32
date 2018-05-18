---
title: Changing Object States
description: Initiating state changes allows you to test failover performance and to perform rolling upgrades. The following functions initiate state changes in various objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '97050a69-5cee-4c27-8b66-67bee0c2ab66'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster objects Failover Cluster ,changing states"]
---

# Changing Object States

Initiating state changes allows you to test [failover](failover.md) performance and to perform rolling upgrades. The following functions initiate state changes in various objects.



| Object                                   | Function                                                 |
|------------------------------------------|----------------------------------------------------------|
| bring a [group](groups.md) online       | [**OnlineClusterGroup**](onlineclustergroup.md)         |
| bring a [resource](resources.md) online | [**OnlineClusterResource**](onlineclusterresource.md)   |
| fail a resource                          | [**FailClusterResource**](failclusterresource.md)       |
| pause a [node](nodes.md)                | [**PauseClusterNode**](pauseclusternode.md)             |
| resume a node                            | [**ResumeClusterNode**](resumeclusternode.md)           |
| take a group offline                     | [**OfflineClusterGroup**](offlineclustergroup.md)       |
| take a resource offline                  | [**OfflineClusterResource**](offlineclusterresource.md) |



 

 

 




