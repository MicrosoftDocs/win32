---
title: CLUSCTL\_RESOURCE\_FORCE\_QUORUM control code
description: Establishes the set of nodes that are sufficient to force quorum in a majority-of-nodes cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ab957c9c-fe05-424f-80e7-48d74acca6ed'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_FORCE_QUORUM control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_FORCE_QUORUM
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_FORCE\_QUORUM control code

Establishes the set of [nodes](nodes.md) that are sufficient to force quorum in a majority-of-nodes cluster. (For more information, see [Quorum Resource](quorum-resource.md).) Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](resourcecontrol.md) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_FORCE\_QUORUM (0x01500046) as follows.



| Component                 | Bit location     | Value                                          |
|---------------------------|------------------|------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>    |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>         |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>              |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>      |
| Type bit<br/>       | 20<br/>    | Internal (0x1)<br/>                      |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_FORCE\_QUORUM** (0x500046)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>       |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Do not support or use CLUSCTL\_RESOURCE\_FORCE\_QUORUM in your resource DLL.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





