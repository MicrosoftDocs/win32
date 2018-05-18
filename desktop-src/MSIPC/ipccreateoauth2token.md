---
title: IpcCreateOAuth2Token function
description: Returns a handle to an authentication token object that is created from an authentication token string.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '2F202E11-3AFD-4EC3-9C86-C1AEB35F7F6B'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcCreateOAuth2Token function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcCreateOAuth2Token
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcCreateOAuth2Token function

Returns a handle to an authentication token object that is created from an authentication token string.

## Syntax


```C++
HRESULT WINAPI IpcCreateOAuth2Token(
  _In_  LPCWSTR                wszAuthToken,
  _Out_ PIPC_AUTH_TOKEN_HANDLE phIpcAuthToken
);
```



## Parameters

<dl> <dt>

*wszAuthToken* \[in\]
</dt> <dd>

A string representing an authentication token provided by a Security Token Service. The string should be in the form of a JSON Web Token (JWT).

</dd> <dt>

*phIpcAuthToken* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the authentication token object.

> [!Note]  
> This key handle should only be closed with [**IpcCloseHandle**](ipcclosehandle.md) when [*IPC\_OAUTH2\_CALLBACK*](ipc-oauth2-callback.md) does not return successfully.

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

When calling **IpcCreateOAuth2Token** from inside your [*IPC\_OAUTH2\_CALLBACK*](ipc-oauth2-callback.md) function, you should not release the handle to *phIpcAuthToken* unless you will be returning an error code from your *IPC\_OAUTH2\_CALLBACK* function. The RMS Client will manage the allocation release when your *IPC\_OAUTH2\_CALLBACK* function returns successfully.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IPC\_CREDENTIAL**](ipc-credential.md)
</dt> <dt>

[*IPC\_OAUTH2\_CALLBACK*](ipc-oauth2-callback.md)
</dt> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





