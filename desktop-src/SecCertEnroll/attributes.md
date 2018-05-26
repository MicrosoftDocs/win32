---
Description: Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate.
ms.assetid: 098be796-dbf9-4332-8450-01ed8b2e6c12
title: Attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Attributes

Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate. Each attribute is a [*Distinguished Encoding Rules*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-distinguished-encoding-rules-gly) (DER) encoded [*Abstract Syntax Notation One*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-abstract-syntax-notation-one-gly) (ASN.1) structure that contains an object identifier (OID) and zero or more values. Attributes are defined by using interfaces included with the Certificate Enrollment API. The following topics discuss attributes in more detail:

-   [Supported Attributes](supported-attributes.md)
-   [Attribute Architecture](attribute-architecture.md)
-   [PKCS \#7 Attributes](pkcs--7-attributes.md)
-   [PKCS \#10 Attributes](pkcs--10-attributes.md)
-   [CMC Attributes](cmc-attributes.md)

 

 



