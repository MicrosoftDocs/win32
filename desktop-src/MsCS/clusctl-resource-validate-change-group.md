---
title: CLUSCTL\_RESOURCE\_VALIDATE\_CHANGE\_GROUP control code
description: TBD. Because the control code is internal, applications cannot use it in a control code function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B325F379-FD23-4911-9831-E85C39F3057E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_VALIDATE_CHANGE_GROUP control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_VALIDATE_CHANGE_GROUP
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_VALIDATE\_CHANGE\_GROUP control code

TBD. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_VALIDATE\_CHANGE\_GROUP (0x01202125) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                      |
|----------------|--------------|------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                      |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit       | 20           | Internal (0x1)<br/>                                  |
| Operation code | 0 23         | **CLCTL\_VALIDATE\_CHANGE\_GROUP** (0x00202125)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





