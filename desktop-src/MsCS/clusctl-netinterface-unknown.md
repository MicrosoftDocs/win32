---
title: CLUSCTL\_NETINTERFACE\_UNKNOWN control code
description: Verifies that the network interface control code verifies that control codes are being processed on the node where execution of the control is directed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12061a66-bc72-4ce2-ba6c-90a8e321d8f3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NETINTERFACE_UNKNOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NETINTERFACE_UNKNOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_NETINTERFACE\_UNKNOWN control code

This [control code](about-control-codes.md) verifies that the network interface control code verifies that control codes are being processed on the node where execution of the control is directed. Applications use this control code as a [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol) parameter.


```C++
ClusterNetInterfaceControl( 
  hNetInterface,                 // network interface handle
  hHostNode,                     // optional host node
  CLUSCTL_NETINTERFACE_UNKNOWN,  // this control code
  NULL,                          // input buffer (not used)
  0,                             // input buffer size (not used)
  NULL,                          // output buffer (not used)
  0,                             // output buffer size (not used)
  NULL                           // actual size of resulting data (not used)
);
```



## Parameters

For complete parameter descriptions, see [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol). This control code has no parameters associated with it.

<dl></dl>

## Return value

When an application uses CLUSCTL\_NETINTERFACE\_UNKNOWN as a parameter for [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol), **ClusterNetInterfaceControl** always returns **ERROR\_SUCCESS**.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_NETINTERFACE\_UNKNOWN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                           |
|----------------|--------------|-------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NETINTERFACE** (0x6)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>          |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>       |
| Type bit       | 20           | External (0x0)<br/>                       |
| Operation code | 0 23         | **CLCTL\_UNKNOWN** (0x0)<br/>             |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>         |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Interface Control Codes](network-interface-control-codes.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol)
</dt> </dl>

 

 





