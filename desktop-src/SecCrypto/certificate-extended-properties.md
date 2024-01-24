---
description: The data in a certificate, certificate revocation list (CRL), or certificate trust list (CTL) context, including any extensions, is read-only and cannot be changed.
ms.assetid: a9958c59-dc89-4d59-8ad3-6651ea4a1e56
title: Certificate Extended Properties
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Extended Properties

The data in a [*certificate*](../secgloss/c-gly.md), [*certificate revocation list*](../secgloss/c-gly.md) (CRL), or [*certificate trust list*](../secgloss/c-gly.md) (CTL) [*context*](../secgloss/c-gly.md), including any extensions, is read-only and cannot be changed. However, on Microsoft platforms, CryptoAPI certificates also have dynamic extended properties that can be added and changed.

> [!Note]  
> Extended properties are associated with a certificate and are not part of a certificate as issued by a [*certification authority*](../secgloss/c-gly.md) (CA). Extended properties are not available on a certificate when it is used on a non-Microsoft platform.

 

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

For complete lists of currently defined extended certificate properties and descriptions of the meaning and use of each property, see [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty) and [**CertSetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty).

## Related topics

<dl> <dt>

[**CertGetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlcontextproperty)
</dt> <dt>

[**CertGetCTLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetctlcontextproperty)
</dt> <dt>

[**CertSetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcrlcontextproperty)
</dt> <dt>

[**CertSetCTLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetctlcontextproperty)
</dt> </dl>

 

 
