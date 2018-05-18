---
title: ClusResGroup.Online method
description: Brings a group \ 32; online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f4861817-a2f6-4b1a-b50c-f3e9119234cd'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Online method Failover Cluster", "Online method Failover Cluster , ClusResGroup class", "ClusResGroup class Failover Cluster , Online method"]
topic_type:
- apiref
api_name:
- ClusResGroup.Online
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroup.Online method

\[The **Online** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Brings a [group](groups.md) [*online*](o-gly.md#-wolf-online-gly).

## Syntax


```VB
ClusResGroup.Online( _
  ByVal varTimeout, _
  [ ByVal objNode ] _
)
```



## Parameters

<dl> <dt>

*varTimeout* 
</dt> <dd>

A **Variant** that specifies how long (in seconds) the method should wait for the group to come online before setting *varPending* to **TRUE** and returning.

</dd> <dt>

*objNode* \[optional\]
</dt> <dd>

Optional [**ClusNode**](clusnode-object.md) object specifying the node on which the group should be brought online. If no node is specified, the **Online** method brings the group online on the best possible node.

</dd> </dl>

## Return value

A **Variant** set to **TRUE** if the request is still pending.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**Online**](online.md)
</dt> </dl>

 

 





