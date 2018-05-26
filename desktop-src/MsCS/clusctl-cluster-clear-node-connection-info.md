---
title: CLUSCTL\_CLUSTER\_CLEAR\_NODE\_CONNECTION\_INFO control code
description: TBD. Applications use this control code as a parameter to the ClusterControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B00D4725-AD1B-415D-A774-1216F0017FFF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_CLEAR_NODE_CONNECTION_INFO control code Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_CLEAR\_NODE\_CONNECTION\_INFO control code

TBD. Applications use this control code as a parameter to the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function.


```C++
ClusterControl( hCluster,                                   // cluster handle
                hHostNode,                                  // optional node handle
                CLUSCTL_CLUSTER_CLEAR_NODE_CONNECTION_INFO, // this control code
                lpInBuffer,                                 // TBD
                cbInBufferSize,                             // input buffer size (bytes)
                lpOutBuffer,                                // TBD
                cbOutBufferSize,                            // output buffer size (bytes)
                lpcbBytesReturned );                        // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) .

<dl> <dt>

*lpInBuffer* \[in\]
</dt> <dd>

TBD.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

TBD.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

TBD.

</dd> <dt>

*cbOutBufferSize* \[in\]
</dt> <dd>

TBD.

</dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The 32 bits of **CLUSCTL\_CLUSTER\_CLEAR\_NODE\_CONNECTION\_INFO** (0x07400307) are defined as follows.



| Component                 | Bit location     | Value                                                          |
|---------------------------|------------------|----------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>                     |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                         |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                              |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                      |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                      |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_CLEAR\_NODE\_CONNECTION\_INFO** (0x400307)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                       |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





