---
Description: Retrieves the cipher suite information for a specified protocol, cipher suite, and key type set.
ms.assetid: ab995d9a-48fa-491a-95b1-d15c5b92f1da
title: SslLookupCipherSuiteInfo function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SslLookupCipherSuiteInfo function

The **SslLookupCipherSuiteInfo** function retrieves the cipher suite information for a specified protocol, cipher suite, and key type set.

## Syntax


```C++
SECURITY_STATUS WINAPI SslLookupCipherSuiteInfo(
  _In_  NCRYPT_PROV_HANDLE      hSslProvider,
  _In_  DWORD                   dwProtocol,
  _In_  DWORD                   dwCipherSuite,
  _In_  DWORD                   dwKeyType,
  _Out_ NCRYPT_SSL_CIPHER_SUITE *pCipherSuite,
  _In_  DWORD                   dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the [*Secure Sockets Layer protocol*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-secure-sockets-layer-protocol-gly) (SSL) protocol provider instance.

</dd> <dt>

*dwProtocol* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Protocol Identifier**](seccngprov-cng_ssl_provider_protocol_identifiers) values.

</dd> <dt>

*dwCipherSuite* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Cipher Suite Identifiers**](seccngprov-cng_ssl_provider_cipher_suite_identifiers) values.

</dd> <dt>

*dwKeyType* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Key Type Identifiers**](seccngprov-cng_ssl_provider_key_type_identifiers) values.

</dd> <dt>

*pCipherSuite* \[out\]
</dt> <dd>

The address of a buffer that contains a [**NCRYPT\_SSL\_CIPHER\_SUITE**](seccngprov-ncrypt_ssl_cipher_suite) structure in which to write the cipher suite information.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | The *hSslProvider* handle is not valid.<br/> |



 

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

 




