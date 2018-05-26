---
title: CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT control code
description: Retrieves the add/delete/change notifications for file shares managed by the File Server resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1e2d3482-5e1f-45a3-9f80-c034582d6a75
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_FILESERVER_SHARE_REPORT control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_FILESERVER_SHARE_REPORT
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT control code

\[The CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT control code is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the add/delete/change notifications for file shares managed by the File Server [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                                // cluster handle
                        hHostNode,                                // optional node handle
                        CLUSCTL_RESOURCE_FILESERVER_SHARE_REPORT, // control code
                        lpInBuffer,                               // input buffer (not used)
                        nInBufferSize,                            // input buffer size (not used)
                        lpOutBuffer,                              // output buffer notification list 
                        cbOutBufferSize,                          // output buffer size (bytes)
                        lpcbBytesReturned );                      // returned data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a notification list containing the resource's add/delete/change notifications.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

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

The structure for the notification list comes from the [**FILESHARE\_CHANGE\_LIST**](/windows/previous-versions/ClusAPI/ns-clusapi-_fileshare_change_list?branch=master) structure.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT (0x01400251) as follows:



| Component      | Bit location | Value                                           |
|----------------|--------------|-------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)                |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                     |
| Modify bit     | 22           | **CLUS\_MODIFY** (0x1)                          |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                  |
| Type bit       | 20           | External (0x0)                                  |
| Operation code | 0 23         | **CLCTL\_FILESERVER\_SHARE\_REPORT** (0x400251) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                    |



 

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

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**FILESHARE\_CHANGE\_LIST**](/windows/previous-versions/ClusAPI/ns-clusapi-_fileshare_change_list?branch=master)
</dt> </dl>

 

 





