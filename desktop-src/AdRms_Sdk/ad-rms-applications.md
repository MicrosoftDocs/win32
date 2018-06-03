---
Description: You can use the Active Directory Rights Management Services (AD RMS) SDK to create applications that enable individuals to protect and consume content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b389a952-b4dd-4467-a100-0c2b017ded3a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Applications
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Applications

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can use the Active Directory Rights Management Services (AD RMS) SDK to create applications that enable individuals to protect and consume content. Content is protected by using encryption and must be decrypted before it can be consumed. In the AD RMS infrastructure, encryption and decryption require public and private keys and utilize multiple certificates and licenses. Certificates and licenses are issued and signed by AD RMS web services running on an AD RMS server. These issues are introduced in the common scenario:

1.  An individual who intends to protect content and consume content protected by others must first acquire certificates that enroll his or her computer and domain user account into the AD RMS certificate hierarchy. Certificates that identify computers are called [*machine certificate*](https://www.bing.com/search?q=*machine certificate*), and those that identify users are called [*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*). Your application must retrieve these certificates from an activation service configured on an AD RMS server in the same Active Directory cluster as the user.
2.  Once activated, an individual who wants to publish protected content uses your application to create an [*issuance license*](https://www.bing.com/search?q=*issuance license*) that specifies who can use the content and the terms of that use. The terms typically specify the time period for which the license is valid and enumerate the rights granted to the consumer. Common rights typically include the right to view, print, edit, and forward.
3.  Your application can send the issuance license to an AD RMS publishing service to be signed or use a client licensor certificate to sign the license offline. If your application uses online signing, the publishing service signs the issuance license and returns it. The signing process also produces an owner license that is saved in the license store of the user's computer. An owner license contains the OWNER right that enables the user, in this case the individual who wants to protect content, to exercise all rights enumerated by the issuance license.
4.  Your application retrieves and binds to the owner license created in step 3 and encrypts the content.
5.  The encrypted content and the signed issuance license are then made available for distribution to appropriate consumers. The distribution method is arbitrary and varies by application.
6.  Once an activated user has retrieved the signed issuance license your application uses it to request an [*end-user license*](https://www.bing.com/search?q=*end-user license*) from the AD RMS licensing service specified in the issuance license. The end-user license contains a list of rights and conditions that apply to the requesting user.
7.  Your application binds to and enforces the rights enumerated in the end-user license and uses the public key in the issuance license to decrypt the protected content.

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[AD RMS Overview](ad-rms-overview.md)
</dt> </dl>

 

 



