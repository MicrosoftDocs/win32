---
title: Name
description: Provides the name of the network being managed by a Cluster Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09903bd1-1049-462f-9a11-b680763e3c36
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for network names
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Name

Provides the name of the [network](networks.md) being managed by a [Cluster Name](network-name.md) resource. The following table summarizes the attributes of the **Name** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Remarks

Every cluster has a core Cluster Name resource. The core Network Name resource stores the cluster name in its **Name** private property and is used by the [Cluster service](cluster-service.md) to manage the cluster name. The **Name** private property of the core Cluster Name resource is read-only. Applications must call the [**SetClusterName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_setclustername?branch=master) function to change the cluster name.

The **Name** private property for all other Cluster Name resources is read/write.

Note that the **Name** common property for a Cluster Name resource provides the name of the resource, not the name of the network.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Name** can be set with the following example code.


```C++
WCHAR                szNameData[] = L"myCluster";
CLUSPROP_SZ_DECLARE( NameValue, sizeof( szNameData ) / sizeof( WCHAR ) );

NameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
NameValue.cbLength  = sizeof( szNameData );
StringCbCopy( NameValue.sz, NameValue.cbLength, szNameData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> <dt>

[**SetClusterName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_setclustername?branch=master)
</dt> </dl>

 

 





