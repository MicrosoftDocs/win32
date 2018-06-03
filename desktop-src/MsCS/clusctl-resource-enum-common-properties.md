---
title: CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES control code
description: Retrieves a list of the read/write resource common property names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e4ed860-e821-4459-94b7-a28b4b419703
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_ENUM_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_ENUM_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES control code

Retrieves a list of the read/write [resource](resources.md) [common property](common-properties.md) names. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_ENUM_COMMON_PROPERTIES,           // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: array of strings
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) or [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains an array of null-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains the name of a read/write [common resource property](resource-common-properties.md).

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

The CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES control code returns only property names, not property values. To retrieve values for common resource properties, use [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md) and [CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md). For more information, see [Getting Information with Control Codes](getting-information-with-control-codes.md).

Do not use the CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)             |
| Type bit       | 20           | External (0x0)                             |
| Operation code | 0 23         | **CLCTL\_ENUM\_COMMON\_PROPERTIES** (0x51) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)               |



 

### Resource DLL Support

Use default. Return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) build the list of property names.

As a general guideline, the Resource Monitor should handle all of the control codes for common properties, while your DLL should handle all control codes for private properties.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





