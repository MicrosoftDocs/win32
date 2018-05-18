---
title: CLUSCTL\_RESOURCE\_NETNAME\_SET\_PWD\_INFO control code
description: Updates information about the security principal associated with a designated resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '82a466e6-8550-4973-9758-d1d83625817d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_NETNAME_SET_PWD_INFO control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_SET_PWD_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_NETNAME\_SET\_PWD\_INFO control code

Updates information about the security principal associated with a designated resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.


```C++
ClusterResourceControl( hResource,       // resource handle
  NULL,                                  // optional node handle (not used)
  CLUSCTL_RESOURCE_NETNAME_SET_PWD_INFO, // this control code
  lpInBuffer,                            // input buffer: security principal's info
  cbInBufferSize,                        // input buffer size (bytes)
  NULL,                                  // output buffer (not used)
  0,                                     // output buffer size (not used)
  NULL );                                // resulting data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Takes the security principal's information to be updated. This information is structured according to the [**CLUS\_NETNAME\_PWD\_INFO**](clus-netname-pwd-info.md) structure.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_SET\_PWD\_INFO (0x0100017a) as follows:



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)             |
| Type bit       | 20           | External (0x0)                             |
| Operation code | 0–23         | **CLCTL\_NETNAME\_SET\_PWD\_INFO** (0x17a) |
| Access code    | 0–1          | **CLUS\_ACCESS\_WRITE** (0x2)              |



 

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

[**CLUS\_NETNAME\_PWD\_INFO**](clus-netname-pwd-info.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> </dl>

 

 





