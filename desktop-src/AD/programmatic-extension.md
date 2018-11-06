---
title: Programmatic Extension
description: Programmatic extensions have several merits, however, an application is opaque; the administrator must trust the documentation included with the setup application.
ms.assetid: e2837757-f887-4d17-a9d2-8989533a3d8e
ms.tgt_platform: multiple
keywords:
- Programmatic Extension
ms.topic: article
ms.date: 05/31/2018
---

# Programmatic Extension

The benefit of an LDIF file is that the administrator can examine its function. However, the schema can also be extended programmatically. Programmatic extensions have several merits, but an application is opaque; the administrator must trust the documentation included with the setup application. Use of programmatic schema extensions may be a barrier to deployment for applications that use them. A programmatic extension is invariant; it is a Windows NT executable. The binary cannot be tampered with, unlike an LDIF or .csv file, which can be edited inadvertently or maliciously.

Benefits of an LDIF file include:

-   Applications can detect and recover from errors and provide user feedback.
-   Applications can handle Unicode without resorting to Base64 encoding.
-   Applications can leverage Windows Installer setup APIs.
-   Applications can be signed to establish authenticity.

 

 




