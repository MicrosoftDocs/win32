---
title: ForceDownload method of the DfsrConnectionInfo class
description: Forces a download of a specified resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3b75928-3e64-4161-83d3-f300baa6b278
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ForceDownload method Distributed File System Replication
- ForceDownload method Distributed File System Replication , DfsrConnectionInfo class
- DfsrConnectionInfo class Distributed File System Replication , ForceDownload method
topic_type:
- apiref
api_name:
- DfsrConnectionInfo.ForceDownload
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ForceDownload method of the DfsrConnectionInfo class

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrConnectionInfo**](dfsrconnectioninfo.md)
</dt> </dl>

 

 





