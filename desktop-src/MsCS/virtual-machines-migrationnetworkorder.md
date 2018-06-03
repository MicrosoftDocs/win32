---
title: MigrationNetworkOrder
description: Specifies the order in which the cluster networks are used to create the data connection during a live migration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 78fea0cf-ba32-4932-b269-baed17f976b9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MigrationNetworkOrder Failover Cluster ,for virtual machines
- MigrationNetworkOrder Failover Cluster
topic_type:
- apiref
api_name:
- MigrationNetworkOrder
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MigrationNetworkOrder

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2:  **

Specifies the order in which the cluster networks are used to create the data connection during a live migration. The networks are specified by the network ID returned by the [**GetClusterNetworkId**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_id) function, separated by semicolons. The following table summarizes the attributes of the **MigrationNetworkOrder** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The system will attempt to create the network connection starting with the first network specified by the property, and stop when it could successfully set up the data connection. If the **MigrationNetworkOrder** property is empty, the networks are sorted based on the [**Metric**](networks-metric.md) and [**AutoMetric**](networks-autometric.md) properties of the available networks.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MigrationNetworkOrder** can be set with the following example code.


```C++
WCHAR szMigrationNetworkOrderData[] = L"766ea40b-eb0f-49d5-8d15-a6a9d0ecf920;2a8f9545-88e0-4526-bc96-890fbaeaa359";
CLUSPROP_SZ_DECLARE( MigrationNetworkOrderValue, 
                     sizeof( szMigrationNetworkOrderData ) / sizeof( WCHAR ) );

MigrationNetworkOrderValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
MigrationNetworkOrderValue.cbLength  = sizeof( szMigrationNetworkOrderData );
StringCbCopy( MigrationNetworkOrderValue.sz, 
              MigrationNetworkOrderValue.cbLength, 
              szMigrationNetworkOrderData );
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Virtual Machine Common Properties](virtual-machine-common-properties.md)
</dt> <dt>

[**GetClusterNetworkId**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_id)
</dt> <dt>

[**AutoMetric**](networks-autometric.md)
</dt> <dt>

[**Metric**](networks-metric.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





