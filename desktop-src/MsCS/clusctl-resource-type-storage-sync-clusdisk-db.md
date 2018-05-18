---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB control code
description: The CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB \ 32;control code TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1c2e6cad-b61b-44cf-ac09-0fb636fb3912'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STORAGE_SYNC_CLUSDISK_DB control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_SYNC_CLUSDISK_DB
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB control code

The CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB [control code](about-control-codes.md) TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.


```C++
ClusterResourceTypeControl( hCluster,                   // cluster handle
                            lpszResTypeName,            // resource type name
                            hHostNode,                  // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_SYNC_CLUSDISK_DB,
                            lpInBuffer,                 // input buffer: TBD
                            cbInBufferSize,             // input buffer size
                            lpOutBuffer,                // output buffer: TBD
                            cbOutBufferSize,            // allocated buffer size
                            lpcbBytesReturned );        // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl></dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values:

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB (0x0240019e) as follows.



| Component                 | Bit location     | Value                                                     |
|---------------------------|------------------|-----------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>         |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                         |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                 |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_STORAGE\_SYNC\_CLUSDISK\_DB** (0x19e)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                  |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





