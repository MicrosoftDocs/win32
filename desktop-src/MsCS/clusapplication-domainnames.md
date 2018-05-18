---
title: ClusApplication.DomainNames property
description: Names of all domains available to a ClusApplication object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '418274eb-a366-4df8-af84-7e4ba8eeed5f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DomainNames property Failover Cluster", "DomainNames property Failover Cluster , ClusApplication object", "ClusApplication object Failover Cluster , DomainNames property"]
topic_type:
- apiref
api_name:
- ClusApplication.DomainNames
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusApplication.DomainNames property

\[The **DomainNames** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the names of all domains available to a [**ClusApplication**](clusapplication-object.md) object.

This property is read-only.

## Syntax


```VB
ClusApplication.DomainNames As DomainNames
```



## Property value

A [**DomainNames**](domainnames-collection.md) collection that contains the available domains.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusApplication is defined as F2E606E6-2631-11D1-89F1-00A0C90D061E<br/>  |



## See also

<dl> <dt>

[**ClusApplication**](clusapplication-object.md)
</dt> <dt>

[**DomainNames**](domainnames-collection.md)
</dt> </dl>

 

 





