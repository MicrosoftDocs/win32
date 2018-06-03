---
title: ClusResGroup.Offline method
description: Takes a group \ 32; offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca4b8bd9-26fb-40f6-86f7-bbd1514fc9ac
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Offline method Failover Cluster
- Offline method Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , Offline method
topic_type:
- apiref
api_name:
- ClusResGroup.Offline
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.Offline method

\[The **Offline** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Takes a [group](groups.md) [*offline*](https://www.bing.com/search?q=*offline*).

## Syntax


```VB
ClusResGroup.Offline( _
  ByVal varTimeout, _
  ByVal varPending _
)
```



## Parameters

<dl> <dt>

*varTimeout* 
</dt> <dd>

A **Variant** that specifies how long (in seconds) the method should wait for the group to come offline before setting *varPending* to **TRUE** and returning.

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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine)
</dt> </dl>

 

 





