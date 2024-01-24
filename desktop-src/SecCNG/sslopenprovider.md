---
description: Opens a handle to the specified Secure Sockets Layer protocol (SSL) protocol provider.
ms.assetid: 0d5c4da3-12d6-4a53-a4d0-f0f174a4c8d8
title: SslOpenProvider function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslOpenProvider
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslOpenProvider function

The **SslOpenProvider** function opens a handle to the specified [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider.

## Syntax


```C++
SECURITY_STATUS WINAPI SslOpenProvider(
  _Out_ NCRYPT_PROV_HANDLE *phSslProvider,
  _In_  LPCWSTR            pszProviderName,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*phSslProvider* \[out\]
</dt> <dd>

The address of an **NCRYPT\_PROV\_HANDLE** in which to write the provider handle.

When you have finished using the handle, you should free it by calling the [**SslFreeObject**](sslfreeobject.md) function.

</dd> <dt>

*pszProviderName* \[in\]
</dt> <dd>

A pointer to a Unicode string that contains the provider name. If the value of this parameter is **NULL**, a handle to the **MS\_SCHANNEL\_PROVIDER** is returned.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use, and it must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | One of the provided handles is not valid.<br/>                      |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phSslProvider* or *ppProviderList* parameter is **NULL**.<br/> |
| <dl> <dt>**STATUS\_NO\_MEMORY**</dt> <dt>0xC0000017L</dt> </dl>      | Not enough memory is available to allocate necessary buffers.<br/>  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

