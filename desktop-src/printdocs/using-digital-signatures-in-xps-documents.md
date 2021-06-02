---
description: This topic lists considerations for using the XPS Digital Signature API to add digital signatures to an XPS document.
ms.assetid: 27c28313-d8db-4c40-9972-cb03bdaa125c
title: Using XPS Digital Signature API
ms.topic: article
ms.date: 05/31/2018
---

# Using XPS Digital Signature API

This topic lists considerations for using the XPS Digital Signature API to add digital signatures to an XPS document.

The XPS Digital Signature API enables applications to request users to sign XPS documents and to verify signatures that are found in XPS documents. The XPS Digital Signature API can be applied to an XPS document without loading it into an XPS OM, and it can be used on XPS document streams that are serialized from an XPS OM.

The [XPS Digital Signature API Programming Tasks](#xps-digital-signature-api-programming-tasks) section contains topics that describe how to program with the XPS Digital Signature API. This topic lists the following considerations for using the XPS Digital Signature API when adding digital signature support to an application.

-   [XPS Digital Signature API Programming Tasks](#xps-digital-signature-api-programming-tasks)
-   [Special Notes about XPS Digital Signature API Programming](#special-notes-about-xps-digital-signature-api-programming)
    -   [Verifying Digital Signatures in an XPS Document](#verifying-digital-signatures-in-an-xps-document)
    -   [Digital Signature Signing Policy](#digital-signature-signing-policy)
    -   [Embedding a Certificate Chain](#embedding-a-certificate-chain)
    -   [Using the CERT\_CONTEXT Structure](#using-the-cert\_context-structure)
-   [Related topics](#related-topics)

## XPS Digital Signature API Programming Tasks

This section contains topics that describe how to perform programming tasks by using the XPS Digital Signature API.

-   [Common Digital Signature Programming Tasks](basic-digital-signature-programming-tasks.md)<dl>

[Initialize the Signature Manager](initialize-the-signature-manager.md)  
    [Sign a Document](sign-a-document.md)  
    [Add a Signature Request to an XPS Document](add-a-signature-request-to-a-document.md)  
    [Verify Document Signatures](verify-document-signatures.md)  
    </dl>
-   [Additional Digital Signature Programming Tasks](advanced-digital-signature-programming-tasks.md)<dl>

[Load a Certificate From a File](load-a-certificate-from-a-file.md)  
    [Verify That a Certificate Supports a Signature Method](verify-a-certificate-supports-a-signature-method.md)  
    [Verify the System Supports a Digest Method](verify-a-certificate-supports-a-digest-method.md)  
    [Embed Certificate Chains in a Document](embedding-certificate-trust-chains-in-a-document.md)  
    </dl>

## Special Notes about XPS Digital Signature API Programming

The following topics require some special consideration when you use the XPS Digital Signature API.

-   [Verifying Digital Signatures in an XPS Document](#verifying-digital-signatures-in-an-xps-document)
-   [Digital Signature Signing Policy](#digital-signature-signing-policy)
-   [Embedding a Certificate Chain](#embedding-a-certificate-chain)
-   [Using the CERT\_CONTEXT Structure](#using-the-cert\_context-structure)

### Verifying Digital Signatures in an XPS Document

[**IXpsSignature::Verify**](/windows/desktop/api/xpsdigitalsignature/nf-xpsdigitalsignature-ixpssignature-verify) checks only the signed content to determine that it has not changed since it was signed. **IXpsSignature::Verify** does not verify any of the certificates that were used to sign the document content.

For more information about certificates and cryptography, see [About Cryptography](/windows/desktop/SecCrypto/about-cryptography).

For an example of how to verify document signatures in a program, see [Verify Document Signatures and Certificates](verify-document-signatures.md).

### Digital Signature Signing Policy

The digital signature signing policy determines which parts of an XPS document are signed. One signing policy option is to sign the signature relationships that start from the signature origin part. Because the signature relationships change with each signature that is added, signatures that are made under this policy will break when new signatures are added. Make sure that you understand clearly the implications and effects of setting this policy; otherwise, unexpected or undesired behavior might result.

For more information about signing policies, see [**XPS\_SIGN\_POLICY**](/windows/win32/api/xpsdigitalsignature/ne-xpsdigitalsignature-xps_sign_policy).

### Embedding a Certificate Chain

The certificates that make up the trust chain of a specific certificate can be added to an XPS document. Embedding these certificates can make it easier, in off-line scenarios, for an application to verify the certificates that a digital signature uses.

For more information about how to embed certificates in an XPS document, see [Embed Certificate Chains in a Document](embedding-certificate-trust-chains-in-a-document.md).

### Using the CERT\_CONTEXT Structure

The [**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context) and [**CERT\_INFO**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_info) structures are the main data structures that hold certificate information. For more information about using these structures, see [Using a CERT\_INFO Data Structure](/windows/desktop/SecCrypto/using-a-cert-info-data-structure).

[**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context) structures that are returned by Crypto API functions must be released when they are no longer needed. To release a **CERT\_CONTEXT** structure, call the [**CertFreeCertificateContext**](/windows/desktop/api/wincrypt/nf-wincrypt-certfreecertificatecontext) function.

## Related topics

<dl> <dt>

[Common Digital Signature Programming Tasks](basic-digital-signature-programming-tasks.md)
</dt> <dt>

[Additional Digital Signature Programming Tasks](advanced-digital-signature-programming-tasks.md)
</dt> <dt>

[**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context)
</dt> <dt>

[**CERT\_INFO**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_info)
</dt> <dt>

[**CertFreeCertificateContext**](/windows/desktop/api/wincrypt/nf-wincrypt-certfreecertificatecontext)
</dt> <dt>

[**XPS\_SIGN\_POLICY**](/windows/win32/api/xpsdigitalsignature/ne-xpsdigitalsignature-xps_sign_policy)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 
