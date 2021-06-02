---
description: The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate.
ms.assetid: 'f2a6854d-1831-489f-adf6-31a0b26511e3'
title: Extensions (Certificate Enrollment API)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Extensions
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Extensions (Certificate Enrollment API)

The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate. The extensions provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more. You can use the [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) interface to define an extension value. Many of the common extensions can be created by using predefined interfaces derived from **IX509Extension**. A collection of extensions is added to a certificate request by including the collection in the request attributes. For more information, see the following topics:

-   [Supported Extensions](supported-extensions.md)
-   [PKCS \#10 Extensions](pkcs--10-extensions.md)
-   [CMC Extensions](cmc-extensions.md)

 

 



