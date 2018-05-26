---
title: CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT control code
description: Queries the server for whether evicting the designated configured node from the cluster or changing the cluster quorum configuration will cause the loss of quorum.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e87d5598-01f5-4d33-aa8c-e9c059cb9716
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_CHECK_VOTER_EVICT control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_CHECK_VOTER_EVICT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT control code

Queries the server for whether evicting the designated configured node from the cluster or changing the cluster quorum configuration will cause the loss of quorum. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function.


```C++
ClusterControl( hCluster,                          // cluster handle
                hHostNode,                         // optional node handle
                CLUSCTL_CLUSTER_CHECK_VOTER_EVICT, // this control code
                lpInBuffer,                        // input buffer: resource\node ID
                nInBufferSize,                     // input buffer size (bytes)
                lpOutBuffer,                       // output buffer: quorum status
                cbOutBufferSize,                   // output buffer size (bytes)
                lpcbBytesReturned );               // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Points to a **NULL**-terminated Unicode string containing either a resource ID for the specified quorum resource or node ID for the specified active node.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a 32-bit integer containing an enumerator from the [**CLUSTER\_QUORUM\_VALUE**](/windows/previous-versions/msclus/ne-clusapi-cluster_quorum_value?branch=master) enumeration indicating whether or not quorum will be lost. lpOutBuffer points to one of the following enumeration values.

<dt>

<span id="CLUSTER_QUORUM_MAINTAINED"></span><span id="cluster_quorum_maintained"></span>

<span id="CLUSTER_QUORUM_MAINTAINED"></span><span id="cluster_quorum_maintained"></span>**CLUSTER\_QUORUM\_MAINTAINED** (0)


</dt> <dd>

The quorum will be maintained.

</dd> <dt>

<span id="CLUSTER_QUORUM_LOST"></span><span id="cluster_quorum_lost"></span>

<span id="CLUSTER_QUORUM_LOST"></span><span id="cluster_quorum_lost"></span>**CLUSTER\_QUORUM\_LOST** (1)


</dt> <dd>

The quorum will be lost.

</dd> </dl> </dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT (0x07000045) as follows.



| Component                 | Bit location     | Value                                            |
|---------------------------|------------------|--------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>       |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>           |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>            |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>        |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                        |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_CHECK\_VOTER\_EVICT** (0x45)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>          |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





