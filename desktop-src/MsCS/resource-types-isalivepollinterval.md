---
title: IsAlivePollInterval
description: Specifies the recommended interval in milliseconds at which a Resource Monitor should poll resources of the particular resource type to determine if they are operational.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8d0d8dc5-0996-4775-9c19-563f345affbe'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["IsAlivePollInterval Failover Cluster ,resource type", "IsAlivePollInterval Failover Cluster"]
topic_type:
- apiref
api_name:
- IsAlivePollInterval
api_type:
- NA
---

# IsAlivePollInterval

Specifies the recommended interval in milliseconds at which a [Resource Monitor](resource-monitor.md) should poll resources of the particular [resource type](resource-types.md) to determine if they are operational. The polling occurs when the Resource Monitor calls a resource DLL's [**IsAlive**](isalive.md) entry point function. The following table summarizes the attributes of the **IsAlivePollInterval** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 1<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 60000<br/>                                     |



 

## Remarks

The **IsAlivePollInterval** property cannot be zero. It should be set to a value that is as small as possible to cause [failovers](failover.md) to occur in a timely manner.

The [**IsAlivePollInterval**](resources-isalivepollinterval.md) property for resources is also a common resource property.

## Examples

The property value portion of a [property list](property-lists.md) entry for **IsAlivePollInterval** can be set with the following example code:


```C++
DWORD          IsAlivePollIntervalData = 300;
CLUSPROP_DWORD IsAlivePollIntervalValue;

IsAlivePollIntervalValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
IsAlivePollIntervalValue.cbLength  = sizeof(DWORD);
IsAlivePollIntervalValue.dw        = IsAlivePollIntervalData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**IsAlive**](isalive.md)
</dt> <dt>

[**IsAlivePollInterval**](resources-isalivepollinterval.md)
</dt> </dl>

 

 





