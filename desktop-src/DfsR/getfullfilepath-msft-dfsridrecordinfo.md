---
title: GetFullFilePath method of the MSFT\_DfsrIdRecordInfo class
description: Retrieves the full path to the file or folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb07e7da-fee8-4442-8156-843852e18969
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetFullFilePath method Distributed File System Replication
- GetFullFilePath method Distributed File System Replication , MSFT_DfsrIdRecordInfo class
- MSFT_DfsrIdRecordInfo class Distributed File System Replication , GetFullFilePath method
topic_type:
- apiref
api_name:
- MSFT_DfsrIdRecordInfo.GetFullFilePath
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetFullFilePath method of the MSFT\_DfsrIdRecordInfo class

Retrieves the full path to the file or folder.

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
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md)
</dt> </dl>

 

 





