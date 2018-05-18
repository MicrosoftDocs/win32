---
title: CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED control code
description: Enables or disabled Storage Spaces Direct (S2D) on a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '719C570F-B264-4561-9098-7AD2B4E6AC87'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLUSTER_SET_CLUSTER_S2D_ENABLED control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_SET_CLUSTER_S2D_ENABLED
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED control code

Enables or disabled Storage Spaces Direct (S2D) on a cluster.

Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](clustercontrol.md) parameter.


```C++
ClusterControl( hCluster,       // cluster handle
                hHostNode,      // optional node handle
                CLUSCTL_CLUSTER_SET_CLUSTER_S2D_ENABLED, // control code
                lpInBuffer,     // input buffer: property list
                cbInBufferSize, // input buffer size (bytes)
                NULL,           // output buffer (not used)
                0,              // output buffer size (not used)
                NULL );         // output data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](clustercontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pass a pointer to a [property list](property-lists.md) that contains the new values.

</dd> </dl>

## Return value

[**ClusterNodeControl**](clusternodecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The property list is correctly formatted and contains valid data values.

</dd> <dt>

**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dd>

122 (0x7A)

The data area passed to a system call is too small. The actual size of the property list buffer as determined by the [Cluster service](cluster-service.md) is larger than the size specified in the *cbInBufferSize* parameter.

</dd> <dt>

**ERROR\_INVALID\_DATA**
</dt> <dd>

13 (0xD)

The data is invalid. The property list is either formatted incorrectly or contains invalid data, such as an out-of-range value.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The parameter is incorrect. The property list is not formatted correctly.

</dd> <dt>

**RPC\_X\_BAD\_STUB\_DATA**
</dt> <dd>

1783 (0x6F7)

The stub received bad data. The *lpInBuffer* parameter is **NULL**.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED (0x07402D62) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component              | Bit location     | Value                                                       |
|------------------------|------------------|-------------------------------------------------------------|
| Object code<br/> | 24–31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>                  |
| Global bit<br/>  | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                      |
| Modify bit<br/>  | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                           |
| User bit<br/>    | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                   |
| Type bit<br/>    | 20<br/>    | External (0x0)<br/>                                   |
| Operation code         | 0–23             | **CLCTL\_SET\_CLUSTER\_S2D\_ENABLED** (0x402D62)<br/> |
| Access code<br/> | 0–1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**S2DEnabled**](dasmodeenabled.md)
</dt> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





