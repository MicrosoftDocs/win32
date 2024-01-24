---
description: Computes the Secure Sockets Layer protocol (SSL) master secret key.
ms.assetid: c9408eb3-711d-42c3-a4ba-e388689da34e
title: SslGenerateMasterKey function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SslGenerateMasterKey
api_type:
- DllExport
api_location:
- Ncrypt.dll
---

# SslGenerateMasterKey function

The **SslGenerateMasterKey** function computes the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) master secret key.

## Syntax


```C++
SECURITY_STATUS WINAPI SslGenerateMasterKey(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  NCRYPT_KEY_HANDLE  hPrivateKey,
  _In_  NCRYPT_KEY_HANDLE  hPublicKey,
  _Out_ NCRYPT_KEY_HANDLE  *phMasterKey,
  _In_  DWORD              dwProtocol,
  _In_  DWORD              dwCipherSuite,
  _In_  PNCryptBufferDesc  pParameterList,
  _Out_ PBYTE              pbOutput,
  _In_  DWORD              cbOutput,
  _Out_ DWORD              *pcbResult,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the SSL protocol provider instance.

</dd> <dt>

*hPrivateKey* \[in\]
</dt> <dd>

The handle to the [*private key*](/windows/desktop/SecGloss/p-gly) used in the exchange.

</dd> <dt>

*hPublicKey* \[in\]
</dt> <dd>

The handle to the [*public key*](/windows/desktop/SecGloss/p-gly) used in the exchange.

</dd> <dt>

*phMasterKey* \[out\]
</dt> <dd>

A pointer to the handle to the generated [*master key*](/windows/desktop/SecGloss/m-gly).

</dd> <dt>

*dwProtocol* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Protocol Identifier**](https://msdn.microsoft.com/library/Hh971257(v=VS.85).aspx) values.

</dd> <dt>

*dwCipherSuite* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Cipher Suite Identifier**](https://msdn.microsoft.com/library/Hh971253(v=VS.85).aspx) values.

</dd> <dt>

*pParameterList* \[in\]
</dt> <dd>

A pointer to an array of **NCryptBuffer** buffers that contain information used as part of the key exchange operation. The precise set of buffers is dependent on the protocol and cipher suite that is used. At the minimum, the list will contain buffers that contain the client and server supplied random values.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

The address of a buffer that receives the premaster secret encrypted with the public key of the server. The *cbOutput* parameter contains the size of this buffer. If this parameter is **NULL**, this function returns the required size, in bytes, in the **DWORD** pointed to by the *pcbResult* parameter.

> [!Note]  
> This buffer is used when performing a RSA key exchange.

 

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The size, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a **DWORD** value in which to place number of bytes written to the *pbOutput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies whether this function is being used for client-side or server-side key exchange.



| Value                                                                                                                                                                                                                                                      | Meaning                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="NCRYPT_SSL_CLIENT_FLAG"></span><span id="ncrypt_ssl_client_flag"></span><dl> <dt>**NCRYPT\_SSL\_CLIENT\_FLAG**</dt> <dt>0x00000001</dt> </dl> | Specifies a client-side key exchange.<br/> |
| <span id="NCRYPT_SSL_SERVER_FLAG"></span><span id="ncrypt_ssl_server_flag"></span><dl> <dt>**NCRYPT\_SSL\_SERVER\_FLAG**</dt> <dt>0x00000002</dt> </dl> | Specifies a server-side key exchange.<br/> |



 

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Not enough memory is available to allocate necessary buffers.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | One of the provided handles is not valid.<br/>                     |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phMasterKey* or *hPublicKey* parameter is not valid.<br/>     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

