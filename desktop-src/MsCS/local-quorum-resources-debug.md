---
title: Debug
description: Specifies whether the cluster is limited to a single node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '57b49616-8ee2-4bd8-b963-87f87a7db5b3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Debug Failover Cluster , for local quorums", "Debug Failover Cluster"]
topic_type:
- apiref
api_name:
- Debug
api_type:
- NA
---

# Debug

\[The **Debug** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Specifies whether the cluster is limited to a single node. The following table summarizes the attributes of the **Debug** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Status<br/>    | Optional<br/>                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 1 (allow multiple nodes)<br/>                  |
| Default<br/>   | 0 (single-node cluster only)<br/>              |



 

## Remarks

By default, local-quorum clusters are limited to a single node: the node that owns the local storage device. Set this property to 1 if you want to create a multi-node cluster using the local storage device as the quorum resource. If there is more than one node in a local-quorum cluster, the **Debug** property cannot be changed back to 0.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Debug** can be set with the following example code.


```C++
WCHAR                szDebugData[] = L"255.255.0.0";
CLUSPROP_SZ_DECLARE( DebugValue, sizeof( szDebugData ) / sizeof( WCHAR ) );

DebugValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DebugValue.cbLength  = sizeof( szDebugData );
StringCbCopy( DebugValue.sz, DebugValue.cbLength, szDebugData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



 

 





