---
description: Signs a hash by using the specified private key.
ms.assetid: 25e8ebc5-278d-4d1f-977a-c2fab07b790a
title: SslSignHash function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslSignHash
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslSignHash function

The **SslSignHash** function signs a [*hash*](/windows/desktop/SecGloss/h-gly) by using the specified [*private key*](/windows/desktop/SecGloss/p-gly). The signing process is performed on the server.

## Syntax


```C++
SECURITY_STATUS WINAPI SslSignHash(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  NCRYPT_KEY_HANDLE  hPrivateKey,
  _In_  PBYTE              pbHashValue,
  _In_  DWORD              cbHashValue,
  _Out_ PBYTE              pbSignature,
  _In_  DWORD              cbSignature,
  _Out_ DWORD              *pcbResult,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

</dd> <dt>

*hPrivateKey* \[in\]
</dt> <dd>

The handle to the private key to use to sign the hash.

</dd> <dt>

*pbHashValue* \[in\]
</dt> <dd>

A pointer to a buffer that contains the hash to sign.

</dd> <dt>

*cbHashValue* \[in\]
</dt> <dd>

The size, in bytes, of the *pbHashValue* buffer.

</dd> <dt>

*pbSignature* \[out\]
</dt> <dd>

The address of a buffer that receives the signature of the hash. The *cbSignature* parameter contains the size of this buffer. To determine the required sized size of the buffer, set the *pbSignature* parameter to **NULL**. The required size of the buffer will be returned in the *pcbResult* parameter.

</dd> <dt>

*cbSignature* \[in\]
</dt> <dd>

The size, in bytes, of the *pbSignature* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a value that, upon completion, contains the actual number of bytes written to the *pbSignature* buffer.

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
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the provided handles is not valid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

