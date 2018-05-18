---
title: Resource object
description: The Resource object is an object automatically created by the Generic Script resource DLL for each instance of a scripted resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b9067ff8-af46-4efd-aa54-8f8b9d9d4c39'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Resource object Failover Cluster", "Resource object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- Resource
api_type:
- COM
---

# Resource object

The **Resource** object is an object automatically created by the Generic Script resource DLL for each instance of a scripted [resource](resources.md). Your script can use the methods and properties of the **Resource** object to identify the resource, log information about the resource, and manipulate [private properties](private-properties.md).

-   [Methods](#methods)

### Methods

The **Resource** object has these methods.



| Method                                            | Description                                                                                                 |
|:--------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**AddProperty**](resource-addproperty.md)       | Adds a new [private property](private-properties.md) to the [resource](resources.md) instance.<br/> |
| [**LogInformation**](resource-loginformation.md) | Writes a string to the cluster event log.<br/>                                                        |
| [**Name**](resource-name.md)                     | Returns the name of the resource instance.<br/>                                                       |
| [**RemoveProperty**](resource-removeproperty.md) | Removes a private property from this resource instance.<br/>                                          |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



 

 





