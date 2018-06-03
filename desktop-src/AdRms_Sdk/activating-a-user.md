---
Description: 'Before a user can encrypt or decrypt content, the user's Active Directory account must be signed into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'c998647b-2e0c-4eee-bcf9-6c080340f5bb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: Activating a User
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Activating a User

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Before a user can encrypt or decrypt content, the user's Active Directory account must be signed into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy. This process, called activating a user account, returns a certificate chain. The root of the chain is a Microsoft certification authority (CA) certificate, and the chain ends with a signed [*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*) (RAC) that uniquely identifies the account. You can use the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function to activate a user. This is an asynchronous function that returns immediately to your application while processing the activation request on another thread. It delivers the result to a callback function that you must create. For more information, see [Creating a Callback Function](creating-a-callback-function.md).

Before you can activate a user account, you must activate the computer that the user has logged onto and retrieve a [*machine certificate*](https://www.bing.com/search?q=*machine certificate*). For more information, see [Activating a Computer](activating-a-computer.md). Because the private key associated with the RAC is encrypted by using the public key in the machine certificate, the RAC cannot be used on another activated computer.

The following topics discuss user activation and rights account certificates in more detail.

| Topic                                                                                  | Example                                                              |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Rights Account Certificates](rights-account-certificates.md)                         | Discusses the general XrML contents of a rights account certificate. |
| [Rights Account Certificate Store](rights-account-certificate-store.md)               | Lists the certificate stores by operating system and AD RMS version. |
| [Rights Account Certificate XML Example](rights-account-certificate-xml-example.md)   | Contains a complete XrML certificate example.                        |
| [Rights Account Certificate Code Example](rights-account-certificate-code-example.md) | Contains a C++ example that activates a user account.                |



 

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



