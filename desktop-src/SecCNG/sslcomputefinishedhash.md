---
description: Computes the hash sent in the finished message of the Secure Sockets Layer protocol (SSL) handshake.
ms.assetid: 82dfeb1d-c141-40c9-b692-daad78ab6d55
title: SslComputeFinishedHash function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslComputeFinishedHash
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslComputeFinishedHash function

The **SslComputeFinishedHash** function computes the [*hash*](/windows/desktop/SecGloss/h-gly) sent in the finished message of the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) handshake.

## Syntax


```C++
SECURITY_STATUS WINAPI SslComputeFinishedHash(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  NCRYPT_KEY_HANDLE  hMasterKey,
  _In_  NCRYPT_HASH_HANDLE hHandshakeHash,
  _Out_ PBYTE              pbOutput,
  _In_  DWORD              cbOutput,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the SSL protocol provider instance.

</dd> <dt>

*hMasterKey* \[in\]
</dt> <dd>

The handle of the [*master key*](/windows/desktop/SecGloss/m-gly) object.

</dd> <dt>

*hHandshakeHash* \[in\]
</dt> <dd>

The handle of the hash of the handshake messages.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

A pointer to a buffer that receives the hash for the finish message.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

One of the following constants.



| Value                                                                                                                                                                                                                                                      | Meaning                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="NCRYPT_SSL_CLIENT_FLAG"></span><span id="ncrypt_ssl_client_flag"></span><dl> <dt>**NCRYPT\_SSL\_CLIENT\_FLAG**</dt> <dt>0x00000001</dt> </dl> | Specifies that this is a client call.<br/> |
| <span id="NCRYPT_SSL_SERVER_FLAG"></span><span id="ncrypt_ssl_server_flag"></span><dl> <dt>**NCRYPT\_SSL\_SERVER\_FLAG**</dt> <dt>0x00000002</dt> </dl> | Specifies that this is a server call.<br/> |



 

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.



| Return code/value                                                                                                                                                                | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>2148073510 (0x80090026)</dt> </dl> | One of the supplied handles is not valid.<br/> |



 

## Remarks

The **SslComputeFinishedHash** function is one of three functions used to generate a hash to use during the SSL handshake.

1.  The [**SslCreateHandshakeHash**](sslcreatehandshakehash.md) function is called to obtain a hash handle.
2.  The [**SslHashHandshake**](sslhashhandshake.md) function is called any number of times with the hash handle to add data to the hash.
3.  The **SslComputeFinishedHash** function is called with the hash handle to obtain the digest of the hashed data.

The hash value is computed by hashing the master secret with a hash of all previous handshake messages sent or received.

The value of *cbOutput* determines the length of the hash data. When the [*Transport Layer Security protocol*](/windows/desktop/SecGloss/t-gly) (TLS) 1.0 protocol is used, this should always be 12 (bytes). For more information, see [The TLS Protocol Version 1.0](https://www.ietf.org/rfc/rfc2246.txt).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

