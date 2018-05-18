---
title: ClusResource.Offline method
description: Takes the resource offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5c3f0129-a859-4823-bd73-0c7e004507e5'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Offline method Failover Cluster", "Offline method Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , Offline method"]
topic_type:
- apiref
api_name:
- ClusResource.Offline
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.Offline method

\[The **Offline** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Takes the [resource](resources.md) [*offline*](o-gly.md#-wolf-offline-gly).

## Syntax


```VB
ClusResource.Offline( _
  ByVal varTimeout, _
  ByVal varPending _
)
```



## Parameters

<dl> <dt>

*varTimeout* 
</dt> <dd>

A **Variant** that specifies how long (in seconds) the method should wait for the resource to come offline before setting *varPending* to **TRUE** and returning.

</dd> <dt>

*varPending* 
</dt> <dd>

A **Variant** set to **TRUE** if the request is still pending.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





