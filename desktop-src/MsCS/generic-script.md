---
title: Generic Script
description: The Generic Script resource type works in conjunction with a script that you must provide to manage an application or service as a highly available cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 21f67569-1b5c-4670-8b7b-a312f98ffd10
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,Generic Script
- Generic Script resource type Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Generic Script

The Generic Script [resource type](resource-types.md) works in conjunction with a script that you must provide to manage an application or service as a highly available cluster [resource](resources.md). In effect, the Generic Script resource type allows you to script your own resource DLL. For more information on how to use the Generic Script resource type, see [Using the Generic Script Resource Type](using-the-generic-script-resource-type.md).

The following table summarizes the characteristics of the Generic Script resource type.



| Characteristic                                        | Description    |
|-------------------------------------------------------|----------------|
| Required [dependencies](resource-dependencies.md)    | None           |
| Required [private properties](private-properties.md) | ScriptFilePath |
| Optional private properties                           | None           |



 

 

 




