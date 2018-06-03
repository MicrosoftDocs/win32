---
title: CLUSCTL\_CLUSTER\_UNKNOWN control code
description: Verifies that control codes are being processed on the node where execution of the control is directed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b5467c0-1cf2-4678-8e1a-000ab053d334
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_UNKNOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_UNKNOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_CLUSTER\_UNKNOWN control code

This [control code](about-control-codes.md) verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed. Applications use this control code as a [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol) parameter.


```C++
ClusterControl( 
  hCluster,                 // cluster handle
  hHostNode,                // optional node handle
  CLUSCTL_CLUSTER_UNKNOWN,  // this control code
  NULL,                     // input buffer (not used)
  0,                        // input buffer size (not used)
  NULL,                     // output buffer (not used)
  0,                        // output buffer size (not used)
  NULL                      // resulting data size (not used)
);
```



## Parameters

For complete parameter descriptions, see [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol). This control code has no parameters associated with it.

<dl></dl>

## Return value

When an application uses CLUSCTL\_CLUSTER\_UNKNOWN as a parameter for [**ClusterControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustercontrol), **ClusterControl** always returns **ERROR\_SUCCESS**.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_UNKNOWN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                      |
|---------------------------|------------------|--------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>     |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>      |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>  |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                  |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_UNKNOWN** (0x0)<br/>        |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>    |



 

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

 

 





