---
Description: One of the advantages of using certificate trust lists (CTLs) is that applications can be designed that can automatically verify signed messages against trusted certificates without bothering the user with dialog boxes.
ms.assetid: e45ea3ae-52bc-49d3-8144-f3becc254f53
title: Verifying Signed Messages by Using CTLs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying Signed Messages by Using CTLs

One of the advantages of using [*certificate trust lists*](security.c_gly#-security-certificate-trust-list-gly) (CTLs) is that applications can be designed that can automatically verify signed messages against trusted certificates without bothering the user with dialog boxes. It also gives a network administrator control sources to be trusted.

The following procedure can be used to verify the signature of a signed message by using a CTL.

**To verify a signed message by using a CTL**

1.  Decode the message as follows:

    1.  Get a pointer to the received message (the encoded [*BLOB*](security.b_gly#-security-blob-gly)).
    2.  Call [**CryptMsgOpenToDecode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentodecode?branch=master), passing the necessary arguments.
    3.  Call [**CryptMsgUpdate**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgupdate?branch=master) once, passing in the handle retrieved in step b and a pointer to the data that is to be decoded. This causes the appropriate actions to be taken on the message, depending on the message type.

2.  Verify the signature of the decoded, signed message, and get a pointer to the signer's [**CERT\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_context?branch=master).

    This can be done by calling [**CryptMsgGetAndVerifySigner**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetandverifysigner?branch=master), passing the message handle retrieved in step 1c as the *hCryptMsg* parameter. If the function call returns **TRUE**, the signature was verified, and a pointer to the signer's [**PCCERT\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_context?branch=master) is returned in the *ppSigner* parameter.

3.  Confirm that the signer is a trusted source as follows:

    1.  Open the certificate store containing the appropriate CTL.
    2.  Get a pointer to the [**CTL\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_ctl_context?branch=master) by calling [**CertFindCTLInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindctlinstore?branch=master).
    3.  To confirm that the signer is a trusted source, call [**CertFindSubjectInCTL**](/windows/win32/Wincrypt/nf-wincrypt-certfindsubjectinctl?branch=master), passing the pointer retrieved in the previous step in the *pCtlContext* parameter, CTL\_CERT\_SUBJECT\_TYPE in the *dwSubjectType* parameter, and the pointer to the [**CERT\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_context?branch=master) retrieved in step 2 in the *pvSubject* parameter. If the function call returns **TRUE**, the **CERT\_CONTEXT** passed to the function is a trusted source in the CTL.

 

 



