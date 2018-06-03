---
Description: Active Directory Rights Management Services (AD RMS) requires that any computer used to encrypt or decrypt content be trusted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0e8bd151-7312-40ca-9d23-4be849031222
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Computer Activation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Computer Activation

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) requires that any computer used to encrypt or decrypt content be trusted. Trust is established by creating a [*machine certificate*](https://www.bing.com/search?q=*machine certificate*) that identifies the computer and signs it into the Pre-production or Production certificate hierarchy. The hierarchy is a certificate chain that begins with a Microsoft root of trust and ends with the machine certificate. Each certificate in the chain signs the one following.

Machine certificates are created on a per-user basis. That is, there is a machine certificate for each user who logs on and activates the computer. The certificate is saved in the user's unique store. Activating a computer that has already been activated overwrites the existing machine certificate for the specified user.

Each machine certificate contains a unique public key. The private key is encrypted and securely stored. The certificate also contains a value that uniquely identifies the computer. If the certificate is transferred between computers, AD RMS will not be able to recompute this value to validate the certificate and will not therefore allow the computer to publish or consume content. Also, each machine certificate is associated with a rights account certificate (RAC) that identifies a user account. For more information about RACs, see [User Activation](user-activation.md). For more information about machine certificates, see [Activating a Computer](activating-a-computer.md).

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Certificate Hierarchy](certificate-hierarchy.md)
</dt> <dt>

[User Activation](user-activation.md)
</dt> </dl>

 

 



