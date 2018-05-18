---
title: ClusResource.CanResourceBeDependent method
description: Determines if the resource can be dependent on another resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd167192f-4577-49b6-aa1c-1dbd6d2aa98c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CanResourceBeDependent method Failover Cluster", "CanResourceBeDependent method Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , CanResourceBeDependent method"]
topic_type:
- apiref
api_name:
- ClusResource.CanResourceBeDependent
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.CanResourceBeDependent method

\[The **CanResourceBeDependent** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Determines if the [resource](resources.md) can be [*dependent*](d-gly.md#-wolf-dependent-gly) on another resource.

## Syntax


```VB
ClusResource.CanResourceBeDependent( _
  ByVal objResource _
)
```



## Parameters

<dl> <dt>

*objResource* 
</dt> <dd>

The [**ClusResource**](clusresource-object.md) object upon which this resource may or may not depend.

</dd> </dl>

## Return value

A **Variant** set to **TRUE** if this resource can depend on the resource identified by *objResource*; otherwise, it is **FALSE**.

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

 

 





