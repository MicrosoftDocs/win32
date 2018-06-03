---
Description: Beginning with Windows Vista, the client component of Active Directory Rights Management Services (AD RMS) is installed with the operating system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9321f2e1-4020-448a-bcbe-c84d8f0598a4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Client
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Client

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Beginning with Windows Vista, the client component of Active Directory Rights Management Services (AD RMS) is installed with the operating system. You can download it for prior operating systems from the following locations.

-   [32-bit RMS client v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=67736)
-   [64-bit RMS client v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=67935)

The AD RMS client, implemented in Msdrm.dll, exposes functionality that enables users to create, publish, and consume protected (encrypted) content. Specifically, an AD RMS-enabled application can leverage the client to perform the following tasks:

-   Send a request to an AD RMS activation service to issue a machine certificate that identifies a computer by signing it into the AD RMS certificate hierarchy. For more information, see [Activating a Computer](activating-a-computer.md).
-   Send a request to an AD RMS activation service to issue a rights account certificate that signs an Active Directory user account into the AD RMS certificate hierarchy and associates the user with a specific computer. For more information, see [Activating a User](activating-a-user.md).
-   Create an [*issuance license*](https://www.bing.com/search?q=*issuance license*) that lists the users who can decrypt protected content and the rights that can be made available to them. The application can send a request to an AD RMS licensing service to sign the issuance license online or it can request a client licensor certificate that can be used to sign the license offline. For more information, see [Creating and Using Issuance Licenses](creating-an-issuance-license.md).
-   Encrypt the content and make it available for authenticated and authorized users. For more information, see [Encrypting Content](encrypting-content.md).
-   Acquire an [*end-user license*](https://www.bing.com/search?q=*end-user license*) for a specific user, decrypt the content, and enforce the rights enumerated in the license. For more information, see [Decrypting Content](decrypting-content.md).

## Related topics

<dl> <dt>

[AD RMS Overview](ad-rms-overview.md)
</dt> </dl>

 

 



