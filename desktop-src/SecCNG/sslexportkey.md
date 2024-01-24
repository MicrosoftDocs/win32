---
description: Returns an Secure Sockets Layer protocol (SSL) session key or public ephemeral key into a serialized BLOB.
ms.assetid: c978e6ac-a535-4625-8598-4aa16484dcad
title: SslExportKey function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslExportKey
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslExportKey function

The **SslExportKey** function returns an [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) [*session key*](/windows/desktop/SecGloss/s-gly) or public ephemeral key into a serialized [*BLOB*](/windows/desktop/SecGloss/b-gly).

## Syntax


```C++
SECURITY_STATUS WINAPI SslExportKey(
  _In_      NCRYPT_PROV_HANDLE hSslProvider,
  _In_      NCRYPT_KEY_HANDLE  hKey,
  _In_      LPCWSTR            pszBlobType,
  _Out_opt_ PBYTE              pbOutput,
  _In_      DWORD              cbOutput,
  _Out_     DWORD              *pcbResult,
  _In_      DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the SSL protocol provider instance.

</dd> <dt>

*hKey* \[in\]
</dt> <dd>

The handle of the key to export.

When you are not specifying a key, set this parameter to **NULL**.

> [!Note]  
> A *hKey* handle is obtained by calling the [**SslOpenPrivateKey**](sslopenprivatekey.md) function. Handles obtained from the [**NCryptOpenKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptopenkey) function are not supported.

 

</dd> <dt>

*pszBlobType* \[in\]
</dt> <dd>

A null-terminated Unicode string that contains an identifier that specifies the type of BLOB to export. This can be one of the following values.



| Value                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BCRYPT_DH_PUBLIC_BLOB"></span><span id="bcrypt_dh_public_blob"></span><dl> <dt>**BCRYPT\_DH\_PUBLIC\_BLOB**</dt> </dl>    | Export a Diffie-Hellman [*public key*](/windows/desktop/SecGloss/p-gly). The *pbOutput* buffer receives a [**BCRYPT\_DH\_KEY\_BLOB**](/windows/desktop/api/Bcrypt/ns-bcrypt-bcrypt_dh_key_blob) structure immediately followed by the key data.<br/>                                                                                                               |
| <span id="BCRYPT_ECCPUBLIC_BLOB"></span><span id="bcrypt_eccpublic_blob"></span><dl> <dt>**BCRYPT\_ECCPUBLIC\_BLOB**</dt> </dl>     | Export an [*elliptic curve cryptography*](/windows/desktop/SecGloss/e-gly) (ECC) public key. The *pbOutput* buffer receives a [**BCRYPT\_ECCKEY\_BLOB**](/windows/desktop/api/Bcrypt/ns-bcrypt-bcrypt_ecckey_blob) structure immediately followed by the key data.<br/>                                                          |
| <span id="BCRYPT_OPAQUE_KEY_BLOB"></span><span id="bcrypt_opaque_key_blob"></span><dl> <dt>**BCRYPT\_OPAQUE\_KEY\_BLOB**</dt> </dl> | Export a symmetric key in a format that is specific to a single [*cryptographic service provider*](/windows/desktop/SecGloss/c-gly) (CSP). Opaque BLOBs are not transferable and must be imported by using the same *cryptographic service provider* (CSP) that generated the BLOB.<br/> |
| <span id="BCRYPT_RSAPUBLIC_BLOB"></span><span id="bcrypt_rsapublic_blob"></span><dl> <dt>**BCRYPT\_RSAPUBLIC\_BLOB**</dt> </dl>     | Export an RSA public key. The *pbOutput* buffer receives a [**BCRYPT\_RSAKEY\_BLOB**](/windows/desktop/api/Bcrypt/ns-bcrypt-bcrypt_rsakey_blob) structure immediately followed by the key data.<br/>                                                                                                                                                                                                |



 

</dd> <dt>

*pbOutput* \[out, optional\]
</dt> <dd>

The address of a buffer that receives the [*key BLOB*](/windows/desktop/SecGloss/k-gly). The *cbOutput* parameter contains the size of this buffer. If this parameter is **NULL**, this function will place the required size, in bytes, in the **DWORD** pointed to by the *pcbResult* parameter.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The size, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

The address of a **DWORD** variable that receives the number of bytes copied to the *pbOutput* buffer. If the *pbOutput* parameter is set to **NULL** when the function is called, the required size for the *pbOutput* buffer, in bytes, is returned in the **DWORD** pointed to by this parameter.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                    | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the provided handles is not valid.<br/> |



 

## Remarks

The **SslExportKey** function facilitates transporting session keys from one process to another as well as exporting the public portion an ephemeral key.

When exporting session keys, the BLOB type is opaque, meaning that the format of the BLOB is irrelevant as long as both the **SslExportKey** and [**SslImportKey**](sslimportkey.md) functions can interpret it.

When exporting the public portion of an ephemeral key the BLOB type must be the appropriate type, such as **NCRYPT\_DH\_PUBLIC\_BLOB** or **NCRYPT\_ECCPUBLIC\_BLOB**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

