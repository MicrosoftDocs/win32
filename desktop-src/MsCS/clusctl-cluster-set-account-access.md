---
title: CLUSCTL\_CLUSTER\_SET\_ACCOUNT\_ACCESS control code
description: Updates the account access settings for a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '84AED831-0E32-46A8-881C-FDF391BFE8F4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_CLUSTER_SET_ACCOUNT_ACCESS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_SET_ACCOUNT_ACCESS
api_location:
- ClusAPI.h
- MSClus.h
api_type:
- HeaderDef
---

# CLUSCTL\_CLUSTER\_SET\_ACCOUNT\_ACCESS control code

Updates the account access settings for a cluster.


```C++
ClusterControl( hCluster,       // cluster handle
                hHostNode,      // optional node handle
                CLUSCTL_CLUSTER_SET_ACCOUNT_ACCESS, // control code
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

A pointer to a [property list](property-lists.md) that contains the new values for the account access settings.

</dd> </dl>

## Return value

[**ClusterControl**](clustercontrol.md) returns one of the following values.

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

By default, failover clusters do not define any private cluster properties. You can use the [CLUSCTL\_CLUSTER\_SET\_PRIVATE\_PROPERTIES](clusctl-cluster-set-private-properties.md) control code to define private properties for a cluster.

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_SET\_ACCOUNT\_ACCESS (0x074000F2) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>            |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)<br/>                     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0–23         | **CLCTL\_SET\_ACCOUNT\_ACCESS** (0x4000F2)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_WRITE** (0x2)<br/>              |



 

## Requirements



|                                     |                                                                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h; </dt> <dt>MSClus.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterSetAccountAccess**](clustersetaccountaccess.md)
</dt> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





