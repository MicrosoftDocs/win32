---
title: CLUSCTL\_NETWORK\_VALIDATE\_PRIVATE\_PROPERTIES control code
description: Verifies that a property list is properly formatted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9ae91ab3-04c3-4c68-b248-35d0601ad725'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_NETWORK_VALIDATE_PRIVATE_PROPERTIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_NETWORK_VALIDATE_PRIVATE_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_NETWORK\_VALIDATE\_PRIVATE\_PROPERTIES control code

Verifies that a [property list](property-lists.md) is properly formatted. Applications use this [control code](about-control-codes.md) as a [**ClusterNetworkControl**](clusternetworkcontrol.md) parameter.


```C++
ClusterNetworkControl( hNetwork,                                     // network handle
                       hHostNode,                                    // optional host node
                       CLUSCTL_NETWORK_VALIDATE_PRIVATE_PROPERTIES,  // this control code
                       lpInBuffer,                                   // input buffer: property list
                       cbInBufferSize,                               // allocated buffer size (bytes)
                       NULL,                                         // output buffer (not used)
                       0,                                            // output buffer size (not used)
                       NULL );                                       // actual size of resulting data (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNetworkControl**](clusternetworkcontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pass a pointer to a [property list](property-lists.md) containing one or more read/write network [private properties](private-properties.md).

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

The parameter is incorrect.

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

By default, failover clusters do not define any private properties for networks.

ClusAPI.h defines the 32 bits of CLUSCTL\_NETWORK\_VALIDATE\_PRIVATE\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                      |
|---------------------------|------------------|------------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_NETWORK** (0x5)<br/>                 |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                      |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                  |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_VALIDATE\_PRIVATE\_PROPERTIES** (0x89)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Control Codes](network-control-codes.md)
</dt> <dt>

[**ClusterNetworkControl**](clusternetworkcontrol.md)
</dt> </dl>

 

 





