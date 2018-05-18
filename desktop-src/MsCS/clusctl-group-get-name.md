---
title: CLUSCTL\_GROUP\_GET\_NAME control code
description: Retrieves the name of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'af2a4c7b-e720-45a8-a12a-827b819fb9cc'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_GROUP_GET_NAME control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_NAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_GROUP\_GET\_NAME control code

Retrieves the name of a [group](groups.md). Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](clustergroupcontrol.md) parameter.


```C++
ClusterGroupControl( 
  hGroup,                  // group handle
  hHostNode,               // optional node handle
  CLUSCTL_GROUP_GET_NAME,  // this control code
  NULL,                    // input buffer (not used)
  0,                       // input buffer size (not used)
  lpOutBuffer,             // output buffer: string
  cbOutBufferSize,         // output buffer size (bytes)
  lpcbBytesReturned        // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupControl**](clustergroupcontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a NULL-terminated Unicode string containing the name of the group.

</dd> </dl>

## Return value

[**ClusterGroupControl**](clustergroupcontrol.md) returns one of the following values.

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

The name of a group is stored in the [**Name**](groups-name.md) property. To retrieve the Name property along with the other read-only common group properties, use the [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md) control code.

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_NAME as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                     |
|----------------|--------------|-------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>  |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/> |
| Type bit       | 20           | External (0x0)<br/>                 |
| Operation code | 0–23         | **CLCTL\_GET\_NAME** (0x29)<br/>    |
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

[CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md)
</dt> <dt>

[**ClusterGroupControl**](clustergroupcontrol.md)
</dt> <dt>

[**Name**](groups-name.md)
</dt> </dl>

 

 





