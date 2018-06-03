---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT control code
description: Allows a quorum resource DLL to specify a new arbitration timeout value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c049905-64b4-4e0a-8b57-77b88c0057a5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_GET_ARB_TIMEOUT control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_ARB_TIMEOUT
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT control code

Allows a [quorum resource](quorum-resource.md) DLL to specify a new arbitration timeout value. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) parameter.


```C++
ClusterResourceTypeControl( hCluster,                              // cluster handle
                            lpszResTypeName,                       // resource type name
                            hHostNode,                             // optional host node
                            CLUSCTL_RESOURCE_TYPE_GET_ARB_TIMEOUT, // this control code
                            NULL,                                  // input buffer (not used)
                            0,                                     // input buffer size (not used)
                            lpOutBuffer,                           // output buffer: DWORD 
                            cbOutBufferSize,                       // allocated buffer size (bytes)
                            lpcbBytesReturned );                   // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) or [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains a **DWORD** specifying the arbitration timeout interval in seconds. If the quorum resource arbitration fails to occur within this time interval, the quorum resource fails. The default value is 60 seconds.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

Although defined as an external control code, CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT behaves more like an internal control code. Applications can retrieve the arbitration timeout value but this information is not very useful.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT as follows.



| Component                 | Bit location     | Value                                             |
|---------------------------|------------------|---------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                         |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_ARB\_TIMEOUT** (0x15)<br/>    |
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

[CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT](clusctl-resource-type-get-arb-timeout.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 





