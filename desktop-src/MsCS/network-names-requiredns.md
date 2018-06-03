---
title: RequireDNS
description: This property is not supported. DNS registration is not required for a Network Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 892487c7-ee96-4598-84ad-e69c37b0f910
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RequireDNS Failover Cluster ,for network names
- RequireDNS Failover Cluster
topic_type:
- apiref
api_name:
- RequireDNS
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequireDNS

\[This property is available for use only in Windows Server 2003.\]

This property is not supported. DNS registration is not required for a [Network Name](network-name.md) resource.

**Windows Server 2003:  **

The **RequireDNS** property determines whether DNS registration is required for a [Network Name](network-name.md) resource. The following table summarizes the attributes of the **RequireDNS** property.



| Attribute            | Value                                                                |
|----------------------|----------------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                   |
| Status<br/>    | Optional<br/>                                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/>                 |
| Minimum<br/>   | 0 (DNS registration not required)<br/>                         |
| Maximum<br/>   | 1 (DNS registration required for resource to come online)<br/> |
| Default<br/>   | 0<br/>                                                         |



 

If **RequireDNS** is set to 1, the [Network Name](network-name.md) resource cannot come online if DNS registration fails.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RequireDNS** can be set with the following example code.


```C++
DWORD          RequireDNSData  = 1;
CLUSPROP_DWORD RequireDNSValue;

RequireDNSValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RequireDNSValue.cbLength  = sizeof(DWORD);
RequireDNSValue.dw        = RequireDNSData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**CreatingDC**](network-names-creatingdc.md)
</dt> <dt>

[**RequireKerberos**](network-names-requirekerberos.md)
</dt> <dt>

[**ResourceData**](network-names-resourcedata.md)
</dt> </dl>

 

 





