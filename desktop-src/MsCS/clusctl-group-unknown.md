---
title: CLUSCTL\_GROUP\_UNKNOWN control code
description: Verifies that control codes are being processed on the node where execution of the control is directed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab34ed81-bd84-4940-8571-91402487b983
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_GROUP_UNKNOWN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_UNKNOWN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_GROUP\_UNKNOWN control code

This [control code](about-control-codes.md) verifies that control codes are being processed on the node where execution of the control is directed. Applications use this control code as a [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol) parameter.


```C++
ClusterGroupControl( 
  hGroup,                 // group handle
  hHostNode,              // optional node handle
  CLUSCTL_GROUP_UNKNOWN,  // this control code
  NULL,                   // input buffer (not used)
  0,                      // input buffer size (not used)
  NULL,                   // output buffer (not used)
  0,                      // output buffer size (not used)
  NULL                    // resulting data size (not used)
);
```



## Parameters

For complete parameter descriptions, see [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol). This control code has no parameters associated with it.

<dl></dl>

## Return value

When an application uses CLUSCTL\_GROUP\_UNKNOWN as a parameter for [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol), **ClusterGroupControl** always returns **ERROR\_SUCCESS**.

## Remarks

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_UNKNOWN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>  |
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

[Group Control Codes](group-control-codes.md)
</dt> <dt>

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol)
</dt> </dl>

 

 





