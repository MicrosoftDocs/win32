---
Description: To make it more difficult for an interloper to substitute a bogus certificate trust list (CTL) for an existing one, verify the signature on the CTL each time the CTL is used.
ms.assetid: 24ba6955-f6d1-4123-ab39-50385f6e03a0
title: Verifying a CTL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying a CTL

To make it more difficult for an interloper to substitute a bogus [*certificate trust list*](security.c_gly#-security-certificate-trust-list-gly) (CTL) for an existing one, verify the signature on the CTL each time the CTL is used. Do not use a CTL that does not contain a trusted signature.

**To verify a CTL signature**

1.  Open the [*certificate store*](security.c_gly#-security-certificate-store-gly) containing the desired CTL.
2.  Get a handle to a [**CTL\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_ctl_context?branch=master) for the CTL. This can be done by calling any of the functions that return a handle to the **CTL\_CONTEXT**, such as [**CertFindCTLInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindctlinstore?branch=master).
3.  Call [**CryptMsgGetAndVerifySigner**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetandverifysigner?branch=master), passing the [**CTL\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_ctl_context?branch=master) retrieved in step 2 in the *hCryptMsg* parameter, a handle to the certificate store containing the certificate of the trusted source for CTLs in the *rghSignerStore* parameter, and the CMSG\_TRUSTED\_SIGNER\_FLAG in the *dwFlags* parameter. If the function returns **TRUE**, the signature was verified, and a pointer to the CTL signer's [**PCCERT\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_context?branch=master) is returned in the *ppSigner* parameter.

 

 



