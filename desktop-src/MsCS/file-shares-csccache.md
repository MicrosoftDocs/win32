---
title: CSCCache
description: Controls client-side caching on a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 52d46b90-41de-4b77-a713-a8928f1e7310
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CSCCache Failover Cluster ,for file shares
- CSCCache Failover Cluster
topic_type:
- apiref
api_name:
- CSCCache
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSCCache

\[The **CSCCache** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Controls client-side caching on a file share. The following table summarizes the attributes of the **CSCCache** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **BYTE**                                                         |
| Access    | Read/write                                                       |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

The **CSCCache** property must be set to one of the following values. For more information see the [**SHARE\_INFO\_1005**](https://msdn.microsoft.com/library/windows/desktop/bb525404) structure.



| Hex  | Enum                          | Meaning                                                           |
|------|-------------------------------|-------------------------------------------------------------------|
| 0x00 | **CSC\_CACHE\_MANUAL\_REINT** | Automatic file-by-file reintegration is not allowed on the share. |
| 0x10 | **CSC\_CACHE\_AUTO\_REINT**   | Automatic file-by-file reintegration is allowed on the share.     |
| 0x20 | **CSC\_CACHE\_VDO**           | Autocaching for programs is enabled.                              |
| 0x30 | **CSC\_CACHE\_NONE**          | No client-side caching is allowed on the share.                   |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **CSCCache** can be set with the following example code.


```C++
BYTE                     CSCData = 0x10; // CSC_CACHE_AUTO_REINT
CLUSPROP_BINARY_DECLARE( CSCValue, sizeof( CSCData ) );

CSCValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_BINARY;
CSCValue.cbLength  = sizeof( CSCData );
memcpy( CSCValue.rgb, CSCData, sizeof( CSCData ) );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> </dl>

 

 





