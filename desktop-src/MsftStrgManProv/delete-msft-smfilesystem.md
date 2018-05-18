---
title: Delete method of the MSFT\_SMFileSystem class
description: Deletes the file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b53ada50-2bea-4db4-9e5d-b78466f78e12'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Delete method", "Delete method, MSFT_SMFileSystem class", "MSFT_SMFileSystem class, Delete method"]
topic_type:
- apiref
api_name:
- MSFT_SMFileSystem.Delete
api_location:
- StorageService.dll
api_type:
- COM
---

# Delete method of the MSFT\_SMFileSystem class

Deletes the file system.

## Syntax


```mof
UInt32 Delete(
  [in]            Boolean               RunAsJob,
  [out]           MSFT_SMJob        REF CreatedStorageJob,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RunAsJob* \[in\]
</dt> <dd>

**True** to start a job that deletes the file system asynchronously; otherwise, **False**.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance that was created by **RunAsJob**. If the job is completed, this property can be set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains the results of calling this method.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMFileSystem**](msft-smfilesystem.md)
</dt> </dl>

 

 





