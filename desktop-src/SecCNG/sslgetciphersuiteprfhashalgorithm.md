---
description: 'Returns the Cryptography API: Next Generation (CNG) Algorithm Identifier of the hashing algorithm that is used for the Transport Layer Security protocol (TLS) pseudo-random function (PRF) for the input protocol, cipher suite, and key type.'
ms.assetid: 8d20b2da-390e-458e-b122-f5ef3722ad87
title: SslGetCipherSuitePRFHashAlgorithm function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SslGetCipherSuitePRFHashAlgorithm
api_type:
- DllExport
api_location:
- Ncrypt.dll
---

# SslGetCipherSuitePRFHashAlgorithm function

The **SslGetCipherSuitePRFHashAlgorithm** function returns the Cryptography API: Next Generation (CNG) Algorithm Identifier of the [*hashing algorithm*](/windows/desktop/SecGloss/h-gly) that is used for the [*Transport Layer Security protocol*](/windows/desktop/SecGloss/t-gly) (TLS) [*pseudo-random function*](/windows/desktop/SecGloss/p-gly) (PRF) for the input protocol, cipher suite, and key type.

## Syntax


```C++
SECURITY_STATUS WINAPI SslGetCipherSuitePRFHashAlgorithm(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _In_  DWORD              dwProtocol,
  _In_  DWORD              dwCipherSuite,
  _In_  DWORD              dwKeyType,
  _Out_ WCHAR              szPRFHash[NCRYPT_SSL_MAX_NAME_SIZE],
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

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

One of the [**CNG SSL Provider Key Type Identifier**](https://msdn.microsoft.com/library/Hh971256(v=VS.85).aspx) values. For key types that are not [*elliptic curve cryptography*](/windows/desktop/SecGloss/e-gly) (ECC), set this parameter to zero.

</dd> <dt>

*szPRFHash* \[out\]
</dt> <dd>

One of the [**CNG Algorithm Identifiers**](cng-algorithm-identifiers.md) for the hash that will be used for the TLS PRF.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use and must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* parameter contains a pointer that is not valid.<br/>                |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *szPRFHash* parameter is set to **NULL**.<br/>                                     |
| <dl> <dt>**NTE\_NOT\_SUPPORTED**</dt> <dt>0x80090029L</dt> </dl>     | The selected function is not supported in the specified version of the interface.<br/> |
| <dl> <dt>**NTE\_BAD\_FLAGS**</dt> <dt>0x80090009L</dt> </dl>         | The *dwFlags* parameter must be set to zero.<br/>                                      |



 

## Remarks

This **SslGetCipherSuitePRFHashAlgorithm** function is called for TLS 1.2 or later conversations to query the hashing algorithm that will be used in the TLS PRF.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

