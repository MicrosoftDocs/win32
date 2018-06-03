---
title: CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN control code
description: Queries the server for whether taking a quorum resource offline or stopping an active node will cause the cluster to lose quorum.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4987c8c1-7f5a-4b4a-8fba-55457922b641
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_CHECK_VOTER_DOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_CHECK_VOTER_DOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN control code

Queries the server for whether taking a quorum resource offline or stopping an active node will cause the cluster to lose quorum. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol) function.


```C++
ClusterControl( hCluster,                         // cluster handle
                hHostNode,                        // optional node handle
                CLUSCTL_CLUSTER_CHECK_VOTER_DOWN, // this control code
                lpInBuffer,                       // input buffer: resource\node ID
                nInBufferSize,                    // input buffer size (bytes)
                lpOutBuffer,                      // output buffer: quorum status
                cbOutBufferSize,                  // output buffer size (bytes)
                lpcbBytesReturned );              // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Points to a **NULL**-terminated Unicode string containing either a resource ID for the specified quorum resource or node ID for the specified active node.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a 32-bit integer containing an enumerator from the [**CLUSTER\_QUORUM\_VALUE**](/previous-versions/windows/desktop/api/msclus/ne-clusapi-cluster_quorum_value) enumeration indicating whether or not quorum will be lost. lpOutBuffer points to one of the following enumeration values.

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

[**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1 (0x1)

Incorrect function. This value is returned if the specified resource pointed to by *lpInBuffer* is not the one currently configured as the quorum resource.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN (0x07000049) as follows:



| Component                 | Bit location     | Value                                           |
|---------------------------|------------------|-------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>      |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>          |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>           |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>       |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                       |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_CHECK\_VOTER\_DOWN** (0x49)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>         |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol)
</dt> </dl>

 

 





