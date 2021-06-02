---
description: Attributes (Certificate Enrollment API) - Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate.
ms.assetid: '6116e61e-3ec5-4992-90ab-e3c7ced291b6'
title: Attributes (Certificate Enrollment API)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attributes
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attributes (Certificate Enrollment API)

Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate. Each attribute is a [*Distinguished Encoding Rules*](/windows/desktop/SecGloss/d-gly) (DER) encoded [*Abstract Syntax Notation One*](/windows/desktop/SecGloss/a-gly) (ASN.1) structure that contains an object identifier (OID) and zero or more values. Attributes are defined by using interfaces included with the Certificate Enrollment API. The following topics discuss attributes in more detail:

-   [Supported Attributes](supported-attributes.md)
-   [Attribute Architecture](attribute-architecture.md)
-   [PKCS \#7 Attributes](pkcs--7-attributes.md)
-   [PKCS \#10 Attributes](pkcs--10-attributes.md)
-   [CMC Attributes](cmc-attributes.md)

 

 
