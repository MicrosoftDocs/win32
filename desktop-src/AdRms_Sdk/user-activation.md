---
Description: Active Directory Rights Management Services (AD RMS) requires that any user who intends to publish or consume protected content be trusted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a169d438-6a34-4424-8c5d-772a22eb80b9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: User Activation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User Activation

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) requires that any user who intends to publish or consume protected content be trusted. Trust is established by issuing a [*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*) (RAC) that signs the Active Directory user account into the Pre-production or Production certificate hierarchy. The hierarchy is a certificate chain that begins with a Microsoft root of trust and ends with the RAC. Each certificate in the chain signs the one following.

RACs cannot be transferred between computers. When a RAC is created, AD RMS ties it to the [*machine certificate*](https://www.bing.com/search?q=*machine certificate*) located in the user's store by using the public key in the machine certificate to encrypt the private key associated with the RAC. When a user wants to publish or consume content, AD RMS attempts to verify the RAC by using the machine certificate public key to decrypt the RAC private key. If verification is not successful, the user is not allowed to continue.

User activation is performed by an AD RMS certification web service running on an AD RMS server. A user may have multiple RACs on a computer, issued by the same or different services. User activation must be performed after computer activation. For more information, see [Activating a User](activating-a-user.md).

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Certificate Hierarchy](certificate-hierarchy.md)
</dt> <dt>

[Computer Activation](computer-activation.md)
</dt> </dl>

 

 



