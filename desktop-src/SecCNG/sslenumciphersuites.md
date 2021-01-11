---
description: Enumerates the cipher suites supported by a Secure Sockets Layer protocol (SSL) protocol provider.
ms.assetid: c12bc422-71c9-44f4-abf7-76902b19d3bd
title: SslEnumCipherSuites function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslEnumCipherSuites
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslEnumCipherSuites function

The **SslEnumCipherSuites** function enumerates the cipher suites supported by a [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider.

## Syntax


```C++
SECURITY_STATUS WINAPI SslEnumCipherSuites(
  _In_     NCRYPT_PROV_HANDLE      hSslProvider,
  _In_opt_ NCRYPT_KEY_HANDLE       hPrivateKey,
  _Out_    NCRYPT_SSL_CIPHER_SUITE **ppCipherSuite,
  _Inout_  PVOID                   *ppEnumState,
  _In_     DWORD                   dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the SSL protocol provider instance.

</dd> <dt>

*hPrivateKey* \[in, optional\]
</dt> <dd>

The handle of a [*private key*](/windows/desktop/SecGloss/p-gly). When a private key is specified, **SslEnumCipherSuites** enumerates the cipher suites that are compatible with the private key. For example, if the private key is a DSS key, then only the DSS\_DHE cipher suites are returned. If the private key is an RSA key, but it does not support raw decryption operations, then the SSL2 cipher suites are not returned.

Set this parameter to **NULL** when you are not specifying a private key.

> [!Note]  
> A *hPrivateKey* handle is obtained by calling the [**SslOpenPrivateKey**](sslopenprivatekey.md) function. Handles obtained from the [**NCryptOpenKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptopenkey) function are not supported.

 

</dd> <dt>

*ppCipherSuite* \[out\]
</dt> <dd>

A pointer to a [**NCRYPT\_SSL\_CIPHER\_SUITE**](https://www.bing.com/search?q=**NCRYPT\_SSL\_CIPHER\_SUITE**) structure to receive the address of the next cipher suite in the list.

</dd> <dt>

*ppEnumState* \[in, out\]
</dt> <dd>

A pointer to a buffer that indicates the current position in the list of cipher suites.

Set the pointer to **NULL** on the first call to **SslEnumCipherSuites**. On each subsequent call, pass the unmodified value back to **SslEnumCipherSuites**.

When there are no more cipher suites available, you should free *ppEnumState* by calling the [**SslFreeBuffer**](sslfreebuffer.md) function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>      | Not enough memory is available to allocate necessary buffers.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the provided handles is not valid.<br/>                     |
| <dl> <dt>**NTE\_NO\_MORE\_ITEMS**</dt> <dt>0x8009002AL</dt> </dl> | No additional cipher suites are supported.<br/>                    |



 

## Remarks

To enumerate all cipher suites supported by the SSL provider, call the **SslEnumCipherSuites** function in a loop until **NTE\_NO\_MORE\_ITEMS** is returned.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Ncrypt.lib</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



## See also

<dl> <dt>

[**NCRYPT\_SSL\_CIPHER\_SUITE**](https://www.bing.com/search?q=**NCRYPT\_SSL\_CIPHER\_SUITE**)
</dt> </dl>

 

