---
title: GetIdRecordByPath method of the MSFT\_DfsrIdRecordInfo class
description: Retrieves a specified MSFT\_DfsrIdRecordInfo instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'AD1AE581-ADCB-4652-9F86-7900190ACC3B'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetIdRecordByPath method Distributed File System Replication", "GetIdRecordByPath method Distributed File System Replication , MSFT_DfsrIdRecordInfo class", "MSFT_DfsrIdRecordInfo class Distributed File System Replication , GetIdRecordByPath method"]
topic_type:
- apiref
api_name:
- MSFT_DfsrIdRecordInfo.GetIdRecordByPath
api_location:
- DfsRWmiV2.dll
api_type:
- COM
---

# GetIdRecordByPath method of the MSFT\_DfsrIdRecordInfo class

Retrieves a specified [**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md) instance. This is a static method.

## Syntax


```mof
uint32 GetIdRecordByPath(
  [in]  string                FullPath,
  [out] MSFT_DfsrIdRecordInfo IdRecord
);
```



## Parameters

<dl> <dt>

*FullPath* \[in\]
</dt> <dd>

Specifies the full path to the requested Id record instance.

</dd> <dt>

*IdRecord* \[out\]
</dt> <dd>

On return contains an embedded instance of a [**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md) class .

</dd> </dl>

## Return value

This method returns one of the [MONITOR\_STATUS return codes](monitor-status-return-codes.md) or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md)
</dt> </dl>

 

 





