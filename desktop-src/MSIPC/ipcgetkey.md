---
title: IpcGetKey function
description: Returns a handle to a key object created from a serialized license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 79140dba-d469-4500-a559-0d6e5ece7071
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetKey function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetKey
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcGetKey function

Returns a handle to a key object created from a serialized license.

## Syntax


```C++
HRESULT WINAPI IpcGetKey(
  _In_       PCIPC_BUFFER     pvLicense,
             DWORD            dwFlags,
  _In_opt_   PCIPC_PROMPT_CTX pContext,
  _Reserved_ LPVOID           pvReserved,
  _Out_      PIPC_KEY_HANDLE  phKey
);
```



## Parameters

<dl> <dt>

*pvLicense* \[in\]
</dt> <dd>

The serialized license for which the key is to be created. For more information, see [**IPC\_BUFFER**](ipc-buffer.md).

</dd> <dt>

*dwFlags* 
</dt> <dd>

Must be 0.

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

An optional pointer to an [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure. This can be used in cases where authentication prompts are not desirable or when an application wants to control the modal behavior of any prompt dialogs.

</dd> <dt>

*pvReserved* 
</dt> <dd>

Reserved for future use. Must be **NULL**.

</dd> <dt>

*phKey* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the key object created by this function.

> [!Note]  
> This key handle should be closed with [**IpcCloseHandle**](ipcclosehandle.md) when no longer needed.

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_NEEDS\_ONLINE**
</dt> <dd>

RMS SDK 2.1 needs network access to complete the operation, but the application requested offline mode.

Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_OFFLINE** flag. Typically, this flag is used in situations in which failure is acceptable and preferred to performing a network access. The system is already optimized to use the network only when absolutely necessary, so we do not recommend that developers use the **IPC\_PROMPT\_FLAG\_OFFLINE** flag as an optimization.

</dd> <dt>

**IPCERROR\_NEEDS\_UI**
</dt> <dd>

RMS SDK 2.1 needs to display a window to complete the operation, but the application requested silent mode.

Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_SILENT** flag.

</dd> <dt>

**IPCERROR\_RIGHT\_NOT\_GRANTED**
</dt> <dd>

Meaning: The user does not have rights to consume the content.

Action: Communicate the process for requesting adequate rights. Referral information can be queried using [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) with *dwPropID* set to **IPC\_LI\_REFERRAL\_INFO\_URL**.

</dd> </dl>

## Remarks

A key object is required for decryption, encryption, and checking granted rights. A key object is created only if the current user has access to the content that the serialized license in *pvLicense* is associated with. The key object is populated with the rights granted to the current user. Whether a specific right has been granted to the current user can be checked by calling [**IpcAccessCheck**](ipcaccesscheck.md).

**IpcGetKey** may initialize COM with the **COINIT\_APARTMENTTHREADED** flag to display user interface elements. As a result, callers who have initialized COM with the **COINIT\_MULTITHREADED** flag must use the **IpcGetKey** function in silent mode by using the **IPC\_PROMPT\_FLAG\_SILENT** flag with the [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IPC\_BUFFER**](ipc-buffer.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IpcAccessCheck**](ipcaccesscheck.md)
</dt> <dt>

[**IpcCloseHandle**](ipcclosehandle.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





