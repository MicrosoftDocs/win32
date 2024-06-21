---
description: A data type used as a handle to a CryptoAPI cryptographic service provider (CSP) or CNG CSP.
ms.assetid: 1ad77adb-5960-4965-bddb-5967b982b034
title: HCRYPTPROV_OR_NCRYPT_KEY_HANDLE (Wincrypt.h)
ms.topic: reference
ms.date: 06/21/2024
---

# HCRYPTPROV_OR_NCRYPT_KEY_HANDLE

The **HCRYPTPROV_OR_NCRYPT_KEY_HANDLE** data type is used as a handle to a CryptoAPI [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) or CNG CSP. This handle must be an [**HCRYPTPROV**](hcryptprov.md) handle that has been created by using the [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) function or an **NCRYPT_KEY_HANDLE** handle that has been created by using the [**NCryptOpenKey**](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenkey) function. New applications should always pass in the **NCRYPT_KEY_HANDLE** handle to a CNG CSP.

```C++
typedef ULONG_PTR HCRYPTPROV_OR_NCRYPT_KEY_HANDLE;
```

The following functions use the **HCRYPTPROV_OR_NCRYPT_KEY_HANDLE** data type:

- [FreeCryptProvFromCertEx](freecryptprovfromcertex.md)
- [CertGetCertificateContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatecontextproperty)
- [CertSetCertificateContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certsetcertificatecontextproperty)
- [CryptAcquireCertificatePrivateKey](/windows/win32/api/wincrypt/nf-wincrypt-cryptacquirecertificateprivatekey)

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Header | `Wincrypt.h` |
