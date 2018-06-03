---
title: CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME control code
description: The CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME \ 32;control code TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86c606fc-0baa-460d-ac15-977cc5e55d00
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_NETNAME_VALIDATE_NETNAME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_NETNAME_VALIDATE_NETNAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME control code

The CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME [control code](about-control-codes.md) TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) callback function.


```C++
ClusterResourceTypeControl( hCluster,                   // cluster handle
                            lpszResTypeName,            // resource type name
                            hHostNode,                  // optional host node
                            CLUSCTL_RESOURCE_TYPE_NETNAME_VALIDATE_NETNAME,
                            lpInBuffer,                 // input buffer: netname
                            cbInBufferSize,             // input buffer size
                            NULL,                       // output buffer (not used)
                            0,                          // allocated buffer size (not used)
                            NULL );                     // size of returned data (not used)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) or [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a null-terminated Unicode string containing a DNS label or NetBIOS computer name.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME (0x02000235) as follows.



| Component                 | Bit location     | Value                                             |
|---------------------------|------------------|---------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                         |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_VALIDATE\_NETNAME** (0x235)<br/>   |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 





