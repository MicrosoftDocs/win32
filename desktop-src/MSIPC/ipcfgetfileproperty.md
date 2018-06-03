---
title: IpcfGetFileProperty function
description: Queries the properties of an IPCF\_FILE\_HANDLE or the file represented by it.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2aebb209-ddbc-4962-a447-b476e39c620b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfGetFileProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfGetFileProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcfGetFileProperty function

Queries the properties of an **IPCF\_FILE\_HANDLE** or the file represented by it.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfGetFileProperty(
  _In_  IPCF_FILE_HANDLE hFile,
  _In_  DWORD            dwPropId,
  _Out_ LPVOID           *ppvProperty
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle properties to be queried.

</dd> <dt>

*dwPropId* \[in\]
</dt> <dd>

Which file property to query.

The *ppvProperty* parameter must match this property ID.

<dt>

<span id="IPCF_FI_HEADER_POSITION"></span><span id="ipcf_fi_header_position"></span>

<span id="IPCF_FI_HEADER_POSITION"></span><span id="ipcf_fi_header_position"></span>**IPCF\_FI\_HEADER\_POSITION** (1)


</dt> <dd>

Describes the file range indicating the offset and size of the protected file header.

> [!Note]  
> For **IpcfGetFileProperty***ppvProperty* is of type **PIPCF\_FILE\_RANGE**\*.

 

</dd> <dt>

<span id="IPCF_FI_CONTENT_KEY"></span><span id="ipcf_fi_content_key"></span>

<span id="IPCF_FI_CONTENT_KEY"></span><span id="ipcf_fi_content_key"></span>**IPCF\_FI\_CONTENT\_KEY** (2)


</dt> <dd>

> \[!Important\]  
> This is currently not implemented and returns **E\_NOTIMPL** if called.

 

Describes the handle to the key which is used to protect the content of the file specified by parameter *hFile*.

> [!Note]  
> For **IpcfGetFileProperty***ppvProperty* is of type **IPC\_KEY\_HANDLE**\*.

 

</dd> <dt>

<span id="IPCF_FI_ACCESS_BLOCK_SIZE"></span><span id="ipcf_fi_access_block_size"></span>

<span id="IPCF_FI_ACCESS_BLOCK_SIZE"></span><span id="ipcf_fi_access_block_size"></span>**IPCF\_FI\_ACCESS\_BLOCK\_SIZE** (3)


</dt> <dd>

Specifies the size of blocks with which the data will be accessed.

> [!Note]  
> For **IpcfGetFileProperty***ppvProperty* is of type **LPDWORD**\*.

 

</dd> <dt>

<span id="IPCF_FI_BASIC_INFORMATION"></span><span id="ipcf_fi_basic_information"></span>

<span id="IPCF_FI_BASIC_INFORMATION"></span><span id="ipcf_fi_basic_information"></span>**IPCF\_FI\_BASIC\_INFORMATION** (4)


</dt> <dd>

> \[!Important\]  
> This is currently not implemented and returns **E\_NOTIMPL** if called.

 

Specifies the basic information about the file represented by the parameter *hFile*.

> [!Note]  
> For **IpcfGetFileProperty***ppvProperty* is of type **PIPCF\_FILE\_BASIC\_INFORMATION**\*.

 

</dd> </dl> </dd> <dt>

*ppvProperty* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the property information.

The structure of the property information depends on the *dwPropID* parameter.

> [!Note]  
> The buffer is allocated by the AD RMS SDK 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md).

 

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



 

 





