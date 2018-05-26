---
Description: The data in a certificate, certificate revocation list (CRL), or certificate trust list (CTL) context, including any extensions, is read-only and cannot be changed.
ms.assetid: a9958c59-dc89-4d59-8ad3-6651ea4a1e56
title: Certificate Extended Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Extended Properties

The data in a [*certificate*](security.c_gly#-security-certificate-gly), [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL), or [*certificate trust list*](security.c_gly#-security-certificate-trust-list-gly) (CTL) [*context*](security.c_gly#-security-context-gly), including any extensions, is read-only and cannot be changed. However, on Microsoft platforms, CryptoAPI certificates also have dynamic extended properties that can be added and changed.

> [!Note]  
> Extended properties are associated with a certificate and are not part of a certificate as issued by a [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA). Extended properties are not available on a certificate when it is used on a non-Microsoft platform.

 

These properties include data that:

-   Pertains to the private key to be used with the certificate.
-   Indicates the type of hashes to be performed on the certificate.
-   Provides user-defined information associated with the certificate.

On Microsoft platforms, values for these properties are attached to and move with the certificate. Currently predefined properties identified with property IDs include the following properties:

-   These properties tie a certificate to a particular CSP and, within that CSP, to a particular private key:
    -   CERT\_KEY\_PROV\_HANDLE\_PROP\_ID
    -   CERT\_KEY\_PROV\_INFO\_PROP\_ID
    -   CERT\_KEY\_CONTEXT\_PROP\_ID
-   These properties indicate the hashing algorithm to be used when a hashing operation is performed:
    -   CERT\_SHA1\_HASH\_PROP\_ID
    -   CERT\_MD5\_HASH\_PROP\_ID

For complete lists of currently defined extended certificate properties and descriptions of the meaning and use of each property, see [**CertGetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty?branch=master) and [**CertSetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty?branch=master).

## Related topics

<dl> <dt>

[**CertGetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcrlcontextproperty?branch=master)
</dt> <dt>

[**CertGetCTLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetctlcontextproperty?branch=master)
</dt> <dt>

[**CertSetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcrlcontextproperty?branch=master)
</dt> <dt>

[**CertSetCTLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetctlcontextproperty?branch=master)
</dt> </dl>

 

 



