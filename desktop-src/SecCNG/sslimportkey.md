---
Description: Imports a key into the Secure Sockets Layer protocol (SSL) protocol provider.
ms.assetid: 42310799-384e-4396-a9d5-5f226ca25a86
title: SslImportKey function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SslImportKey function

The **SslImportKey** function imports a key into the [*Secure Sockets Layer protocol*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-secure-sockets-layer-protocol-gly) (SSL) protocol provider.

## Syntax


```C++
SECURITY_STATUS WINAPI SslImportKey(
  _In_  NCRYPT_PROV_HANDLE hSslProvider,
  _Out_ NCRYPT_KEY_HANDLE  *phKey,
  _In_  LPCWSTR            pszBlobType,
  _In_  PBYTE              pbKeyBlob,
  _In_  DWORD              cbKeyBlob,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle to the SSL protocol provider instance.

</dd> <dt>

*phKey* \[out\]
</dt> <dd>

A pointer to the handle of the [*cryptographic key*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-key-gly) to receive the imported key.

</dd> <dt>

*pszBlobType* \[in\]
</dt> <dd>

A null-terminated Unicode string that contains an identifier that specifies the type of [*BLOB*](https://msdn.microsoft.com/library/windows/desktop/ms721569#-security-blob-gly) that is contained in the *pbInput* buffer. This can be one of the following values.



| Value                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BCRYPT_DH_PUBLIC_BLOB"></span><span id="bcrypt_dh_public_blob"></span><dl> <dt>**BCRYPT\_DH\_PUBLIC\_BLOB**</dt> </dl>    | Export a Diffie-Hellman [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly). The *pbOutput* buffer receives a [**BCRYPT\_DH\_KEY\_BLOB**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dh_key_blob?branch=master) structure immediately followed by the key data.<br/>                                                                                                                                                        |
| <span id="BCRYPT_ECCPUBLIC_BLOB"></span><span id="bcrypt_eccpublic_blob"></span><dl> <dt>**BCRYPT\_ECCPUBLIC\_BLOB**</dt> </dl>     | Export an [*elliptic curve cryptography*](https://msdn.microsoft.com/library/windows/desktop/ms721575#-security-elliptic-curve-cryptography-gly) (ECC) [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly). The *pbOutput* buffer receives a [**BCRYPT\_ECCKEY\_BLOB**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_ecckey_blob?branch=master) structure immediately followed by the key data.<br/>                             |
| <span id="BCRYPT_OPAQUE_KEY_BLOB"></span><span id="bcrypt_opaque_key_blob"></span><dl> <dt>**BCRYPT\_OPAQUE\_KEY\_BLOB**</dt> </dl> | Export a [*symmetric key*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-symmetric-key-gly) in a format that is specific to a single [*cryptographic service provider*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-service-provider-gly) (CSP). Opaque BLOBs are not transferable and must be imported by using the same CSP that generated the BLOB.<br/> |
| <span id="BCRYPT_RSAPUBLIC_BLOB"></span><span id="bcrypt_rsapublic_blob"></span><dl> <dt>**BCRYPT\_RSAPUBLIC\_BLOB**</dt> </dl>     | Export an [*RSA*](https://msdn.microsoft.com/library/windows/desktop/ms721604#-security-rsa-gly) public key. The *pbOutput* buffer receives a [**BCRYPT\_RSAKEY\_BLOB**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_rsakey_blob?branch=master) structure immediately followed by the key data.<br/>                                                                                                                                                                                 |



 

</dd> <dt>

*pbKeyBlob* \[in\]
</dt> <dd>

A pointer to the buffer that contains the [*key BLOB*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-blob-gly).

</dd> <dt>

*cbKeyBlob* \[in\]
</dt> <dd>

The size, in bytes, of the *pbKeyBlob* buffer.

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
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* handle is not valid.<br/>                       |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *phKey* parameter is **NULL**.<br/>                            |



 

## Remarks

You can use the **SslImportKey** function to import session keys as a part of the process of transferring session keys from one process to another.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

 




