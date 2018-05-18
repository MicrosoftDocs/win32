---
title: CLUSCTL\_RESOURCE\_NETNAME\_VALIDATE\_VCO control code
description: Confirms whether the security principal of the designated resource can be managed by the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1a0b081a-864e-4d06-97c0-0642cd107af5'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_NETNAME_VALIDATE_VCO control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_VALIDATE_VCO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_NETNAME\_VALIDATE\_VCO control code

Confirms whether the security principal of the designated resource can be managed by the cluster. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.


```C++
ClusterResourceControl( hResource,                             // resource handle
                        NULL,                                  // optional node handle (not used)
                        CLUSCTL_RESOURCE_NETNAME_VALIDATE_VCO, // control code
                        lpInBuffer,                            // input buffer: security principal name
                        nInBufferSize,                         // input buffer size
                        NULL,                                  // output buffer (not used)
                        0,                                     // output buffer size (not used)
                        NULL );                                // returned data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

The name of the resource's security principal.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_VALIDATE\_VCO (0x01000181) as follows:



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)          |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)               |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)            |
| Type bit       | 20           | External (0x0)                            |
| Operation code | 0–23         | **CLCTL\_NETNAME\_VALIDATE\_VCO** (0x181) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)              |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> </dl>

 

 





