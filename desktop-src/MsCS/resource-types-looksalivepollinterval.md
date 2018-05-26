---
title: LooksAlivePollInterval
description: Specifies the recommended interval in milliseconds at which the Cluster service should poll resources of the particular resource type to determine if they appear operational.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 87ce50aa-a707-4091-9c65-ffdc314bcc4d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LooksAlivePollInterval Failover Cluster ,for resource types
- LooksAlivePollInterval Failover Cluster
topic_type:
- apiref
api_name:
- LooksAlivePollInterval
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LooksAlivePollInterval

Specifies the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll [resources](resources.md) of the particular [resource type](resource-types.md) to determine if they appear operational. The polling occurs when the [Resource Monitor](resource-monitor.md) calls a resource DLL's [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) entry point function. The following table summarizes the attributes of the **LooksAlivePollInterval** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 1                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 5000                                      |



 

## Remarks

A resource type must have a value for its **LooksAlivePollInterval** property; it is not optional. **LooksAlivePollInterval** should be set to a value that is as small as possible to cause [failovers](failover.md) to occur in a timely manner. Zero is not a valid setting because it prevents the [Resource Monitor](resource-monitor.md) from calling any of the resources' [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) entry point functions.

The [**LooksAlivePollInterval**](resources-looksalivepollinterval.md) property for resources is also a common resource property.

## Examples

The property value portion of a [property list](property-lists.md) entry for **LooksAlivePollInterval** can be set with the following example code:


```C++
DWORD          LooksAlivePollIntervalData = 300;
CLUSPROP_DWORD LooksAlivePollIntervalValue;

LooksAlivePollIntervalValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
LooksAlivePollIntervalValue.cbLength  = sizeof(DWORD);
LooksAlivePollIntervalValue.dw        = LooksAlivePollIntervalData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> <dt>

[**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master)
</dt> <dt>

[**LooksAlivePollInterval**](resources-looksalivepollinterval.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





