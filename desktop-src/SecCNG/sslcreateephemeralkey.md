---
description: Creates an ephemeral key for use during the authentication that occurs during the Secure Sockets Layer protocol (SSL) handshake.
ms.assetid: faad9b3b-e476-4e61-b978-bcb517ecaeb7
title: SslCreateEphemeralKey function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SslCreateEphemeralKey
api_type:
- DllExport
api_location:
- Ncrypt.dll
---

# SslCreateEphemeralKey function

The **SslCreateEphemeralKey** function creates an ephemeral key for use during the authentication that occurs during the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) handshake.

## Syntax


```C++
SECURITY_STATUS WINAPI SslCreateEphemeralKey(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _Out_ NCRYPT_KEY_HANDLE  *phEphemeralKey,
  _In_  DWORD              dwProtocol,
  _In_  DWORD              dwCipherSuite,
  _In_  DWORD              dwKeyType,
  _In_  DWORD              dwKeyBitLen,
  _In_  PBYTE              pbParams,
  _In_  DWORD              cbParams,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the SSL protocol provider instance.

</dd> <dt>

*phEphemeralKey* \[out\]
</dt> <dd>

The handle of the ephemeral key.

</dd> <dt>

*dwProtocol* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Protocol Identifier**](https://msdn.microsoft.com/library/Hh971257(v=VS.85).aspx) values.

</dd> <dt>

*dwCipherSuite* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Cipher Suite Identifier**](https://msdn.microsoft.com/library/Hh971253(v=VS.85).aspx) values.

</dd> <dt>

*dwKeyType* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Key Type Identifier**](https://msdn.microsoft.com/library/Hh971256(v=VS.85).aspx) values. Set this parameter to zero for key types that are not [*elliptic curve cryptography*](/windows/desktop/SecGloss/e-gly) (ECC).

</dd> <dt>

*dwKeyBitLen* \[in\]
</dt> <dd>

The length, in bits, of the key.

</dd> <dt>

*pbParams* \[in\]
</dt> <dd>

A pointer to a buffer to contain parameters for the key that is to be created. If a [*Diffie-Hellman (ephemeral) key-exchange algorithm*](/windows/desktop/SecGloss/d-gly) (DHE) cipher suite is not used, set the *pbParams* parameter to **NULL** and the *cbParams* parameter to zero.

</dd> <dt>

*cbParams* \[in\]
</dt> <dd>

The length, in bytes, of the data in the *pbParams* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.



| Return code/value                                                                                                                                                       | Description                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | There is insufficient memory to allocate the buffer.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* handle is not valid.<br/>              |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | One of the supplied parameters is not valid.<br/>         |



 

## Remarks

When using a DHE cipher suite, the internal SSL implementation passes server *p* and *g* parameters to the **SslCreateEphemeralKey** function in the *pbParams* and *cbParams* parameters.

The format of the data in the *pbParams* buffer is the same as that used when setting the [**BCRYPT\_DH\_PARAMETERS**](cng-property-identifiers.md) property, and it starts with a [**BCRYPT\_DH\_PARAMETER\_HEADER**](/windows/desktop/api/Bcrypt/ns-bcrypt-bcrypt_dh_parameter_header) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

