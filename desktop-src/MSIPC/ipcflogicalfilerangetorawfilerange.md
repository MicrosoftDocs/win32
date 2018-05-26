---
title: IpcfLogicalFileRangeToRawFileRange function
description: Gets the raw file range for the given logical file range of the protected file content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2380bb68-07c9-4ea2-be64-78ca56b8f077
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfLogicalFileRangeToRawFileRange function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfLogicalFileRangeToRawFileRange
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfLogicalFileRangeToRawFileRange function

Gets the raw file range for the given logical file range of the protected file content.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfLogicalFileRangeToRawFileRange(
  _In_  IPCF_FILE_HANDLE     hFile,
  _In_  PCIPCF_FILE_RANGE    inRange,
  _Out_ PIPCF_RAW_FILE_RANGE outRange
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle to the protected file obtained from [**IpcfOpenFileOnILockBytes**](ipcfopenfileonilockbytes.md) or [**IpcfOpenFileOnHandle**](ipcfopenfileonhandle.md).

</dd> <dt>

*inRange* \[in\]
</dt> <dd>

Pointer to the structure [**IPCF\_FILE\_RANGE**](ipcf-file-range.md) indicating the logical range of data in the pfile represented by *hFile*.

</dd> <dt>

*outRange* \[out\]
</dt> <dd>

Pointer to the structure [**IPCF\_RAW\_FILE\_RANGE**](ipcf-raw-file-range.md) indicating the raw range corresponding to the logical range represented by *inRange*.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



 

 





