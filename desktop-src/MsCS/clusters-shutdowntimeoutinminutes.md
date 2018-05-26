---
title: ShutdownTimeoutInMinutes
description: Specifies how many minutes after a system shutdown is initiated that the failover cluster service will wait for resources to go offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eb295867-475b-4fd9-bd1d-343118565f48
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ShutdownTimeoutInMinutes Failover Cluster ,for clusters
- ShutdownTimeoutInMinutes Failover Cluster ,for failover clusters
- ShutdownTimeoutInMinutes Failover Cluster
topic_type:
- apiref
api_name:
- ShutdownTimeoutInMinutes
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ShutdownTimeoutInMinutes

Specifies how many minutes after a system shutdown is initiated that the failover cluster service will wait for resources to go offline. The following table summarizes the attributes of the **ShutdownTimeoutInMinutes** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 1440<br/>                                      |
| Default<br/>   | 20<br/>                                        |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_SHUTDOWN\_TIMEOUT\_MINUTES**.

This property is also exposed as the **ShutdownTimeoutInMinutes** property of the [**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422) WMI class.

> [!Note]  
> If the Hyper-V role is installed, the default time-out value is calculated based on the size of physical memory, using a ratio of 100 minutes / 64 GB. The minimum computed value is 20 minutes.

 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShutdownTimeoutInMinutes** can be set with the following example code:


```C++
CLUSPROP_DWORD ShutdownTimeoutInMinutesValue;

ShutdownTimeoutInMinutesValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ShutdownTimeoutInMinutesValue.cbLength  = sizeof(DWORD);
ShutdownTimeoutInMinutesValue.dw        = 15;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422)
</dt> </dl>

 

 





