---
description: Generates a set of Secure Sockets Layer protocol (SSL) session keys.
ms.assetid: 88465f30-8591-411e-8618-8a381d4c22e9
title: SslGenerateSessionKeys function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslGenerateSessionKeys
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslGenerateSessionKeys function

The **SslGenerateSessionKeys** function generates a set of [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) session keys.

## Syntax


```C++
SECURITY_STATUS WINAPI SslGenerateSessionKeys(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  NCRYPT_KEY_HANDLE  hMasterKey,
  _Out_ NCRYPT_KEY_HANDLE  *phReadKey,
  _Out_ NCRYPT_KEY_HANDLE  *phWriteKey,
  _In_  PNCryptBufferDesc  pParameterList,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the SSL protocol provider instance.

</dd> <dt>

*hMasterKey* \[in\]
</dt> <dd>

The handle to the [*master key*](/windows/desktop/SecGloss/m-gly) object.

</dd> <dt>

*phReadKey* \[out\]
</dt> <dd>

A pointer to the returned read key handle.

</dd> <dt>

*phWriteKey* \[out\]
</dt> <dd>

A pointer to the returned write key handle.

</dd> <dt>

*pParameterList* \[in\]
</dt> <dd>

A pointer to an array of **NCryptBuffer** buffers that contain information used as part of the key exchange operation. The precise set of buffers is dependent on the protocol and cipher suite that is used. At the minimum, the list will contain buffers that contain the client and server supplied random values.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Not enough memory is available to allocate necessary buffers.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | One of the provided handles is not valid.<br/>                     |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phReadKey* or *phWriteKey* parameter is null.<br/>            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

