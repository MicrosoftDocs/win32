---
title: IpcGetTemplateIssuerList function
description: Returns available issuers of rights policy templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '019c9f42-ba17-488c-941e-e1ae45daa10a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcGetTemplateIssuerList function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcGetTemplateIssuerList
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcGetTemplateIssuerList function

Returns available issuers of rights policy templates. The available issuers is a list of RMS servers that this user has already contacted.

## Syntax


```C++
HRESULT WINAPI IpcGetTemplateIssuerList(
  _In_opt_   PCIPC_CONNECTION_INFO      pConnectionInfo,
             DWORD                      dwFlags,
  _In_opt_   PCIPC_PROMPT_CTX           pContext,
  _Reserved_ LPVOID                     pvReserved,
  _Out_      PCIPC_TEMPLATE_ISSUER_LIST *ppcTemplateIssuers
);
```



## Parameters

<dl> <dt>

*pConnectionInfo* \[in, optional\]
</dt> <dd>

Optional RMS Server information from which to get templates. See [**IPC\_CONNECTION\_INFO**](ipc-connection-info.md) for server URLs.

If specified, this function will return only the [**IPC\_TEMPLATE\_ISSUER\_LIST**](ipc-template-issuer-list.md) structure for the specified server. If not specified, this function will return **IPC\_TEMPLATE\_ISSUER\_LIST** structures for all available servers.

</dd> <dt>

*dwFlags* 
</dt> <dd>

<dt>

<span id="IPC_GTIL_FLAG_DEFAULT_SERVER_ONLY"></span><span id="ipc_gtil_flag_default_server_only"></span>

<span id="IPC_GTIL_FLAG_DEFAULT_SERVER_ONLY"></span><span id="ipc_gtil_flag_default_server_only"></span>**IPC\_GTIL\_FLAG\_DEFAULT\_SERVER\_ONLY** (1)


</dt> <dd>

Use this flag to retrieve only the default server for the enterprise or user. If this flag is specified, then *pConnectionInfo* should be **NULL**.

</dd> </dl> </dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

An optional pointer to an [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure. This can be used in cases where authentication prompts are not desirable or when an application wants to control the modal behavior of any prompt dialogs.

</dd> <dt>

*pvReserved* 
</dt> <dd>

Reserved for future use. Must be **NULL**.

</dd> <dt>

*ppcTemplateIssuers* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the Template Issuer List. For more information, see [**IPC\_TEMPLATE\_ISSUER\_LIST**](ipc-template-issuer-list.md).

> [!Note]  
> The buffer is allocated by the RMS SDK 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md).

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_NEEDS\_ONLINE**
</dt> <dd>

Meaning: RMS SDK 2.1 needs network access to complete the operation, but the application requested offline mode.

Action: Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_OFFLINE** flag. Typically, this flag is used in situations in which failure is acceptable and preferred to performing a network access. The system is already optimized to use the network only when absolutely necessary, so we do not recommend that developers use the **IPC\_PROMPT\_FLAG\_OFFLINE** flag as an optimization.

</dd> <dt>

**IPCERROR\_NEEDS\_UI**
</dt> <dd>

Meaning: RMS SDK 2.1 needs to display a window to complete the operation, but the application requested silent mode.

Action: Call the function again, without specifying the IPC\_PROMPT\_FLAG\_SILENT flag.

</dd> </dl>

## Remarks

The issuer information can be used as basis of application-specified policy. An application can use the issuer information returned by this function to create its own usage policy by calling [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) if the **fAllowFromScratch** of the [**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md) structure is set to **TRUE**.

**IpcGetTemplateIssuerList** may initialize COM with the **COINIT\_APARTMENTTHREADED** flag to display user interface elements. As a result, callers who have initialized COM with the **COINIT\_MULTITHREADED** flag must use the **IpcGetTemplateIssuerList** function in silent mode by using the **IPC\_PROMPT\_FLAG\_SILENT** flag with the [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Ipcprot.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPC\_CONNECTION\_INFO**](ipc-connection-info.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md)
</dt> <dt>

[**IPC\_TEMPLATE\_ISSUER\_LIST**](ipc-template-issuer-list.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





