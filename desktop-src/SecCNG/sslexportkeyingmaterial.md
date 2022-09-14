---
description: Exports keying material per the RFC 5705 standard.
ms.assetid: 19624852-B1A6-4BB4-96AF-0457834DA294
title: SslExportKeyingMaterial function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslExportKeyingMaterial
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslExportKeyingMaterial function

Exports keying material per the [RFC 5705 standard](https://tools.ietf.org/html/rfc5705). This function uses the TLS pseudorandom function to produce a byte buffer of keying material. It takes a reference to the master secret, the disambiguating ASCII label, client and server random values, and optionally the application context data.

## Syntax


```C++
SECURITY_STATUS WINAPI SslExportKeyingMaterial(
  _In_     NCRYPT_PROV_HANDLE hSslProvider,
  _In_     NCRYPT_KEY_HANDLE  hMasterKey,
  _In_     PCHAR              sLabel,
  _In_     PBYTE              pbRandoms,
  _In_     DWORD              cbRandoms,
  _In_opt_ PBYTE              pbContextValue,
  _In_     WORD               cbContextValue,
  _Out_    PBYTE              pbOutput,
  _In_     DWORD              cbOutput,
  _In_     DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the TLS protocol provider instance.

</dd> <dt>

*hMasterKey* \[in\]
</dt> <dd>

The handle of the master key object that will be used to create the keying material to br exported.

</dd> <dt>

*sLabel* \[in\]
</dt> <dd>

a NUL-terminated ASCII label string. Schannel will remove the terminating NUL character before passing it to the pseudorandom function.

</dd> <dt>

*pbRandoms* \[in\]
</dt> <dd>

A pointer to a buffer that contains a concatenation of the *client\_random* and *server\_random* values of the TLS connection.

</dd> <dt>

*cbRandoms* \[in\]
</dt> <dd>

The length, in bytes, of the *pbRandoms* buffer.

</dd> <dt>

*pbContextValue* \[in, optional\]
</dt> <dd>

A pointer to a buffer that contains the application context. If *pbContextValue* is **NULL**, *cbContextValue* must be zero.

</dd> <dt>

*cbContextValue* \[in\]
</dt> <dd>

The length, in bytes, of the *pbContextValue* buffer.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

The address of a buffer that receives the exported keying material. The *cbOutput* parameter contains the size of this buffer. This value cannot be **NULL**.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbOutput* buffer. Must be greater than zero.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Not used. Must be set to zero.

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

 




