---
title: Message Queuing
description: Supports Message Queuing (MSMQ). Only one MSMQ resource can be in a resource group at one time. The following table summarizes the dependencies and private properties of an MSMQ resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec538fd1-f4d6-4c9a-8267-783dfff75b46
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,Message Queuing
- Message Queuing resource type Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Message Queuing

Supports [Message Queuing (MSMQ)](https://www.bing.com/search?q=Message Queuing (MSMQ)). Only one MSMQ [resource](resources.md) can be in a resource group at one time. The following table summarizes the dependencies and private properties of an MSMQ resource.



| Characteristic                                        | Description                                                                                                                                                             |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | [DTC](distributed-transaction-coordinator.md) resource, [Network Name](network-name.md) resource, [Physical Disk](physical-disk.md) or other storage class resource. |
| Required [private properties](private-properties.md) | None                                                                                                                                                                    |
| Optional private properties                           | None                                                                                                                                                                    |



 

 

 




