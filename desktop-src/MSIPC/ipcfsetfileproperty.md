---
title: IpcfSetFileProperty function
description: Sets the properties on IPCF\_FILE\_HANDLE or on the file represented by it.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0d49f2b6-41cf-4a7c-ac90-e4fd5237d531
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfSetFileProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfSetFileProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcfSetFileProperty function

Sets the properties on **IPCF\_FILE\_HANDLE** or on the file represented by it.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfSetFileProperty(
  _In_ IPCF_FILE_HANDLE hFile,
  _In_ DWORD            dwPropId,
  _In_ LPCVOID          pvProperty
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle properties to be set.

</dd> <dt>

*dwPropId* \[in\]
</dt> <dd>

Type of file property to modify.

The *pvProperty* parameter must match this type.

<dt>

<span id="IPCF_FI_HEADER_POSITION"></span><span id="ipcf_fi_header_position"></span>

<span id="IPCF_FI_HEADER_POSITION"></span><span id="ipcf_fi_header_position"></span>**IPCF\_FI\_HEADER\_POSITION** (1)


</dt> <dd>

Describes the file range indicating the offset and size of the protected file header.

> [!Note]  
> For **IpcfSetFileProperty** cannot set this property.

 

</dd> <dt>

<span id="IPCF_FI_CONTENT_KEY"></span><span id="ipcf_fi_content_key"></span>

<span id="IPCF_FI_CONTENT_KEY"></span><span id="ipcf_fi_content_key"></span>**IPCF\_FI\_CONTENT\_KEY** (2)


</dt> <dd>

> \[!Important\]  
> This is currently not implemented and returns **E\_NOTIMPL** if called.

 

Describes the handle to the key which is used to protect the content of the file specified by parameter *hFile*.

> [!Note]  
> For **IpcfSetFileProperty** cannot set this property.

 

</dd> <dt>

<span id="IPCF_FI_ACCESS_BLOCK_SIZE"></span><span id="ipcf_fi_access_block_size"></span>

<span id="IPCF_FI_ACCESS_BLOCK_SIZE"></span><span id="ipcf_fi_access_block_size"></span>**IPCF\_FI\_ACCESS\_BLOCK\_SIZE** (3)


</dt> <dd>

Specifies the size of blocks with which the data will be accessed.

> [!Note]  
> For **IpcfSetFileProperty***pvProperty* is of type **LPDWORD**.

 

</dd> <dt>

<span id="IPCF_FI_BASIC_INFORMATION"></span><span id="ipcf_fi_basic_information"></span>

<span id="IPCF_FI_BASIC_INFORMATION"></span><span id="ipcf_fi_basic_information"></span>**IPCF\_FI\_BASIC\_INFORMATION** (4)


</dt> <dd>

> \[!Important\]  
> This is currently not implemented and returns **E\_NOTIMPL** if called.

 

Specifies the basic information about the file represented by the parameter *hFile*.

> [!Note]  
> For **IpcfSetFileProperty***pvProperty* is of type **PCIPCF\_FILE\_BASIC\_INFORMATION**.

 

</dd> </dl> </dd> <dt>

*pvProperty* \[in\]
</dt> <dd>

Pointer to the buffer which contains the property to be set.

The value depends on the parameter *dwPropId*.

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



 

 





