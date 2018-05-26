---
title: CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS control code
description: Retrieves the token and credentials used to validate a cluster nodes access to a storage account for a Cloud Witness resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CB2F7852-24E9-4460-B794-67DDEE17226F
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLOUD_WITNESS_RESOURCE_TYPE_VALIDATE_CREDENTIALS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLOUD_WITNESS_RESOURCE_TYPE_VALIDATE_CREDENTIALS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS control code

Retrieves the token and credentials used to validate a cluster node's access to a storage account for a [Cloud Witness](cloud-witness.md) resource. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) function.


```C++
ClusterResourceTypeControl( 
  hCluster,                  // cluster handle
  lpszResourceTypeName,      // resource type name
  hHostNode,                 // optional host node
  CLUSCTL_CLOUD_WITNESS_RESOURCE_TYPE_VALIDATE_CREDENTIALS,  // this control code
  lpInBuffer,                // input buffer
  nInBufferSize,             // input buffer size (not used)
  lpOutBuffer,               // output buffer
  cbOutBufferSize,           // allocated buffer size
  lpcbBytesReturned );       // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) or [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

A pointer the retrieved credentials and token.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) returns one of the following values:

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

Implementations of [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS (0x020020E1) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                                                |
|----------------|--------------|--------------------------------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>                                    |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                                               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                                                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                                            |
| Type bit       | 20           | External (0x0)<br/>                                                            |
| Operation code | 0 23         | **CLCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS** (0x20E1)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                                              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





