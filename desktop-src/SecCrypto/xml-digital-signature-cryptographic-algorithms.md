---
description: CryptXML natively supports the URIs listed below.
ms.assetid: 012bad01-228a-4bb0-b883-0c2c7abd9271
title: XML Digital Signature Cryptographic Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# XML Digital Signature Cryptographic Algorithms

CryptXML natively supports the URIs listed below. If support is required for cryptographic algorithms and transforms that are not part of the native support, you can use [Cryptography API: Next Generation](../seccng/cng-portal.md) and [XML Digital Signature Cryptographic Extensions](xml-digital-signature-cryptographic-extensions.md) to support new algorithms.

## Supported URIs

Digest Methods



| Constant                                 | URI value                                                   |
|------------------------------------------|-------------------------------------------------------------|
| wszURI\_XMLNS\_DIGSIG\_SHA1<br/>   | "https://www.w3.org/2000/09/xmldsig\#sha1"<br/>        |
| wszURI\_XMLNS\_DIGSIG\_SHA256<br/> | "https://www.w3.org/2001/04/xmlenc\#sha256"<br/>       |
| wszURI\_XMLNS\_DIGSIG\_SHA384<br/> | "https://www.w3.org/2001/04/xmldsig-more\#sha384"<br/> |
| wszURI\_XMLNS\_DIGSIG\_SHA512<br/> | "https://www.w3.org/2001/04/xmlenc\#sha512"<br/>       |



 

Signature Methods



| Constant                                        | URI value                                                         |
|-------------------------------------------------|-------------------------------------------------------------------|
| wszURI\_XMLNS\_DIGSIG\_RSA\_SHA1<br/>     | "https://www.w3.org/2000/09/xmldsig\#rsa-sha1"<br/>          |
| wszURI\_XMLNS\_DIGSIG\_DSA\_SHA1<br/>     | "https://www.w3.org/2000/09/xmldsig\#dsa-sha1"<br/>          |
| wszURI\_XMLNS\_DIGSIG\_RSA\_SHA256<br/>   | "https://www.w3.org/2001/04/xmldsig-more\#rsa-sha256"<br/>   |
| wszURI\_XMLNS\_DIGSIG\_RSA\_SHA384<br/>   | "https://www.w3.org/2001/04/xmldsig-more\#rsa-sha384"<br/>   |
| wszURI\_XMLNS\_DIGSIG\_RSA\_SHA512<br/>   | "https://www.w3.org/2001/04/xmldsig-more\#rsa-sha512"<br/>   |
| wszURI\_XMLNS\_DIGSIG\_ECDSA\_SHA1<br/>   | "https://www.w3.org/2001/04/xmldsig-more\#ecdsa-sha1"<br/>   |
| wszURI\_XMLNS\_DIGSIG\_ECDSA\_SHA256<br/> | "https://www.w3.org/2001/04/xmldsig-more\#ecdsa-sha256"<br/> |
| wszURI\_XMLNS\_DIGSIG\_ECDSA\_SHA384<br/> | "https://www.w3.org/2001/04/xmldsig-more\#ecdsa-sha384"<br/> |
| wszURI\_XMLNS\_DIGSIG\_ECDSA\_SHA512<br/> | "https://www.w3.org/2001/04/xmldsig-more\#ecdsa-sha512"<br/> |
| wszURI\_XMLNS\_DIGSIG\_HMAC\_SHA1<br/>    | "https://www.w3.org/2000/09/xmldsig\#hmac-sha1"<br/>         |
| wszURI\_XMLNS\_DIGSIG\_HMAC\_SHA256<br/>  | "https://www.w3.org/2001/04/xmldsig-more\#hmac-sha256"<br/>  |
| wszURI\_XMLNS\_DIGSIG\_HMAC\_SHA384<br/>  | "https://www.w3.org/2001/04/xmldsig-more\#hmac-sha384"<br/>  |
| wszURI\_XMLNS\_DIGSIG\_HMAC\_SHA512<br/>  | "https://www.w3.org/2001/04/xmldsig-more\#hmac-sha512"<br/>  |



 

 

 
