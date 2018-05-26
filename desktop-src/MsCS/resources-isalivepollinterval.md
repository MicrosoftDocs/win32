---
title: IsAlivePollInterval
description: Provides the recommended interval in milliseconds at which the Cluster service should poll the resource to determine if it is operational.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a422e98-f983-4b5c-ad99-cebd2f583f92
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IsAlivePollIntervalc Failover Cluster ,for resources
- IsAlivePollInterval Failover Cluster
topic_type:
- apiref
api_name:
- IsAlivePollInterval
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IsAlivePollInterval

Provides the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll the resource to determine if it is operational. The polling occurs when the [Resource Monitor](resource-monitor.md) calls the [resource DLL's](resource-dlls.md) [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) entry point function. The following table summarizes the attributes of the **IsAlivePollInterval** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 10<br/>                                        |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 60000 (1 minute)<br/>                          |



 

## Remarks

If a resource does not set the **IsAlivePollInterval** property or sets it to  1, the [Cluster service](cluster-service.md) uses the [**IsAlivePollInterval**](resource-types-isalivepollinterval.md) property for the [resource type](resource-types.md) associated with the resource.

The data value for **IsAlivePollInterval** cannot be zero.

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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master)
</dt> <dt>

[**IsAlivePollInterval**](resource-types-isalivepollinterval.md)
</dt> </dl>

 

 





