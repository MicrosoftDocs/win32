---
title: StatusNetBIOS
description: Contains the returned status code from the last NetBIOS operation that the resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 40B51389-A2FF-4347-8D99-3AC422B993C8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusNetBIOS Failover Cluster , for message queuings
- StatusNetBIOS Failover Cluster
topic_type:
- apiref
api_name:
- StatusNetBIOS
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StatusNetBIOS

Contains the returned status code from the last NetBIOS operation that the resource performed. The following table summarizes the attributes of the **StatusNetBIOS** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0xFFFFFFFF                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_STATUS\_NETBIOS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





