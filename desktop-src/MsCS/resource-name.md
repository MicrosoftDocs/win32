---
title: Resource Name method
description: Returns the name of the resource instance. Note that you cannot use this method to set the name of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c88352ef-563e-4e85-a455-c541bf09557f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Name method Failover Cluster", "Name method Failover Cluster , Resource interface", "Resource interface Failover Cluster , Name method"]
topic_type:
- apiref
api_name:
- Resource.Name
api_type:
- COM
---

# Resource::Name method

Returns the name of the [resource](resources.md) instance. Note that you cannot use this method to set the name of the resource.

## Syntax


```C++
string Name();
```



## Parameters

This method has no parameters.

## Return value

The name of the resource.

## Remarks

Resource names are not case sensitive. A resource name must be unique within the cluster. The name is set when the resource is created and can be changed using the [**SetClusterResourceName**](setclusterresourcename.md) function.

## Examples

See the [Scripted Resource Example](scripted-resource-example.md).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[**Resource**](resource-object.md)
</dt> </dl>

 

 





