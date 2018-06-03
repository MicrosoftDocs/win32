---
title: ForceDownload method of the MSFT\_DfsrConnectionInfo class
description: Forces a download of a specified resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8cf5724f-e45b-47f1-a9cd-238e573c1336
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ForceDownload method Distributed File System Replication
- ForceDownload method Distributed File System Replication , MSFT_DfsrConnectionInfo class
- MSFT_DfsrConnectionInfo class Distributed File System Replication , ForceDownload method
topic_type:
- apiref
api_name:
- MSFT_DfsrConnectionInfo.ForceDownload
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ForceDownload method of the MSFT\_DfsrConnectionInfo class

Forces a download of a specified resource. The connection and bandwidth are controlled by other methods. This method assumes that the connection is on. The unique ID of the resource to be downloaded can be obtained by querying the ID record as described in [Getting the ID Record for a File or Folder](getting-the-id-record-for-a-file-or-folder.md).

## Syntax


```mof
uint32 ForceDownload(
  [in] string ReplicatedFolderGuid,
  [in] string Uid
);
```



## Parameters

<dl> <dt>

*ReplicatedFolderGuid* \[in\]
</dt> <dd>

The unique identifier of the replicated folder to force replication on.

</dd> <dt>

*Uid* \[in\]
</dt> <dd>

The unique ID of the resource to download.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrConnectionInfo**](msft-dfsrconnectioninfo.md)
</dt> </dl>

 

 





