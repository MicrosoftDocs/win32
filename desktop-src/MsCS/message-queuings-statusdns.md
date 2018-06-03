---
title: StatusDNS
description: Contains the returned status code from the last DNS operation that the resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7F01A79F-CA04-4465-8C5B-986218F83C9F
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusDNS Failover Cluster , for message queuings
- StatusDNS Failover Cluster
topic_type:
- apiref
api_name:
- StatusDNS
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StatusDNS

Contains the returned status code from the last [*DNS*](https://www.bing.com/search?q=*DNS*) operation that the resource performed. The following table summarizes the attributes of the **StatusDNS** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0xFFFFFFFF                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_STATUS\_DNS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





