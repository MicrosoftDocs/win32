---
title: ADSI Error Codes
description: All ADSI error codes are returned as COM HRESULT values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 573889e4-37af-4aca-afd7-ef06bcf8aa0d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,reference,error codes
- error codes ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Error Codes

All ADSI error codes are returned as COM **HRESULT** values. They can be grouped into the following four types:

-   [Generic COM error codes](generic-com-error-codes.md)
-   [Generic ADSI error codes](generic-adsi-error-codes.md)
-   [Win32 error codes for ADSI](win32-error-codes-for-adsi.md)
-   [LDAP error codes for ADSI](ldap-error-codes-for-adsi.md)

In addition, certain interfaces provide additional error information, known as ADSI extended error messages, which can be obtained using the [**ADsGetLastError**](/windows/win32/Adshlp/nf-adshlp-adsgetlasterror?branch=master) function.

Finally, the C++ [example code](code-example-for-working-with-adsi-error-messages.md) shown in this section shows how to work ADSI error messages.

 

 




