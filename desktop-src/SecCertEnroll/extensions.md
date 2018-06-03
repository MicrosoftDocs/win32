---
Description: The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate.
ms.assetid: ca8df7a4-caa4-4fe7-81a8-8fce372454f4
title: Extensions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extensions

The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate. The extensions provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more. You can use the [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) interface to define an extension value. Many of the common extensions can be created by using predefined interfaces derived from **IX509Extension**. A collection of extensions is added to a certificate request by including the collection in the request attributes. For more information, see the following topics:

-   [Supported Extensions](supported-extensions.md)
-   [PKCS \#10 Extensions](pkcs--10-extensions.md)
-   [CMC Extensions](cmc-extensions.md)

 

 



