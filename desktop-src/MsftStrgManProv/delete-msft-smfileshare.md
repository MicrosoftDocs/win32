---
title: Delete method of the MSFT\_SMFileShare class
description: Deletes a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e48e2ef9-feb1-4111-a1f9-529c21d1898a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Delete method
- Delete method, MSFT_SMFileShare class
- MSFT_SMFileShare class, Delete method
topic_type:
- apiref
api_name:
- MSFT_SMFileShare.Delete
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Delete method of the MSFT\_SMFileShare class

Deletes a file share.

## Syntax


```mof
UInt32 Delete(
  [in]            Boolean               RunAsJob,
  [out]           MSFT_SMJob        REF CreatedStorageJob,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **True**, start a job to delete the file share asynchronously.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMFileShare**](msft-smfileshare.md)
</dt> </dl>

 

 





