---
title: Resource.RemoveProperty method
description: Removes a private property from the resource instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00396d5d-cb41-4f07-9976-966a8cc831aa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveProperty method Failover Cluster
- RemoveProperty method Failover Cluster , Resource class
- Resource class Failover Cluster , RemoveProperty method
topic_type:
- apiref
api_name:
- Resource.RemoveProperty
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource.RemoveProperty method

Removes a [private property](private-properties.md) from the [resource](resources.md) instance.

## Syntax


```VB
Resource.RemoveProperty( _
  ByVal strName _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

String specifying the name of the private property to remove.

</dd> </dl>

## Return value

This method has no return values.

## Remarks

To access the value of any private property, use Resource.&lt;Name of private property&gt;.

## Examples

See the [Scripted Resource Example](scripted-resource-example.md).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[**Resource**](resource-object.md)
</dt> </dl>

 

 





