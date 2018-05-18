---
Description: 'Several functions add a certificate context or a link to a context to a store \[Platform Software Development Kit (SDK)\].'
ms.assetid: '0355b254-be52-4af4-9567-ee2df092075f'
title: Working with Certificates in Certificate Stores
---

# Working with Certificates in Certificate Stores

Several functions add a certificate context or a link to a context to a store.

For certificates already in certificate context form:

-   [**CertAddCertificateContextToStore**](certaddcertificatecontexttostore.md)
-   [**CertAddCRLContextToStore**](certaddcrlcontexttostore.md)
-   [**CertAddCTLContextToStore**](certaddctlcontexttostore.md)
-   [**CertAddCertificateLinkToStore**](certaddcertificatelinktostore.md)
-   [**CertAddCRLLinkToStore**](certaddcrllinktostore.md)
-   [**CertAddCTLLinkToStore**](certaddctllinktostore.md)

For certificates that are in encoded form but not full certificate contexts:

-   [**CertAddEncodedCertificateToStore**](certaddencodedcertificatetostore.md)
-   [**CertAddEncodedCRLToStore**](certaddencodedcrltostore.md)
-   [**CertAddEncodedCTLToStore**](certaddencodedctltostore.md)

The following functions delete a certificate, CRL, or CTL from a store by decrementing its reference count by one. If this causes the reference count to become zero, the memory used to store the certificate, CRL, or CTL is freed.

-   [**CertDeleteCertificateFromStore**](certdeletecertificatefromstore.md)
-   [**CertDeleteCRLFromStore**](certdeletecrlfromstore.md)
-   [**CertDeleteCTLFromStore**](certdeletectlfromstore.md)

 

 



