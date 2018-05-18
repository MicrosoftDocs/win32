---
title: AdminExtensions
description: The AdminExtensions property provides the class identifiers (CLSIDs) for the Cluster Administrator extension DLLs that are associated with the resource type. The following table summarizes the attributes of the AdminExtensions property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c7c7ab62-f6ca-4fca-823b-920d82549d05'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["AdminExtensions Failover Cluster ,for resource types", "AdminExtensions Failover Cluster"]
topic_type:
- apiref
api_name:
- AdminExtensions
api_type:
- NA
---

# AdminExtensions

The **AdminExtensions** property provides the class identifiers (**CLSID**s) for the [Cluster Administrator](cluster-administrator.md) extension DLLs that are associated with the [resource type](resource-types.md). The following table summarizes the attributes of the **AdminExtensions** property.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_MULTI\_SZ**](clusprop-multi-sz.md)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

The data value for the **AdminExtensions** property should be set to one or more class identifiers, formatted as a sequence of null-terminated Unicode strings with the entire sequence terminated by an additional **NULL**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **AdminExtensions** can be set with the following example code.


```C++
WCHAR szAdmExData[] = L"{4EC90FB0-D0BB-11CF-B5EF-00A0C90AB505}\0"
                      L"{806EA659-39DC-4BC9-B9DE-B44B671F0236}\0"
                      L"{7904197E-F39E-4458-8848-A56CA675EE4D}\0";

CLUSPROP_SZ_DECLARE( AdmExValue, 
                     sizeof( szAdmExData ) / sizeof( WCHAR ) );

AdmExValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_MULTI_SZ;

AdmExValue.cbLength  = sizeof( szAdmExData );

CopyMemory( (PVOID) AdmExValue.sz, 
            (PVOID) szAdmExData, 
            sizeof( szAdmExData ) );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_MULTI\_SZ**](clusprop-multi-sz.md)
</dt> </dl>

 

 





