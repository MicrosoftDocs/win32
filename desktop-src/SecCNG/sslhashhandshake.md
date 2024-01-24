---
description: Returns a handle to the handshake hash.
ms.assetid: c0f20084-c863-42cf-afdf-298c5a96eed9
title: SslHashHandshake function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslHashHandshake
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslHashHandshake function

The **SslHashHandshake** function returns a handle to the handshake hash.

## Syntax


```C++
SECURITY_STATUS WINAPI SslHashHandshake(
  _In_    NCRYPT_PROV_HANDLE hSslProvider,
  _Inout_ NCRYPT_HASH_HANDLE hHandshakeHash,
  _Out_   PBYTE              pbInput,
  _In_    DWORD              cbInput,
  _In_    DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

</dd> <dt>

*hHandshakeHash* \[in, out\]
</dt> <dd>

The handle to the hash object.

</dd> <dt>

*pbInput* \[out\]
</dt> <dd>

The address of a buffer that contains the data to be hashed.

</dd> <dt>

*cbInput* \[in\]
</dt> <dd>

The size, in bytes, of the *pbInput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

## Remarks

The **SslHashHandshake** function is one of three functions used to generate a hash to use during the SSL handshake.

1.  The [**SslCreateHandshakeHash**](sslcreatehandshakehash.md) function is called to obtain a hash handle.
2.  The **SslHashHandshake** function is called any number of times with the hash handle to add data to the hash.
3.  The [**SslComputeFinishedHash**](sslcomputefinishedhash.md) function is called with the hash handle to obtain the digest of the hashed data.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

