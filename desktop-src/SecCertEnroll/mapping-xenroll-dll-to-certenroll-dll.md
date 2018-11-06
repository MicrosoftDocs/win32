---
Description: The Xenroll.dll library has been removed from the operating system and replaced by CertEnroll.dll.
ms.assetid: ec28fbdc-9198-472a-8976-7b5db09069a6
title: Mapping Xenroll.dll to CertEnroll.dll
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Xenroll.dll to CertEnroll.dll

Prior to Windows Vista, the Certificate Enrollment Control was implemented in Xenroll.dll. The Xenroll.dll library has been removed from the operating system and replaced by CertEnroll.dll.

Xenroll attempted to implement two parallel sets of interfaces. [**ICEnroll**](https://msdn.microsoft.com/library/windows/desktop/aa382482), [**ICEnroll2**](https://msdn.microsoft.com/library/windows/desktop/aa382484), [**ICEnroll3**](https://msdn.microsoft.com/library/windows/desktop/aa382486), and [**ICEnroll4**](https://msdn.microsoft.com/library/windows/desktop/aa382488) were Automation-compliant and compatible with scripting languages. The corresponding interfaces—[**IEnroll**](https://msdn.microsoft.com/library/windows/desktop/aa385494), [**IEnroll2**](https://msdn.microsoft.com/library/windows/desktop/aa385495), and [**IEnroll4**](https://msdn.microsoft.com/library/windows/desktop/aa385496)—could not be scripted but were more convenient for C++ programmers. As they evolved, the two sets of interfaces did not remain synchronized. In particular, the set of dual interfaces represented most recently by **ICEnroll4** defines only a subset of the functionality defined by **IEnroll4**.

CertEnroll.dll implements a larger and more structured set of Automation-compliant COM interfaces. The following topics discuss how Xenroll.dll maps to CertEnroll.dll for different types of functionality.

-   [Certificate Request Functions](certificate-request-functions.md)
-   [Certificate Response Functions](certificate-response-functions.md)
-   [Attribute Functions](attribute-functions.md)
-   [Extension Functions](extension-functions.md)
-   [External Property Functions](external-property-functions.md)
-   [Private and Public Key Functions](private-and-public-key-functions.md)
-   [Cryptographic Service Provider Functions](cryptographic-service-provider-functions.md)
-   [Certificate Store Functions](certificate-store-functions.md)
-   [Personal Information Exchange Functions](personal-information-exchange-functions.md)
-   [Helper Functions](helper-functions.md)

## Related topics

<dl> <dt>

[Using the Certificate Enrollment API](about-the-certificate-enrollment-api.md)
</dt> </dl>

 

 



