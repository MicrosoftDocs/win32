---
title: CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_GET\_OU\_FOR\_VCO control code
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D60F2375-3874-499E-AB14-C488D8F54A37'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_NETNAME_GET_OU_FOR_VCO control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_NETNAME_GET_OU_FOR_VCO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_GET\_OU\_FOR\_VCO control code

TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( hCluster,                                        // cluster handle
                            lpszResourceTypeName,                            // resource type name
                            hHostNode,                                       // optional host node
                            CLUSCTL_RESOURCE_TYPE_NETNAME_GET_OU_FOR_VCO,    // this control code
                            lpInBuffer,                                      // input buffer
                            nInBufferSize,                                  // input buffer size
                            lpOutBuffer,                                     // output buffer
                            nOutBufferSize,                                 // allocated buffer size
                            lpBytesReturned );                             // actual size of resulting data
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [*ResourceTypeControl*](resourcetypecontrol.md).

<dl> <dt>

*hCluster* \[in\]
</dt> <dd>

A handle to the cluster that contains the resource type identified by the *lpszResourceTypeName* parameter.

</dd> <dt>

*lpszResourceTypeName* \[in\]
</dt> <dd>

A handle to the cluster that contains the resource type identified by the *lpszResourceTypeName* parameter.

</dd> <dt>

*hHostNode* \[in, optional\]
</dt> <dd>

A handle to the node that hosts the affected resource type.

</dd> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to the input buffer that contains the data for the operation, or **NULL** if no information is needed.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpInBuffer* parameter, in bytes.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

A pointer to the output buffer that receives the data retrieved by the operation, or **NULL** if no data will is retrieved.

</dd> <dt>

*nOutBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpOutBuffer* parameter, in bytes.

</dd> <dt>

*lpBytesReturned* \[out, optional\]
</dt> <dd>

The actual size of the data retrieved by the operation, in bytes.

</dd> </dl>

## Return value

When an application uses [CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_GET\_OU\_FOR\_VC](clusctl-cluster-get-clusdb-timestamp.md) as a parameter for [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md), **ClusterResourceTypeControl** returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. This value is returned if the *lpBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the buffer for *lpOutBuffer* was not large enough to hold the data that was returned by the operation.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation was not successful. If the operation required an output buffer, the value specified by *lpBytesReturned* (if not NULL on input) is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_GET\_OU\_FOR\_VCO (0x0240026E) as follows:



| Component                 | Bit location     | Value                                                       |
|---------------------------|------------------|-------------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>           |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                       |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                   |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_NETNAME\_GET\_OU\_FOR\_VCO** (0x40026E)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                     |



 

For more information, see [Control Code Architecture](control-code-architecture.md)

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





