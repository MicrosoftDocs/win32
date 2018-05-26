---
Description: In the event of a security incident, the revocation or exclusion of a certificate may be necessary.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 84eb9778-a7ba-4266-b929-2683dec8e28f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Deciding How Many Applications to Sign
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Deciding How Many Applications to Sign

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

In the event of a security incident, the revocation or exclusion of a certificate may be necessary. If you have used the certificate to sign several applications, all will become unavailable. Using a new certificate for each application increases the granularity of revocation or exclusion events. When you apply for a Production License Agreement, Microsoft requires that you describe each application that the certificate will be used to sign.

> [!Note]  
> Debug builds should never be signed with the production certificate.

 

## Related topics

<dl> <dt>

[Recommended Software Development Practices](recommended-software-development-practices.md)
</dt> </dl>

 

 



