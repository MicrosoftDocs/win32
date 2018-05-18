---
title: SharePath
description: Path to the File Share Witness.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e86fd3a3-591e-4d6d-868e-1a1779ca15d4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["SharePath Failover Cluster , for File Share Quorum Witness Resource private properties", "SharePath Failover Cluster"]
topic_type:
- apiref
api_name:
- SharePath
api_type:
- NA
---

# SharePath

Specifies the path to the File Share Witness. The following table summarizes the attributes of the **SharePath** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | TBD                                                              |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_FSWITNESS\_SHARE\_PATH**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Quorum Witness Resource Private Properties](file-share-quorum-witness-resource-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> </dl>

 

 





