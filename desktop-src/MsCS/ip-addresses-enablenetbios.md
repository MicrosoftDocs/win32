---
title: EnableNetBIOS
description: Determines whether a NetBIOS device is created and bound to the IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b767335-edc1-47d7-8dea-13f6df902e5e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- EnableNetBios Failover Cluster ,for IP addresses
- EnableNetBIOS Failover Cluster
topic_type:
- apiref
api_name:
- EnableNetBIOS
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableNetBIOS

Determines whether a NetBIOS device is created and bound to the [IP address](ip-address.md). The following table summarizes the attributes of the **EnableNetBIOS** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | 2                                         |
| Default   | **TRUE** (1)                              |



 

## Remarks

The **EnableNetBIOS** property can be set to one of the following values.



| Value         | Description                                                            |
|---------------|------------------------------------------------------------------------|
| **TRUE** (1)  | Creates a NetBIOS device and binds it to the IP address.               |
| **FALSE** (0) | Does not create a NetBIOS device.                                      |
| 2             | retrieves and uses the NetBIOS settings that are specified on the NIC. |



 

Setting **EnableNetBIOS** to **TRUE** allows NetBIOS applications to use the IP Address resource.

There is a limit of 64 NetBIOS devices in the [*cluster*](https://www.bing.com/search?q=*cluster*). If you have a large number of IP addresses for non-NetBIOS use (for example, a Web server with many virtual roots), set **EnableNetBIOS** to **FALSE** for each IP Address resource.

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableNetBIOS** can be set with the following example code.


```C++
DWORD          EnableNetBIOSData = FALSE;
CLUSPROP_DWORD EnableNetBIOSValue;

EnableNetBIOSValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
EnableNetBIOSValue.cbLength  = sizeof(DWORD);
EnableNetBIOSValue.dw        = EnableNetBIOSData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





