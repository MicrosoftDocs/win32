---
description: Retrieves the cipher suite information for a specified protocol, cipher suite, and key type set.
ms.assetid: ab995d9a-48fa-491a-95b1-d15c5b92f1da
title: SslLookupCipherSuiteInfo function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SslLookupCipherSuiteInfo
api_type:
- DllExport
api_location:
- Ncrypt.dll
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

The handle to the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

</dd> <dt>

*dwProtocol* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Protocol Identifier**](https://msdn.microsoft.com/library/Hh971257(v=VS.85).aspx) values.

</dd> <dt>

*dwCipherSuite* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Cipher Suite Identifiers**](https://msdn.microsoft.com/library/Hh971253(v=VS.85).aspx) values.

</dd> <dt>

*dwKeyType* \[in\]
</dt> <dd>

One of the [**CNG SSL Provider Key Type Identifiers**](https://msdn.microsoft.com/library/Hh971256(v=VS.85).aspx) values.

</dd> <dt>

*pCipherSuite* \[out\]
</dt> <dd>

The address of a buffer that contains a [**NCRYPT\_SSL\_CIPHER\_SUITE**](https://www.bing.com/search?q=**NCRYPT\_SSL\_CIPHER\_SUITE**) structure in which to write the cipher suite information.

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



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

