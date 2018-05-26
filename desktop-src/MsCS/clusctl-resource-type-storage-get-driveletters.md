---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS control code
description: Queries a bitmask of the driver letters that are not in use on the designated node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7960baea-64b5-481b-9237-044ffa7b3b0a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_STORAGE_GET_DRIVELETTERS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_GET_DRIVELETTERS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS control code

Queries a bitmask of the driver letters that are not in use on the designated node. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) callback function.


```C++
ClusterResourceTypeControl( hCluster,                                       // cluster handle
                            lpszResTypeName,                                // resource type name
                            hHostNode,                                      // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_GET_DRIVELETTERS, // this control code
                            lpInBuffer,                                     // input buffer: (not used, but required)
                            cbInBufferSize,                                 // input buffer size: size of lpOutBuffer
                            lpOutBuffer,                                    // output buffer: drive letter bitmask
                            cbOutBufferSize,                                // allocated buffer size
                            lpcbBytesReturned );                            // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) or [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [**CLUS\_STORAGE\_GET\_AVAILABLE\_DRIVELETTERS**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_get_available_driveletters?branch=master) structure indicating the drive letters not in use.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS (0x020001ed) as follows.



| Component      | Bit location | Value                                         |
|----------------|--------------|-----------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)        |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                |
| Type bit       | 20           | External (0x0)                                |
| Operation code | 0 23         | **CLCTL\_STORAGE\_GET\_DRIVELETTERS** (0x1ed) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                  |



 

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

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master)
</dt> <dt>

[**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)
</dt> <dt>

[**CLUS\_STORAGE\_GET\_AVAILABLE\_DRIVELETTERS**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_get_available_driveletters?branch=master)
</dt> </dl>

 

 





