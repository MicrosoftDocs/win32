---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS control code
description: Retrieves a property list describing the format of each resource common property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cc4975c4-dec4-44d2-9cd3-f00dcd8720ed
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_GET_COMMON_RESOURCE_PROPERTY_FMTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_COMMON_RESOURCE_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS control code

Retrieves a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter.


```C++
ClusterResourceTypeControl( 
  hCluster,                               // cluster handle
  lpszResTypeName,                        // resource type name
  hHostNode,                              // optional node handle
  CLUSCTL_RESOURCE_TYPE_GET_COMMON_PROPERTY_FMTS,  // this control code
  NULL,                                   // input buffer (not used)
  0,                                      // input buffer size (not used)
  lpOutBuffer,                            // output buffer: property list
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned );                    // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md).

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) returns one of the following values.

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

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                   |
|----------------|--------------|---------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)                  |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                             |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                              |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                          |
| Type bit       | 20           | External (0x1)                                          |
| Operation code | 0 23         | **CLCTL\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS** (0x69) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                            |



 

### Resource DLL Support

Use default. Return **ERROR\_INVALID\_FUNCTION** to let the Resource Monitor create the property list. The Resource Monitor will return a version-appropriate list of common resource type properties.

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

<dl> <dt>

<span id="For_more_information_on_the__________ResourceTypeControl_entry_point_function__see__________Implementing__________ResourceTypeControl."></span><span id="for_more_information_on_the__________resourcetypecontrol_entry_point_function__see__________implementing__________resourcetypecontrol."></span><span id="FOR_MORE_INFORMATION_ON_THE__________RESOURCETYPECONTROL_ENTRY_POINT_FUNCTION__SEE__________IMPLEMENTING__________RESOURCETYPECONTROL."></span>For more information on the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 





