---
title: ClusProperty.Length property
description: Size of a cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9e2d1aec-8644-43e9-a079-82cf96e43e4e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Length property Failover Cluster", "Length property Failover Cluster , ClusProperty object", "ClusProperty object Failover Cluster , Length property"]
topic_type:
- apiref
api_name:
- ClusProperty.Length
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperty.Length property

\[The **Length** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the byte size of a [cluster object property](cluster-object-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperty.Length
```



## Property value

**Long** that receives the length, in bytes, of the cluster object property.

## Remarks

The **Length** property corresponds to the **cbLength** member of a [**CLUSPROP\_VALUE**](clusprop-value.md) structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperty is defined as F2E606FE-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**CLUSPROP\_VALUE**](clusprop-value.md)
</dt> </dl>

 

 





