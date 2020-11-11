---
title: Security Considerations Text Services Framework
description: Security Considerations Text Services Framework
ms.assetid: c1250ca0-3887-4519-888f-2ed436a39917
keywords:
- Text Services Framework (TSF),security
- TSF (Text Services Framework),security
- text services,security
- TSF-enabled applications,security
- security for TSF
- Text Services Framework (TSF),best practices
- TSF (Text Services Framework),best practices
- TSF-enabled applications,best practices
- text services,best practices
- best practices for TSF
- Text Services Framework (TSF),error checking
- TSF (Text Services Framework),error checking
- TSF-enabled applications,error checking
- text services,error checking
- error checking
- Text Services Framework (TSF),digital signatures
- TSF (Text Services Framework),digital signatures
- text services,digital signatures
- TSF-enabled applications,digital signatures
- digital signatures
- Text Services Framework (TSF),LoadLibrary calls
- TSF (Text Services Framework),LoadLibrary calls
- text services,LoadLibrary calls
- TSF-enabled applications,LoadLibrary calls
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations: Text Services Framework

## Best Practices for Developing with TSF

-   **Digital Signatures:** Text service providers should provide digital signatures with their binary executables. A registered text service has access to system threads and could expose information that would otherwise not be accessible. To help ensure stable and secure operation, the user should verify the digital signature of a text service before the text service is allowed to load. See [Introduction to Code Signing](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85)) for the proper procedure to create a digital signature.
-   **Error Checking:** Each method or function call should be checked for success. In the event of failure, the remaining method or function calls should be skipped. Most of the code examples in this documentation have limited error checking, or none at all, to avoid obscuring the point to be illustrated. You should not paste examples from the documentation directly into production code; rather, you should enhance the examples by adding your own error checking.

-   **LoadLibrary Calls:** To obtain a pointer to any of the [TSF functions](text-services-framework-functions.md), you will need to use [LoadLibrary](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [GetProcAddress](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress). However, it is important to follow procedures for formatting the DLL path name, as given in **LoadLibrary** documentation.

## Related topics

<dl> <dt>

[Security Best Practices](/windows/desktop/SecBP/best-practices-for-the-security-apis)
</dt> <dt>

[Introduction to Code Signing](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85))
</dt> <dt>

[TSF functions](text-services-framework-functions.md)
</dt> <dt>

[LoadLibrary](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> <dt>

[GetProcAddress](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress)
</dt> </dl>

 

 