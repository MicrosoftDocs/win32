---
title: MigrationExcludeNetworks
description: Specifies cluster networks that should not be used during a live migration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 30dddf69-0631-4f81-986a-92eeaf1a2b75
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MigrationExcludeNetworks Failover Cluster ,for virtual machines
- MigrationExcludeNetworks Failover Cluster
topic_type:
- apiref
api_name:
- MigrationExcludeNetworks
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MigrationExcludeNetworks

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2:  **

Specifies cluster networks that should not be used during a live migration. The networks are specified by the network ID returned by the [**GetClusterNetworkId**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_id?branch=master) function, separated by semicolons. The following table summarizes the attributes of the **MigrationExcludeNetworks** property.



| Attribute            | Value                                                                     |
|----------------------|---------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                        |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                            |
| Minimum<br/>   | **NULL**<br/>                                                       |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)).<br/> |
| Default<br/>   | **NULL**<br/>                                                       |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MigrationExcludeNetworks** can be set with the following example code.


```C++
WCHAR szMigrationExcludeNetworksData[] = L"aaa54ff1-249b-4b93-b811-d43c2bf1910a;0cc1d307-479c-4ebf-81a6-0c55d4a65cc4";
CLUSPROP_SZ_DECLARE( MigrationExcludeNetworksValue, 
                     sizeof( szMigrationExcludeNetworksData ) / sizeof( WCHAR ) );

MigrationExcludeNetworksValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
MigrationExcludeNetworksValue.cbLength  = sizeof( szMigrationExcludeNetworksData );
StringCbCopy( MigrationExcludeNetworksValue.sz, 
              MigrationExcludeNetworksValue.cbLength, 
              szMigrationExcludeNetworksData );
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

[**GetClusterNetworkId**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_id?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





