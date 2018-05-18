---
title: ClusResource.TypeName property
description: Returns the resource type name of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3230fa1-67f9-43d5-b06a-03ffc2487a63'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["TypeName property Failover Cluster", "TypeName property Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , TypeName property"]
topic_type:
- apiref
api_name:
- ClusResource.TypeName
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.TypeName property

\[The **TypeName** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [resource type](resource-types.md) name of the [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.TypeName
```



## Property value

**String** that receives the resource type name.

## Remarks

The name returned is the name of the resource type as registered with the [Cluster service](cluster-service.md), for example: "[File Share](file-share.md)" or "[Physical Disk](physical-disk.md)".

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
</dt> <dt>

[**ClusResource.Type**](clusresource-type.md)
</dt> </dl>

 

 





