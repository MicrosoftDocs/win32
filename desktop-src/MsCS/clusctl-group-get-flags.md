---
title: CLUSCTL\_GROUP\_GET\_FLAGS control code
description: Retrieves the flags that are set for a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0daffb5e-f63c-48ef-8fe3-f17aa6181386'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_GROUP_GET_FLAGS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_FLAGS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_GROUP\_GET\_FLAGS control code

Retrieves the flags that are set for a [group](groups.md). Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](clustergroupcontrol.md) parameter.


```C++
ClusterGroupControl( 
  hGroup,                   // group handle
  hHostNode,                // optional node handle
  CLUSCTL_GROUP_GET_FLAGS,  // this control code
  NULL,                     // input buffer (not used)
  0,                        // input buffer size (not used)
  lpOutBuffer,              // output buffer: property list
  cbOutBufferSize,          // output buffer size (bytes)
  lpcbBytesReturned         // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupControl**](clustergroupcontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to **DWORD** bitmask specifying the flags defined for the group.

</dd> </dl>

## Return value

[**ClusterGroupControl**](clustergroupcontrol.md) returns one of the following values:

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

By default, no flags are defined for groups.

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_FLAGS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>  |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/> |
| Type bit       | 20           | External (0x0)<br/>                 |
| Operation code | 0–23         | **CLCTL\_GET\_FLAGS** (0x9)<br/>    |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>   |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Group Control Codes](group-control-codes.md)
</dt> <dt>

[**ClusterGroupControl**](clustergroupcontrol.md)
</dt> </dl>

 

 





