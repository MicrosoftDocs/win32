---
description: XML is an industry standard for describing structured data. An XML Digital Signature is an XML representation of a digital signature that provides the ability to verify the origin and integrity of XML document and externally referenced data.
ms.assetid: 02ca8d9b-be08-4b15-895f-9c8c4b0ed536
title: XML Digital Signature Overview
ms.topic: article
ms.date: 05/31/2018
---

# XML Digital Signature Overview

XML is an industry standard for describing structured data. An XML Digital Signature is an XML representation of a [*digital signature*](../secgloss/d-gly.md) that provides the ability to verify the origin and integrity of XML document and externally referenced data. XML digital signatures can be used to sign arbitrary data, including an XML document or fragment, an HTML page, plain text, or binary-encoded data such as a JPEG file.

The XML digital signature format supported by the CryptXML digital signature API is specified by the XML Signature Syntax and Processing (Second Edition) W3C recommendation.

The CryptXML digital signature implements support for the required signature types, cryptographic algorithms, canonicalization algorithms, and the specified enveloped transform.

Developers can extend the default set of cryptographic algorithms supported by CryptXML by creating cryptographic extension DLLs. Developers can also create their own custom transforms and canonicalization algorithms on top of CryptXML API. Developers can use the CryptXML APIs with the Windows certificate APIs.

 

 
