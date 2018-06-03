---
title: LooksAlivePollInterval
description: Provides the recommended interval in milliseconds at which the Cluster service should poll the resource to determine if it appears operational.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a269118-8512-4fca-a0de-5154914881a7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LooksAlivePollInterval Failover Cluster ,for resources
- LooksAlivePollInterval Failover Cluster
topic_type:
- apiref
api_name:
- LooksAlivePollInterval
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LooksAlivePollInterval

Provides the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll the resource to determine if it appears operational. The polling occurs when the [Resource Monitor](resource-monitor.md) calls the [resource DLL's](resource-dlls.md) [**LooksAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine) entry point function. The following table summarizes the attributes of the **LooksAlivePollInterval** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 10<br/>                                        |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0xFFFFFFFF<br/>                                |



 

## Remarks

If a resource does not set the **LooksAlivePollInterval** property or sets it to 0xFFFFFFFF, the Cluster service uses the [**LooksAlivePollInterval**](resource-types-looksalivepollinterval.md) property for the [resource type](resource-types.md) associated with the [resource](resources.md).

The resource DLL should return an event handle from the [**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine) call that is signaled when a resource fails. For more information, see [Implementing LooksAlive](implementing-looksalive.md) and [Implementing Online](implementing-online.md).

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

[Resource Common Properties](resource-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**LooksAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine)
</dt> <dt>

[**LooksAlivePollInterval**](resource-types-looksalivepollinterval.md)
</dt> <dt>

[**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine)
</dt> </dl>

 

 





