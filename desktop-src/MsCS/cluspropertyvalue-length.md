---
title: ClusPropertyValue.Length property
description: Size of a property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c9c2e4b8-71db-4d28-80ac-f774af573871
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Length property Failover Cluster
- Length property Failover Cluster , ClusPropertyValue object
- ClusPropertyValue object Failover Cluster , Length property
topic_type:
- apiref
api_name:
- ClusPropertyValue.Length
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPropertyValue.Length property

\[The **Length** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the byte size of a [*property value*](p-gly.md#-wolf-property-value-gly).

This property is read-only.

## Syntax


```VB
ClusPropertyValue.Length
```



## Property value

**Long** that receives the length, in bytes, of the property value.

## Remarks

The **Length** property corresponds to the **cbLength** member of a [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusPropertyValue is defined as F2E6071A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusPropertyValue**](cluspropertyvalue-object.md)
</dt> <dt>

[**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master)
</dt> </dl>

 

 





