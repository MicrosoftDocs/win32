---
title: ClusResource.CommonProperties property
description: Read/write common properties of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '14f80d93-541c-4893-8aa6-7b4ba90ecdea'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CommonProperties property Failover Cluster", "CommonProperties property Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , CommonProperties property"]
topic_type:
- apiref
api_name:
- ClusResource.CommonProperties
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.CommonProperties property

\[The **CommonProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [common properties](common-properties.md) of a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.CommonProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the [read/write](read-write-properties.md) common properties of the resource.

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

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResource.CommonROProperties**](clusresource-commonroproperties.md)
</dt> </dl>

 

 





