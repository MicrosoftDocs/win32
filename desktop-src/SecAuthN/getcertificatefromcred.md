---
description: Gets the certificate from the user credential.
ms.assetid: 3C79D049-89DC-4AF5-8C0A-5B7EBBBD69D3
title: GetCertificateFromCred function (Lsaidprov.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCertificateFromCred
api_type: 
- HeaderDef
api_location: 
- Lsaidprov.h
---

# GetCertificateFromCred function

Gets the certificate from the user credential.

## Syntax


```C++
NTSTATUS GetCertificateFromCred(
  _In_  PVOID  ProviderHandle,
  _In_  HANDLE ClientToken,
  _In_  PVOID  SuppliedCred,
  _In_  ULONG  SuppliedCredSize,
  _Out_ PVOID  *CertContext
);
```



## Parameters

<dl> <dt>

*ProviderHandle* \[in\]
</dt> <dd>

Identity provider handle.

</dd> <dt>

*ClientToken* \[in\]
</dt> <dd>

Token of the caller who is retrieving the certificate.

</dd> <dt>

*SuppliedCred* \[in\]
</dt> <dd>

A pointer to a [**SECPKG\_SUPPLIED\_CREDENTIAL**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_supplied_credential) structure that contains the credential of an online ID whose certificate is requested. The identity provider must validate the input data as if it is coming from an untrusted source.

</dd> <dt>

*SuppliedCredSize* \[in\]
</dt> <dd>

The size, in bytes, of the *SuppliedCred* buffer.

</dd> <dt>

*CertContext* \[out\]
</dt> <dd>

If the function succeeds, this parameter is a pointer to the returned CCERT\_CONTEXT pointer. When you have finished using the certificate context, release it by calling the [**CertFreeCertificateContext**](/windows/desktop/api/wincrypt/nf-wincrypt-certfreecertificatecontext) function.

</dd> </dl>

## Return value

If the function succeeds, the function returns STATUS\_SUCCESS.

If the function fails, the function may return one of the following NTSTATUS error codes.



| Return value                                                                                            | Description                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>STATUS\_NOT\_SUPPORTED</dt> </dl>       | The identity provider does not recognize the credential type of the supplied credential. LSA will try the next identity provider.<br/>                                           |
| <dl> <dt>STATUS\_LOGON\_FAILURE</dt> </dl>       | The credential is incorrect.<br/>                                                                                                                                                |
| <dl> <dt>STATUS\_INVALID\_PARAMETER</dt> </dl>   | A parameter is not valid. The credential may be in an incorrect format and not in the defined [**SECPKG\_SUPPLIED\_CREDENTIAL**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_supplied_credential) structure.<br/> |
| <dl> <dt>STATUS\_NETWORK\_UNREACHABLE</dt> </dl> | The identity provider cannot contact the cloud to obtain the certificate.<br/>                                                                                                   |
| <dl> <dt>STATUS\_PASSWORD\_EXPIRED</dt> </dl>    | The account password has expired.<br/>                                                                                                                                           |
| <dl> <dt>STATUS\_ACCOUNT\_LOCKED\_OUT</dt> </dl> | The account has been locked out. <br/>                                                                                                                                           |
| <dl> <dt>Others</dt> </dl>                       | Other provider-specific error codes. <br/>                                                                                                                                       |



 

## Remarks

Before fetching the certificate from the cloud, the identity provider should check that there is a valid certificate for this user in the user's "MY" certificate store. If a valid certificate exists, the provider should return this certificate to avoid unnecessary network traffic.

The identity provider can also cache the certificate locally as long as it is protected from the current user.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Lsaidprov.h</dt> </dl> |



 

