---
Description: Activating a user creates a rights account certificate (RAC) that identifies the user account by signing it into an Active Directory Rights Management Services (AD RMS) Pre-production (or Production) hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1188a556-b8d0-4e15-ad75-32c236eff119
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Activate a User Account
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Activate a User Account

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Activating a user creates a [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly) (RAC) that identifies the user account by signing it into an Active Directory Rights Management Services (AD RMS) Pre-production (or Production) hierarchy.

The RAC is tied to the [*machine certificate*](m-gly.md#-rm-machine-certificate-gly) of a specific computer. That is, the AD RMS activation service that creates the RAC uses the public key in the machine certificate to sign the private key in the RAC. You must therefore activate the computer before activating a user. For more information, see [Activate the Development Computer](activate-the-development-computer.md).

A RAC is used, along with an issuance license, to retrieve an [*end-user license*](e-gly.md#-rm-end-user-license-gly) that enables the user to consume protected content. A user can have more than one RAC on a computer, one for each AD RMS service against which the user is activated, but the user cannot transfer a RAC between computers. The user account must exist in Active Directory. You can activate the account by running the UserActivation sample included with the SDK or by writing a program that calls the [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function.

## Related topics

<dl> <dt>

[Machine Certificates](machine-certificates.md)
</dt> <dt>

[Rights Account Certificates](rights-account-certificates.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



