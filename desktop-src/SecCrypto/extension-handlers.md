---
description: Beginning with X.509 Certificate format Version 3, a certificate may contain certificate extensions.
ms.assetid: fb106cab-8a61-4a83-8fb4-7c045d905575
title: Extension Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Extension Handlers

Beginning with [*X.509*](../secgloss/x-gly.md) Certificate format Version 3, a certificate may contain certificate extensions. (For the contents of an X.509 Certificate, see [Certificate Properties](certificate-properties.md).) These extensions indicate additional information. For example, an extension can indicate additional subject identification information, or it can indicate key usage information, which specifies the tasks (such as signature or encryption) for which a key can be used. A set of standard extensions is defined for application use, and extensions may also be customized.

Each extension has an associated object identifier string that identifies the type of additional information and a data structure that contains this information. For example, the key usage object identifier is "2.5.29.15", which indicates key usage information. Its associated data structure is a [**CRYPT\_BIT\_BLOB**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_bit_blob) (bitfield) specifying how the key can be used.

An extension can be added to a certificate before it is issued. When the certificate is issued, any enabled extensions are part of the certificate. If an extension is marked critical, its use must be known by the using application, and the application must adhere to the intent or value of the extension. Certificate Services allows extensions to be set on a non-issued certificate through methods provided by [**ICertAdmin**](/windows/desktop/api/Certadm/nn-certadm-icertadmin) and [**ICertServerPolicy**](/windows/desktop/api/Certif/nn-certif-icertserverpolicy). For details about certificate extensions, see [**CERT\_EXTENSION**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_extension) in the CryptoAPI documentation. For information about common certificate extension data structures, see [X.509 Certificate Extension Structures](cryptography-structures.md).

The extension handler is a COM object that provides routines for encoding the more complex, but commonly used extensions and data types, such as IA5String or PrintableString.

Extensions that have the data types **DATE**, **LONG**, and **BSTR** do not require an extension handler. The policy module simply calls [**ICertServerPolicy::SetCertificateExtension**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateextension) with the *Type* parameter set to a value representing the extension data type: PROPTYPE\_DATE, PROPTYPE\_LONG, or PROPTYPE\_STRING. It then passes the extension to the server engine. The server engine, in turn, performs the [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) encoding before storing the extension in the certificate.

However, extensions that have data types other than these default types must be ASN.1 encoded by an extension handler before the policy module passes them to the server engine. When the policy module calls [**ICertServerPolicy::SetCertificateExtension**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateextension) to pass an ASN.1-encoded extension to the server engine, it must set the *Type* parameter to PROPTYPE\_BINARY. The server engine then simply stores this encoded extension in the certificate.

The default extension handler, Certenc.dll, exports a number of **ICertEncodeXXX** interfaces and can be called by the policy module. The necessary type information is also contained in Certencl.dll which is supplied in the Platform Software Development Kit (SDK). Each interface provides an **Encode** method that returns an ASN.1-encoded certificate extension to the policy module in a binary format. The policy module can then set the extension in a certificate by calling the [**ICertServerPolicy::SetCertificateExtension**](/windows/desktop/api/Certif/nf-certif-icertserverpolicy-setcertificateextension) method.

For more information, see [Writing Custom Extension Handlers](writing-custom-extension-handlers.md).

 

 
