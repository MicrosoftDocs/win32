---
title: Resource.LogInformation method
description: Writes the specified string to the cluster event log.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 383c0b3f-77ae-44bc-8513-41da6948e331
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LogInformation method Failover Cluster
- LogInformation method Failover Cluster , Resource object
- Resource object Failover Cluster , LogInformation method
topic_type:
- apiref
api_name:
- Resource.LogInformation
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource.LogInformation method

Writes the specified string to the cluster event log.

## Syntax


```VB
Resource.LogInformation( _
  ByVal strMessage _
)
```



## Parameters

<dl> <dt>

*strMessage* 
</dt> <dd>

String describing the event to log.

</dd> </dl>

## Return value

This method has no return values.

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
</dt> <dt>

[View the cluster diagnostic log](https://technet.microsoft.com/library/cc775695.aspx)
</dt> </dl>

 

 





