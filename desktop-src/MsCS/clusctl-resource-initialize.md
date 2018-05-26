---
title: CLUSCTL\_RESOURCE\_INITIALIZE control code
description: Used by the resource to initialize any state after it has been created for the first time.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 58fe8aa7-a109-46bc-b61a-91b35aae186e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_INITIALIZE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_INITIALIZE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_INITIALIZE control code

Used by the resource to initialize any state after it has been created for the first time. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_INITIALIZE (0x0150004a) as follows.



| Component                 | Bit location     | Value                                       |
|---------------------------|------------------|---------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit<br/>       | 20<br/>    | Internal (0x1)<br/>                   |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_INITIALIZE** (0x50004a)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>    |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Do not support or use CLUSCTL\_RESOURCE\_INITIALIZE in your resource DLL.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> </dl>

 

 





