---
title: CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES control code
description: Retrieves a list of the read/write resource type common property names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca04e4c9-0fc8-48f5-a604-9d726f2bc102
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_ENUM_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_ENUM_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES control code

Retrieves a list of the read/write [resource type](resource-types.md) [common property](common-properties.md) names. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) parameter.


```C++
ClusterResourceTypeControl( 
  hCluster,                                      // cluster handle
  lpszResTypeName,                               // resource type name
  hHostNode,                                     // optional host node
  CLUSCTL_RESOURCE_TYPE_ENUM_COMMON_PROPERTIES,  // this control code
  NULL,                                          // input buffer (not used)
  0,                                             // input buffer size (not used)
  lpOutBuffer,                                   // output buffer: array of strings
  cbOutBufferSize,                               // allocated buffer size (bytes)
  lpcbBytesReturned );                           // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) or [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains an array of null-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains the name of a read/write [common resource type property](resource-type-common-properties.md).

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code in addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

The CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES control code returns only property names, not property values. To retrieve values for common resource type properties, use [CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTIES](clusctl-resource-type-get-common-properties.md) and [CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-type-get-ro-common-properties.md). For more information, see [Getting Information with Control Codes](getting-information-with-control-codes.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>     |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0 23         | **CLCTL\_ENUM\_COMMON\_PROPERTIES** (0x51)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>               |



 

### Resource DLL Support

Use default. Return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) build the list of property names.

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

For more information on the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTIES](clusctl-resource-type-get-common-properties.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-type-get-ro-common-properties.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master)
</dt> <dt>

[**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)
</dt> </dl>

 

 





