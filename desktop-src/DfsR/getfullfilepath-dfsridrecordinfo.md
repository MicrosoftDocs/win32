---
title: GetFullFilePath method of the DfsrIdRecordInfo class
description: Retrieves the complete path to the file or folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5dfd3f09-5bef-434d-9d37-03e468bd410d
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetFullFilePath method Distributed File System Replication
- GetFullFilePath method Distributed File System Replication , DfsrIdRecordInfo class
- DfsrIdRecordInfo class Distributed File System Replication , GetFullFilePath method
topic_type:
- apiref
api_name:
- DfsrIdRecordInfo.GetFullFilePath
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetFullFilePath method of the DfsrIdRecordInfo class

Retrieves the complete path to the file or folder.

## Syntax


```mof
uint32 GetFullFilePath(
  [out] string FullPath
);
```



## Parameters

<dl> <dt>

*FullPath* \[out\]
</dt> <dd>

The full path, if the method succeeds.

</dd> </dl>

## Return value

This method returns one of the [MONITOR\_STATUS return codes](monitor-status-return-codes.md) or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

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

[**DfsrIdRecordInfo**](dfsridrecordinfo.md)
</dt> </dl>

 

 





