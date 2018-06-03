---
title: Resource.AddProperty method
description: Adds a new private property to the resource instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 21767030-0102-491a-87dc-0675dac02bfc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddProperty method Failover Cluster
- AddProperty method Failover Cluster , Resource class
- Resource class Failover Cluster , AddProperty method
topic_type:
- apiref
api_name:
- Resource.AddProperty
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource.AddProperty method

Adds a new [private property](private-properties.md) to the [resource](resources.md) instance.

## Syntax


```VB
Resource.AddProperty( _
  ByVal strName _
)
```



## Parameters

<dl> <dt>

*strName* 
</dt> <dd>

String specifying the name of the new private property.

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

 

 





