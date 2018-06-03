---
title: CLUSCTL\_GROUP\_GET\_FAILURE\_INFO control code
description: Retrieves information about a group failure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9E351079-E1E9-4755-BF73-7C665CA8C6EB
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_GROUP_GET_FAILURE_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_FAILURE_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_GROUP\_GET\_FAILURE\_INFO control code

Retrieves information about a group failure. Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol) parameter.


```C++
ClusterGroupControl( 
  hGroup,                                // group handle
  hHostNode,                             // optional node handle
  CLUSCTL_GROUP_GET_FAILURE_INFO,        // this control code
  lpInBuffer,                            // input buffer
  nInBufferSize,                         // input buffer size
  lpOutBuffer,                           // output buffer
  nOutBufferSize,                        // output buffer size
  lpBytesReturned                        // resulting data size
);
```



## Parameters

For complete parameter descriptions, see [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol). The following control code function parameter is specific to this control code.

<dl> <dt>

*hGroup* \[in\]
</dt> <dd>

A handle to the group that failed.

</dd> <dt>

*hHostNode* \[in, optional\]
</dt> <dd>

A handle to the node that is to perform the operation. If **NULL**, the node that contains the group performs the operation.

</dd> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to the input buffer that contains the data for the operation, or **NULL** if no information is needed.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpInBuffer* parameter, in bytes.

</dd> <dt>

*lpOutBuffer* \[out, optional\]
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

When an application uses CLUSCTL\_GROUP\_GET\_FAILURE\_INFO as a parameter for [**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol), **ClusterGroupControl** returns one of the following values:

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

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_FAILURE\_INFO (0x03000019) as follows. For more information, see [Control Code Architecture](control-code-architecture.md).



| Component      | Bit location | Value                                           |
|----------------|--------------|-------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>        |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>          |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>           |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>       |
| Type bit       | 20           | External (0x0)<br/>                       |
| Operation code | 0 23         | **CLCTL\_GET\_FAILURE\_INFO** (0x19)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>         |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Group Control Codes](group-control-codes.md)
</dt> <dt>

[**ClusterGroupControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clustergroupcontrol)
</dt> </dl>

 

 





