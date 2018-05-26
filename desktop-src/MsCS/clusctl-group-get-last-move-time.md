---
title: CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME control code
description: Gets the last time a resource group moved.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05B3260B-DF40-4904-9779-C668C627A631
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_GROUP_GET_LAST_MOVE_TIME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_GET_LAST_MOVE_TIME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME control code

Gets the last time a resource group moved. Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustergroupcontrol?branch=master) parameter.


```C++
ClusterGroupControl( 
  hGroup,                                // group handle
  hHostNode,                             // optional node handle
  CLUSCTL_GROUP_GET_LAST_MOVE_TIME,  // this control code
  lpInBuffer,                            // input buffer
  nInBufferSize,                         // input buffer size
  lpOutBuffer,                           // output buffer: array of strings
  cbOutBufferSize,                       // output buffer size (bytes)
  lpcbBytesReturned                      // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustergroupcontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

A values list that contains the retrieved time information.

</dd> </dl>

## Return value

[**ClusterGroupControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustergroupcontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME (0x030002D9) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                      |
|----------------|--------------|------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>                   |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                      |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit       | 20           | External (0x0)<br/>                                  |
| Operation code | 0 23         | **CLCTL\_GROUP\_GET\_LAST\_MOVE\_TIME** (0x2D9)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Group Control Codes](group-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





