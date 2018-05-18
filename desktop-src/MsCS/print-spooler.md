---
title: Print Spooler
description: The Print Spooler resource type describes a network printer that applications access using a network IP address rather than an individual name. Each group can have only a single Print Spooler resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f94ccac1-5223-4e96-b275-229bddfeb8df'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster , Print Spooler", "Print Spooler resource type Failover Cluster"]
---

# Print Spooler

The Print Spooler [resource type](resource-types.md) describes a network printer that applications access using a network IP address rather than an individual name. Each [group](groups.md) can have only a single Print Spooler [resource](resources.md).

The following table summarizes the characteristics of the Print Spooler resource type.



| Characteristic                                        | Description                                                                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | [Network Name](network-name.md) resource, [Physical Disk](physical-disk.md) or other type of storage class resource |
| Required [private properties](private-properties.md) | [**DefaultSpoolDirectory**](print-spoolers-defaultspooldirectory.md)                                                 |
| Optional private properties                           | [**JobCompletionTimeout**](print-spoolers-jobcompletiontimeout.md)                                                   |



 

 

 




