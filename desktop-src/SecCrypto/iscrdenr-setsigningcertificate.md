---
description: Specifies a signing certificate (also known as the enrollment agent certificate).
ms.assetid: db2437a9-46f6-48c3-9630-82ec556df645
title: ISCrdEnr::setSigningCertificate method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCrdEnr.setSigningCertificate
- SCrdEnr.setSigningCertificate
api_type: 
- COM
api_location: 
- Scrdenrl.dll
---

# ISCrdEnr::setSigningCertificate method

The **setSigningCertificate** method specifies a signing certificate (also known as the *enrollment agent certificate*).

Before enrolling on behalf of users, you must select or set a signing certificate. The [*private key*](../secgloss/p-gly.md) associated with this signing certificate is used to sign a PKCS \#7 request. The PKCS \#7, in turn, contains the user's PKCS \#10 request (which is signed with the user's private key).

## Syntax


```C++
HRESULT setSigningCertificate(
  [in] DWORD dwFlags,
  [in] BSTR bstrCertTemplateName
);
```


```VB

SCrdEnr.setSigningCertificate( _
  ByVal dwFlags, _
  ByVal bstrCertTemplateName _
)
```





## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved for future use. Set this value to zero.

</dd> <dt>

*bstrCertTemplateName* \[in\]
</dt> <dd>

Name of the certificate template for the signing certificate. You can use the value "EnrollmentAgent" if you have obtained an EnrollmentAgent certificate.

</dd> </dl>

## Return value

### VB

If the method succeeds, the method returns S\_OK.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

Before enrolling on behalf of a user, you must first obtain a signing certificate. You can obtain a signing certificate by using the Certificate Manager MMC snap-in. The **setSigningCertificate** method does not obtain the signing certificate but informs the Smart Card Enrollment Control which previously obtained signing certificate to use. The **setSigningCertificate** method searches the caller's "My" store for the most recent signing certificate corresponding to the certificate template specified by *bstrCertTemplateName*.

An alternative to **setSigningCertificate** is **ISCrdEnr::setSigningCertificate**.

After a signing certificate is set, its name can be retrieved by calling [**ISCrdEnr::getSigningCertificateName**](iscrdenr-getsigningcertificatename.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Scrdenrl.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCrdEnr is defined as 753988a1-1357-436d-9cf5-f089bdd67d64<br/>             |



## See also

<dl> <dt>

[**ISCrdEnr**](iscrdenr.md)
</dt> <dt>

[**ISCrdEnr::getSigningCertificateName**](iscrdenr-getsigningcertificatename.md)
</dt> </dl>

 

 
