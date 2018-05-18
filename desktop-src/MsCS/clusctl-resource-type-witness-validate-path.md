---
title: CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH control code
description: Confirms that the server can access the file share path for the designated resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27bd42de-1df9-4b8c-be97-c7496c787600'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_WITNESS_VALIDATE_PATH control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_WITNESS_VALIDATE_PATH
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH control code

Confirms that the server can access the file share path for the designated resource type. Applications use this control code as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) function.

The [CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH](clusctl-resource-type-gen-app-validate-path.md), [CLUSCTL\_RESOURCE\_TYPE\_GEN\_SCRIPT\_VALIDATE\_PATH](clusctl-resource-type-gen-script-validate-path.md), and CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH control codes all share the same value (0x02000231). Any resource DLL that supports two or more of these resource types must handle these carefully.


```C++
ClusterResourceTypeControl( hCluster,                                     // cluster handle
                            lpszResTypeName,                              // resource type name
                            hHostNode,                                    // optional host node
                            CLUSCTL_RESOURCE_TYPE_WITNESS_VALIDATE_PATH,  // this control code
                            lpInBuffer,                                   // input buffer: witness path
                            cbInBufferSize,                               // input buffer size (in bytes)
                            NULL,                                         // output buffer (not used)
                            0,                                            // allocated buffer size (not used)
                            0 );                                          // returned data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pointer to a buffer containing the witness path.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH (0x02000231) as follows.



| Component                 | Bit location     | Value                                             |
|---------------------------|------------------|---------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                         |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_VALIDATE\_PATH** (0x231)<br/>      |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

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

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> </dl>

 

 





