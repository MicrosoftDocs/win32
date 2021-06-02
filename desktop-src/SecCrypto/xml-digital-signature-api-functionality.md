---
description: CryptXML provides a low level set of APIs that allow applications to create and verify enveloped, enveloping, and detached signatures. You can use CryptXML to create and verify content stored in signature object elements, including manifests.
ms.assetid: 962dffdb-caa6-4aa7-b5c6-3a9de8cfaf6c
title: XML Digital Signature API Functionality
ms.topic: article
ms.date: 05/31/2018
---

# XML Digital Signature API Functionality

CryptXML provides a low level set of APIs that allow applications to create and verify enveloped, enveloping, and detached signatures. You can use CryptXML to create and verify content stored in signature object elements, including manifests. A public/private, shared key, or an [*X.509*](../secgloss/x-gly.md) certificate or certificate chain can be used to sign and verify the XML [*digital signature*](../secgloss/d-gly.md).

Applications that use CryptXML to verify external references (references that target an external document or file outside of the document context) must resolve the external URIs and retrieve the data to be digested.

For information about the cryptographic algorithms supported by CryptXML, see [XML Digital Signature Cryptographic Algorithms](xml-digital-signature-cryptographic-algorithms.md).

CryptXML provides support for the canonicalization algorithms with the following identifiers.



| Constant                                              | URI value                                                                  |
|-------------------------------------------------------|----------------------------------------------------------------------------|
| wszURI\_CANONICALIZATION\_C14N<br/>             | "https://www.w3.org/TR/2001/REC-xml-c14n-20010315"<br/>               |
| wszURI\_CANONICALIZATION\_C14NC<br/>            | "https://www.w3.org/TR/2001/REC-xml-c14n-20010315\#WithComments"<br/> |
| wszURI\_CANONICALIZATION\_EXSLUSIVE\_C14N<br/>  | "https://www.w3.org/2001/10/xml-exc-c14n\#"<br/>                      |
| wszURI\_CANONICALIZATION\_EXSLUSIVE\_C14NC<br/> | "https://www.w3.org/2001/10/xml-exc-c14n\#WithComments"<br/>          |



 

CryptXML provides support for the enveloped signature transform.



| Constant                                       | URI value                                                           |
|------------------------------------------------|---------------------------------------------------------------------|
| wszURI\_XMLNS\_TRANSFORM\_ENVELOPED<br/> | "https://www.w3.org/2000/09/xmldsig\#enveloped-signature"<br/> |



 

By default, CryptXML does not support XPath or XSLT transforms. If required, applications can implement these transforms on top of CryptXML.

 

 
