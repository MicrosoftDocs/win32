---
Description: The functions CertAddCertificateLinkToStore, CertAddCRLLinkToStore, and CertAddCTLLinkToStore add links to existing contexts into certificate stores rather than adding copies of those contexts.
ms.assetid: 482fb11e-eb59-4de2-a2ad-c1960617e64b
title: Certificate Links
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Links

The functions [**CertAddCertificateLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatelinktostore?branch=master), [**CertAddCRLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcrllinktostore?branch=master), and [**CertAddCTLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddctllinktostore?branch=master) add links to existing contexts into [*certificate stores*](security.c_gly#-security-certificate-store-gly) rather than adding copies of those contexts. Adding links to stores makes the same physical [*certificate*](security.c_gly#-security-certificate-gly), [*CRL*](security.c_gly#-security-certificate-revocation-list-gly), or [*CTL*](security.c_gly#-security-certificate-trust-list-gly) available through several different stores. Changes made to the extended properties of a [*context*](security.c_gly#-security-context-gly) from the store of the original context, or from a store where a link to that context is stored, are available in the store that holds the original context and in all other stores that have links to that context.

For an example that uses [**CertAddCertificateLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatelinktostore?branch=master), see [Example C Program: Certificate Store Operations](example-c-program-certificate-store-operations.md).

![certificate links](images/mancert1.png)

Assume that certificates A.1, A.2, A.3, and A.4 are originally in store A, and certificates B.1, B.2, B.3, and B.4 are originally in store B.

-   The diagram shows a link added in store B to certificate A.2 and a link added in store A to certificate B.2.
-   The original of certificate A.2 is still in store A. The original of B.2 is still in store B.
-   Any changes made to the extended properties of certificate A.2 or certificate B.2 from either store A or store B will be available to both stores.
-   If a copy of certificate A.3 were made and stored in store B, any changes to the extended properties of the original A.3 certificate made from store A would not be visible in the new copy in store B. If changes were made to the extended properties of the copy of certificate A.3 in store B, those changes would not affect the contents of the original A.3 certificate and would not be visible from store A.

 

 



