---
title: ClusResTypeResources.DeleteItem method
description: Deletes a resource from the cluster and removes it from a ClusResTypeResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'be221cf6-0f27-48b2-bb87-5c7200841cd7'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DeleteItem method Failover Cluster", "DeleteItem method Failover Cluster , ClusResTypeResources class", "ClusResTypeResources class Failover Cluster , DeleteItem method"]
topic_type:
- apiref
api_name:
- ClusResTypeResources.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResTypeResources.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [resource](resources.md) from the [*cluster*](c-gly.md#-wolf-cluster-gly) and removes it from a [**ClusResTypeResources**](clusrestyperesources-collection.md) collection.

## Syntax


```VB
ClusResTypeResources.DeleteItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

Integer that identifies an object in the collection by name or numeric index. Index numbers range from 1 to object.[**Count**](clusrestyperesources-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                 |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>     |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>     |
| IID<br/>                      | IID\_ISClusResTypeResources is defined as F2E60714-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResTypeResources**](clusrestyperesources-collection.md)
</dt> </dl>

 

 





