---
title: DHCP Service
description: The DHCP Service resource type supports the Dynamic Host Configuration Protocol (DHCP) Service as a cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0aa3ea17-1a46-46d4-8adf-4b9ce860b013'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,DHCP Service", "DHCP Service resource type Failover Cluster"]
---

# DHCP Service

The DHCP Service [resource type](resource-types.md) supports the Dynamic Host Configuration Protocol (DHCP) Service as a cluster [resource](resources.md). There can be only one instance of a resource of this type in the [*cluster*](c-gly.md#-wolf-cluster-gly) (that is, a cluster can support only one DHCP Service). The following table summarizes the characteristics of the DHCP resource type.



| Characteristic                                        | Description                                                                                            |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | Storage class resource, such as a [Physical Disk](physical-disk.md)                                   |
| Required [private properties](private-properties.md) | [**BackupPath**](the-dhcp-service-backuppath.md), [**DatabasePath**](the-dhcp-service-backuppath.md) |
| Optional private properties                           | None                                                                                                   |



 

 

 




