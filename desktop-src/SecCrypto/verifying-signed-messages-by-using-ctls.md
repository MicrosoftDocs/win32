---
description: One of the advantages of using certificate trust lists (CTLs) is that applications can be designed that can automatically verify signed messages against trusted certificates without bothering the user with dialog boxes.
ms.assetid: e45ea3ae-52bc-49d3-8144-f3becc254f53
title: Verifying Signed Messages by Using CTLs
ms.topic: article
ms.date: 05/31/2018
---

# Verifying Signed Messages by Using CTLs

One of the advantages of using [*certificate trust lists*](../secgloss/c-gly.md) (CTLs) is that applications can be designed that can automatically verify signed messages against trusted certificates without bothering the user with dialog boxes. It also gives a network administrator control sources to be trusted.

The following procedure can be used to verify the signature of a signed message by using a CTL.

**To verify a signed message by using a CTL**

1.  Decode the message as follows:

    1.  Get a pointer to the received message (the encoded [*BLOB*](../secgloss/b-gly.md)).
    2.  Call [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode), passing the necessary arguments.
    3.  Call [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) once, passing in the handle retrieved in step b and a pointer to the data that is to be decoded. This causes the appropriate actions to be taken on the message, depending on the message type.

2.  Verify the signature of the decoded, signed message, and get a pointer to the signer's [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context).

    This can be done by calling [**CryptMsgGetAndVerifySigner**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetandverifysigner), passing the message handle retrieved in step 1c as the *hCryptMsg* parameter. If the function call returns **TRUE**, the signature was verified, and a pointer to the signer's [**PCCERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) is returned in the *ppSigner* parameter.

3.  Confirm that the signer is a trusted source as follows:

    1.  Open the certificate store containing the appropriate CTL.
    2.  Get a pointer to the [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context) by calling [**CertFindCTLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindctlinstore).
    3.  To confirm that the signer is a trusted source, call [**CertFindSubjectInCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindsubjectinctl), passing the pointer retrieved in the previous step in the *pCtlContext* parameter, CTL\_CERT\_SUBJECT\_TYPE in the *dwSubjectType* parameter, and the pointer to the [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) retrieved in step 2 in the *pvSubject* parameter. If the function call returns **TRUE**, the **CERT\_CONTEXT** passed to the function is a trusted source in the CTL.

 

 
