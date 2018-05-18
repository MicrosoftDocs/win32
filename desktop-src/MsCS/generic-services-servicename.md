---
title: ServiceName
description: Describes the short name of the Generic Service to run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9f7427d0-215a-4a5e-8ee2-5860c94ae1d3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ServiceName Failover Cluster ,for generic services", "ServiceName Failover Cluster"]
topic_type:
- apiref
api_name:
- ServiceName
api_type:
- NA
---

# ServiceName

Describes the short name of the [Generic Service](generic-service.md) to run. The following table summarizes the attributes of the **ServiceName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

For more information about service names, see the function [**CreateService**](https://msdn.microsoft.com/library/windows/desktop/ms682450).

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ServiceName** can be set with the following example code.


```C++
WCHAR szServiceNameData[] = L"MYSVC";
CLUSPROP_SZ_DECLARE( ServiceNameValue, 
                     sizeof(szServiceNameData) / sizeof(WCHAR) );
ServiceNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
ServiceNameValue.cbLength = sizeof( szServiceNameData );
StringCbCopy( ServiceNameValue.sz, 
              ServiceNameValue.cbLength, 
              szServiceNameData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Generic Service Private Properties](generic-service-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> <dt>

[**CreateService**](https://msdn.microsoft.com/library/windows/desktop/ms682450)
</dt> </dl>

 

 





