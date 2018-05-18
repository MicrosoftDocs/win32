---
Description: 'CryptoAPI provides functions to work with certificates, certificate revocation lists (CRLs) and certificate trust lists (CTLs).'
ms.assetid: '23460329-44ed-4bcb-9727-5c841070f093'
title: Operations with Certificates
---

# Operations with Certificates

[*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) provides functions to work with [*certificates*](security.c_gly#-security-certificate-gly), [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs) and [*certificate trust lists*](security.c_gly#-security-certificate-trust-list-gly) (CTLs). These include functions for converting encoded types to context types, functions that duplicate objects, and functions that free these objects. These functions encode information into contexts but do not add this context to any store. These functions are [**CertCreateCertificateContext**](certcreatecertificatecontext.md), [**CertCreateCRLContext**](certcreatecrlcontext.md), and [**CertCreateCTLContext**](certcreatectlcontext.md). Use the appropriate CertFree function to free contexts created by one of these functions.

The CryptoAPI functions to duplicate certificates, CRLs, and CTLs increment the [*reference counter*](security.r_gly#-security-reference-count-gly) in the specified context and return a pointer to the context. The duplicating functions do not allocate additional space or copy the data from a context into a new memory location. These functions are [**CertDuplicateCertificateContext**](certduplicatecertificatecontext.md), [**CertDuplicateCRLContext**](certduplicatecrlcontext.md), and [**CertDuplicateCTLContext**](certduplicatectlcontext.md). Contexts created with any of these functions must be freed using the appropriate CertFree function.

The CryptoAPI functions that free certificates, CRLs, and CTLs are [**CertFreeCertificateContext**](certfreecertificatecontext.md), [**CertFreeCRLContext**](certfreecrlcontext.md), and [**CertFreeCTLContext**](certfreectlcontext.md). Each of these functions decreases the [*reference count*](security.r_gly#-security-reference-count-gly) in a context. If the reference count reaches zero, the memory allocated for the context is released.

For complete lists of functions for working with certificates, CRLs, and CTLs, see [Certificate and Certificate Store Maintenance Functions](cryptography-functions.md#certificate-and-certificate-store-maintenance-functions), [Certificate Functions](cryptography-functions.md#certificate-functions), [Certificate Revocation List Functions](cryptography-functions.md#certificate-revocation-list-functions), and [Certificate Trust List Functions](cryptography-functions.md#certificate-trust-list-functions).

 

 



