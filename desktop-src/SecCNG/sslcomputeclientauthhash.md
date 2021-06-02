---
description: Computes a hash to use during certificate authentication.
ms.assetid: f4a12464-8ad6-4bf9-8b6e-49bdf5332b66
title: SslComputeClientAuthHash function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslComputeClientAuthHash
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslComputeClientAuthHash function

The **SslComputeClientAuthHash** function computes a [*hash*](/windows/desktop/SecGloss/h-gly) to use during [*certificate*](/windows/desktop/SecGloss/c-gly) authentication.

## Syntax


```C++
SECURITY_STATUS WINAPI SslComputeClientAuthHash(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  NCRYPT_KEY_HANDLE  hMasterKey,
  _In_  NCRYPT_HASH_HANDLE hHandshakeHash,
  _In_  LPCWSTR            pszAlgId,
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

The handle of the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

</dd> <dt>

*hMasterKey* \[in\]
</dt> <dd>

The handle of the [*master key*](/windows/desktop/SecGloss/m-gly) object.

</dd> <dt>

*hHandshakeHash* \[in\]
</dt> <dd>

The handle of the hash of the handshake computed so far.

</dd> <dt>

*pszAlgId* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that identifies the requested [*cryptographic algorithm*](/windows/desktop/SecGloss/c-gly). This can be one of the standard [**CNG Algorithm Identifiers**](cng-algorithm-identifiers.md) or the identifier for another registered algorithm.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

The address of a buffer that receives the [*key BLOB*](/windows/desktop/SecGloss/k-gly). The *cbOutput* parameter contains the size of this buffer. If this parameter is **NULL**, this function will place the required size, in bytes, in the **DWORD** pointed to by the *pcbResult* parameter.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a **DWORD** value that specifies the length, in bytes, of the hash written to the *pbOutput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the supplied handles is not valid.<br/> |



 

## Remarks

The **SslComputeClientAuthHash** function computes the hash that is sent in the certificate verification message of the SSL handshake. The hash value is computed by creating a hash that contains the master secret with a hash of all previous handshake messages sent or received. For more information about the SSL handshake sequence, see [Description of the Secure Sockets Layer (SSL) Handshake](https://support.microsoft.com/kb/257591).

The manner in which the hash is computed depends on the protocol and cipher suite used. In addition, the hash depends on the type of client authentication key used; the *pszAlgId* parameter indicates the type of key used for client authentication.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

