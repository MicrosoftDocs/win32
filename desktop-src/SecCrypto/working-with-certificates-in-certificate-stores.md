---
Description: Several functions add a certificate context or a link to a context to a store \[Platform Software Development Kit (SDK)\].
ms.assetid: 0355b254-be52-4af4-9567-ee2df092075f
title: Working with Certificates in Certificate Stores
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Working with Certificates in Certificate Stores

Several functions add a certificate context or a link to a context to a store.

For certificates already in certificate context form:

-   [**CertAddCertificateContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatecontexttostore?branch=master)
-   [**CertAddCRLContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcrlcontexttostore?branch=master)
-   [**CertAddCTLContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddctlcontexttostore?branch=master)
-   [**CertAddCertificateLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatelinktostore?branch=master)
-   [**CertAddCRLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcrllinktostore?branch=master)
-   [**CertAddCTLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddctllinktostore?branch=master)

For certificates that are in encoded form but not full certificate contexts:

-   [**CertAddEncodedCertificateToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedcertificatetostore?branch=master)
-   [**CertAddEncodedCRLToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedcrltostore?branch=master)
-   [**CertAddEncodedCTLToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedctltostore?branch=master)

The following functions delete a certificate, CRL, or CTL from a store by decrementing its reference count by one. If this causes the reference count to become zero, the memory used to store the certificate, CRL, or CTL is freed.

-   [**CertDeleteCertificateFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletecertificatefromstore?branch=master)
-   [**CertDeleteCRLFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletecrlfromstore?branch=master)
-   [**CertDeleteCTLFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletectlfromstore?branch=master)

 

 



