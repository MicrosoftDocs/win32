---
description: Several functions add a certificate context or a link to a context to a store \[Platform Software Development Kit (SDK)\].
ms.assetid: 0355b254-be52-4af4-9567-ee2df092075f
title: Working with Certificates in Certificate Stores
ms.topic: article
ms.date: 05/31/2018
---

# Working with Certificates in Certificate Stores

Several functions add a certificate context or a link to a context to a store.

For certificates already in certificate context form:

-   [**CertAddCertificateContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatecontexttostore)
-   [**CertAddCRLContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrlcontexttostore)
-   [**CertAddCTLContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddctlcontexttostore)
-   [**CertAddCertificateLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatelinktostore)
-   [**CertAddCRLLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrllinktostore)
-   [**CertAddCTLLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddctllinktostore)

For certificates that are in encoded form but not full certificate contexts:

-   [**CertAddEncodedCertificateToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcertificatetostore)
-   [**CertAddEncodedCRLToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcrltostore)
-   [**CertAddEncodedCTLToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedctltostore)

The following functions delete a certificate, CRL, or CTL from a store by decrementing its reference count by one. If this causes the reference count to become zero, the memory used to store the certificate, CRL, or CTL is freed.

-   [**CertDeleteCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecertificatefromstore)
-   [**CertDeleteCRLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecrlfromstore)
-   [**CertDeleteCTLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletectlfromstore)

 

 



