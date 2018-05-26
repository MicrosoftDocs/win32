---
title: CLUSCTL\_NODE\_UNKNOWN control code
description: Verifies that control codes are being processed on the node where execution of the control is directed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c52faae4-aadc-4415-8858-d578273a1ecb
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NODE_UNKNOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NODE_UNKNOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_NODE\_UNKNOWN control code

This [control code](about-control-codes.md) verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed. Applications use this control code as a [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master) parameter.


```C++
ClusterNodeControl( 
  hNode,                                             // node handle
  hHostNode,                                         // optional host node
  CLUSCTL_NODE_UNKNOWN,                              // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  NULL,                                              // output buffer (not used)
  0,                                                 // output buffer size (not used)
  NULL );                                            // actual size of resulting data (not used)
```



## Parameters

For complete parameter descriptions, see [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master). This control code has no parameters associated with it.

<dl></dl>

## Return value

When an application uses CLUSCTL\_NODE\_UNKNOWN as a parameter for [**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master), **ClusterNodeControl** always returns **ERROR\_SUCCESS**.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_NODE\_UNKNOWN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NODE** (0x4)<br/>   |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/> |
| Type bit       | 20           | External (0x0)<br/>                 |
| Operation code | 0 23         | **CLCTL\_UNKNOWN** (0x0)<br/>       |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>   |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Node Control Codes](node-control-codes.md)
</dt> <dt>

[**ClusterNodeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternodecontrol?branch=master)
</dt> </dl>

 

 





