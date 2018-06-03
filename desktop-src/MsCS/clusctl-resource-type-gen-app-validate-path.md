---
title: CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH control code
description: Confirms that, for resources of type \ 0034;Generic Application \ 0034;, the server can access the file using the supplied path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5df5d085-56d1-4aa0-9912-f51a800578a7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_GEN_APP_VALIDATE_PATH control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GEN_APP_VALIDATE_PATH
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH control code

Confirms that, for resources of type "Generic Application", the server can access the file using the supplied path. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) callback function.

The CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH, [CLUSCTL\_RESOURCE\_TYPE\_GEN\_SCRIPT\_VALIDATE\_PATH](clusctl-resource-type-gen-script-validate-path.md), and [CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH](clusctl-resource-type-witness-validate-path.md) control codes all share the same value (0x02000231). Any resource DLL that supports two or more of these resource types must handle these carefully.


```C++
ClusterResourceTypeControl( hCluster,                                    // cluster handle
                            lpszResTypeName,                             // resource type name
                            hHostNode,                                   // optional host node
                            CLUSCTL_RESOURCE_TYPE_GEN_APP_VALIDATE_PATH, // this control code
                            lpInBuffer,                                  // input buffer: path
                            cbInBufferSize,                              // input buffer size
                            NULL,                                        // output buffer (not used)
                            0,                                           // allocated buffer size (not used)
                            NULL);                                       // returned data size (not used)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) or [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

A null-terminated Unicode string containing the file path.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) returns one of the following values.

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

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH (0x02000231) as follows.



| Component      | Bit location | Value                                  |
|----------------|--------------|----------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2) |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)            |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)         |
| Type bit       | 20           | External (0x0)                         |
| Operation code | 0 23         | **CLCTL\_VALIDATE\_PATH** (0x231)      |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)           |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

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

 

 





