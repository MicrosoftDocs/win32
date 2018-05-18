---
title: DhcpEnabled
description: Indicates whether DHCP is enabled for the network interface resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '12bd1359-d2e0-4b00-8df9-78bae5905b22'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DhcpEnabled Failover Cluster , for Network Interface common properties", "DhcpEnabled Failover Cluster"]
topic_type:
- apiref
api_name:
- DhcpEnabled
api_type:
- NA
---

# DhcpEnabled

Indicates whether DHCP is enabled for the network interface resource. The following table summarizes the attributes of the **DhcpEnabled** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>     |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0 (DHCP is disabled)<br/>                      |
| Maximum<br/>   | 1 (DHCP is enabled)<br/>                       |
| Default<br/>   | 0<br/>                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Network Interface Common Properties](network-interface-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





