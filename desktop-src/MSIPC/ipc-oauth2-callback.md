---
title: IPC\_OAUTH2\_CALLBACK callback function
description: A pointer to a function that is called when the RMS client requests an OAuth authentication token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F193EF52-00B3-40D6-A2D6-FE3C6D6B887B'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_OAUTH2_CALLBACK callback function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_OAUTH2_CALLBACK
api_location:
- Ipcbase.h
api_type:
- UserDefined
---

# IPC\_OAUTH2\_CALLBACK callback function

A pointer to a function that is called when the RMS client requests an OAuth authentication token.

## Syntax


```C++
HRESULT  CALLBACK IPC_OAUTH2_CALLBACK(
  _In_  LPVOID                pvContext,
  _In_  PIPC_NAME_VALUE_LIST  pOAuth2ChallengeInfo,
  _Out_ IPC_AUTH_TOKEN_HANDLE *phAccessToken
);
```



## Parameters

<dl> <dt>

*pvContext* \[in\]
</dt> <dd>

Pointer to an application-defined structure that is assigned as part of [**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md).

</dd> <dt>

*pOAuth2ChallengeInfo* \[in\]
</dt> <dd>

Pointer to a list of OAuth settings provided by the IRM server.

For the Azure Active Directory Security Token Service (STS), these settings are:

<dt>

<span id="authorization"></span><span id="AUTHORIZATION"></span>

**authorization** (URL for the STS authorization provider)


</dt> <dd></dd> <dt>

<span id="resource"></span><span id="RESOURCE"></span>

**resource** (Service principal name for this Azure Rights Management Service)


</dt> <dd></dd> <dt>

<span id="realm"></span><span id="REALM"></span>

**realm** (Identifier for the tenant that is requesting the authentication token)


</dt> <dd></dd> </dl> </dd> <dt>

*phAccessToken* \[out\]
</dt> <dd>

Pointer to a pointer that will hold the address of an **IPC\_AUTH\_TOKEN\_HANDLE**.

Use [**IpcCreateOAuth2Token**](ipccreateoauth2token.md) to allocate this handle before returning successfully from the function pointed to by *IPC\_OAUTH2\_CALLBACK*.

Do not release this allocation after returning from the *IPC\_OAUTH2\_CALLBACK* function. The RMS SDK will manage the allocation release.

</dd> </dl>

## Return value

The return value of a callback is managed by the system.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPC\_NAME\_VALUE\_LIST**](ipc-name-value-list.md)
</dt> <dt>

[**IPC\_OAUTH2\_CALLBACK\_INFO**](ipc-oath2-callback-info.md)
</dt> <dt>

[**IpcCreateOAuth2Token**](ipccreateoauth2token.md)
</dt> <dt>

[**Data types**](microsoft-information-protection-and-control-client-data-types.md)
</dt> </dl>

 

 





