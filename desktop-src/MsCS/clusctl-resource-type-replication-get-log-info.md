---
title: CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_LOG\_INFO control code
description: Internal. Retrieves log information from a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 87361C2D-BAA4-4058-964D-8466AD875F9B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_REPLICATION_GET_LOG_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_REPLICATION_GET_LOG_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_LOG\_INFO control code

[Internal](internal-control-codes.md). Retrieves log information from a replication group.[Resource DLLs](resource-dlls.md) receive this [control code](about-control-codes.md) through the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, which is called once for every resource type supported by the DLL.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of this control code (0x02002145) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                        |
|----------------|--------------|--------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>            |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                       |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x1)<br/>                        |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                    |
| Type bit       | 20           | Internal (0x1)<br/>                                    |
| Operation code | 0 23         | **CLCTL\_REPLICATION\_GET\_LOG\_INFO** (0x002145)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                      |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





