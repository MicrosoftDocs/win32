---
title: CLUSCTL\_RESOURCE\_NETNAME\_REGISTER\_DNS\_RECORDS control code
description: Instructs the designated resource to re-register its DNS Host records with the DNS server associated with the designated node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 42ecb377-81a7-49f0-8ed4-a50f96af9317
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_NETNAME_REGISTER_DNS_RECORDS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_REGISTER_DNS_RECORDS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_NETNAME\_REGISTER\_DNS\_RECORDS control code

Instructs the designated resource to re-register its DNS Host records with the DNS server associated with the designated node. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                                     // resource handle
                        NULL,                                          // optional node handle (not used)
                        CLUSCTL_RESOURCE_NETNAME_REGISTER_DNS_RECORDS, // this control code
                        NULL,                                          // input buffer (not used)
                        0,                                             // input buffer size (not used)
                        NULL,                                          // output buffer (not used)
                        0,                                             // output buffer size (not used)
                        NULL );                                        // resulting data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*hResource* 
</dt> <dd>

Handle to the resource that needs to re-register its DNS Host records.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_REGISTER\_DNS\_RECORDS (0x01000172) as follows.



| Component                 | Bit location     | Value                                                         |
|---------------------------|------------------|---------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                   |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                        |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                         |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                     |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                     |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_NETNAME\_REGISTER\_DNS\_RECORDS** (0x172)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                      |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 Datacenter with SP1, Windows Server 2008 Enterprise with SP1<br/> |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl>        |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





