---
title: CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL control code
description: Deletes a file share on a physical disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0ed70700-d437-4958-852a-03966e4632f9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_FILESERVER_SHARE_DEL control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_FILESERVER_SHARE_DEL
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL control code

\[The CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL control code is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a file share on a physical disk resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function.


```C++
ClusterResourceControl( hResource,                              // cluster handle
                        hHostNode,                             // optional node handle
                        CLUSCTL_RESOURCE_FILESERVER_SHARE_DEL, // control code
                        lpInBuffer,                            // input buffer: file share name
                        nInBufferSize,                         // input buffer size
                        lpOutBuffer,                           // output buffer: (not used)
                        cbOutBufferSize,                       // output buffer size (not used)
                        lpcbBytesReturned );                   // returned data size (not used)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Points to the name of the file share resource to be deleted.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The file share has been deleted.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL (0x01400249) as follows.



| Component      | Bit location | Value                                        |
|----------------|--------------|----------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)             |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                  |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)                       |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)               |
| Type bit       | 20           | External (0x0)                               |
| Operation code | 0 23         | **CLCTL\_FILESERVER\_SHARE\_DEL** (0x400249) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                 |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> </dl>

 

 





