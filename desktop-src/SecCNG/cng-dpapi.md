---
Description: Microsoft introduced the data protection application programming interface (DPAPI) in Windows 2000.
ms.assetid: 048DEA72-39E1-4129-A554-F7D08442C2D9
title: CNG DPAPI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CNG DPAPI

Microsoft introduced the data protection application programming interface (DPAPI) in Windows 2000. The API consists of two functions, [**CryptProtectData**](https://msdn.microsoft.com/library/windows/desktop/aa380261) and [**CryptUnprotectData**](https://msdn.microsoft.com/library/windows/desktop/aa380882). DPAPI is part of CryptoAPI and was intended for developers who knew very little about using cryptography. The two functions could be used to encrypt and decrypt static data on a single computer.

Cloud computing, however, often requires that content encrypted on one computer be decrypted on another. Therefore, beginning with Windows 8, Microsoft extended the idea of using a relatively straightforward API to encompass cloud scenarios. This new API, called DPAPI-NG, enables you to securely share secrets (keys, passwords, key material) and messages by protecting them to a set of principals that can be used to unprotect them on different computers after proper authentication and authorization. The following principals are currently supported:

-   A group in an Active Directory forest.
-   Web credentials.

For more information, see the following topics:

-   [Protection Providers](protection-providers.md)
-   [Protection Descriptors](protection-descriptors.md)
-   [Protected Data Format](protected-data-format.md)

DPAPI-NG is built on top of Cryptography Next Generation (CNG) and includes the following functions:

-   [**NCryptCreateProtectionDescriptor**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptcreateprotectiondescriptor?branch=master)
-   [**NCryptCloseProtectionDescriptor**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptcloseprotectiondescriptor?branch=master)
-   [**NCryptProtectSecret**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptprotectsecret?branch=master)
-   [**NCryptQueryProtectionDescriptorName**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptqueryprotectiondescriptorname?branch=master)
-   [**NCryptRegisterProtectionDescriptorName**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptregisterprotectiondescriptorname?branch=master)
-   [**NCryptStreamClose**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptstreamclose?branch=master)
-   [**NCryptStreamOpenToProtect**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptstreamopentoprotect?branch=master)
-   [**NCryptStreamOpenToUnprotect**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptstreamopentounprotect?branch=master)
-   [**NCryptStreamUpdate**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptstreamupdate?branch=master)
-   [**NCryptUnprotectSecret**](/windows/win32/NCryptprotect/nf-ncryptprotect-ncryptunprotectsecret?branch=master)

 

 



