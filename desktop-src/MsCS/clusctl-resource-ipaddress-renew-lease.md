---
title: CLUSCTL\_RESOURCE\_IPADDRESS\_RENEW\_LEASE control code
description: Renews the DHCP based lease of an IP address associated with a designated resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee631871-91d6-4aaa-b071-f18eba3a848a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_IPADDRESS_RENEW_LEASE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_IPADDRESS_RENEW_LEASE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_IPADDRESS\_RENEW\_LEASE control code

Renews the DHCP based lease of an IP address associated with a designated resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                              // resource handle
                        hHostNode,                              // optional node handle
                        CLUSCTL_RESOURCE_IPADDRESS_RENEW_LEASE, // this control code
                        NULL,                                   // lpInBuffer (not used)
                        0,                                      // cbInBufferSize (not used)
                        NULL,                                   // lpOutBuffer (not used)
                        0,                                      // cbOutBufferSize (not used)
                        lpcbBytesReturned );                    // resulting data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl></dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_IPADDRESS\_RENEW\_LEASE (0x014001be) as follows:



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>              |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                        |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_IPADDRESS\_RENEW\_LEASE** (0x4001be)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                 |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_IPADDRESS\_RELEASE\_LEASE](clusctl-resource-ipaddress-release-lease.md)
</dt> </dl>

 

 





