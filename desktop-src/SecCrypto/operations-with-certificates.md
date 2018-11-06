---
Description: CryptoAPI provides functions to work with certificates, certificate revocation lists (CRLs) and certificate trust lists (CTLs).
ms.assetid: 23460329-44ed-4bcb-9727-5c841070f093
title: Operations with Certificates
ms.topic: article
ms.date: 05/31/2018
---

# Operations with Certificates

[*CryptoAPI*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) provides functions to work with [*certificates*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx), [*certificate revocation lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRLs) and [*certificate trust lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CTLs). These include functions for converting encoded types to context types, functions that duplicate objects, and functions that free these objects. These functions encode information into contexts but do not add this context to any store. These functions are [**CertCreateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecertificatecontext), [**CertCreateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecrlcontext), and [**CertCreateCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatectlcontext). Use the appropriate CertFree function to free contexts created by one of these functions.

The CryptoAPI functions to duplicate certificates, CRLs, and CTLs increment the [*reference counter*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) in the specified context and return a pointer to the context. The duplicating functions do not allocate additional space or copy the data from a context into a new memory location. These functions are [**CertDuplicateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecertificatecontext), [**CertDuplicateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecrlcontext), and [**CertDuplicateCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatectlcontext). Contexts created with any of these functions must be freed using the appropriate CertFree function.

The CryptoAPI functions that free certificates, CRLs, and CTLs are [**CertFreeCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatecontext), [**CertFreeCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecrlcontext), and [**CertFreeCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreectlcontext). Each of these functions decreases the [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) in a context. If the reference count reaches zero, the memory allocated for the context is released.

For complete lists of functions for working with certificates, CRLs, and CTLs, see [Certificate and Certificate Store Maintenance Functions](cryptography-functions.md), [Certificate Functions](cryptography-functions.md), [Certificate Revocation List Functions](cryptography-functions.md), and [Certificate Trust List Functions](cryptography-functions.md).

 

 



