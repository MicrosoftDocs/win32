---
title: ClusResource.Online method
description: Brings the resource online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64f63071-b07d-4391-9631-a7a1dae35dc5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Online method Failover Cluster
- Online method Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , Online method
topic_type:
- apiref
api_name:
- ClusResource.Online
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.Online method

\[The **Online** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Brings the [resource](resources.md) [*online*](https://www.bing.com/search?q=*online*).

## Syntax


```VB
ClusResource.Online( _
  ByVal varTimeout, _
  ByVal varPending _
)
```



## Parameters

<dl> <dt>

*varTimeout* 
</dt> <dd>

A **Variant** that specifies how long (in seconds) the method should wait for the resource to come online before setting *varPending* to **TRUE** and returning.

</dd> <dt>

*varPending* 
</dt> <dd>

A **Variant** set to **TRUE** if the request is still pending.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Any resources that the resource [*depends*](https://www.bing.com/search?q=*depends*) on are brought online first.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





