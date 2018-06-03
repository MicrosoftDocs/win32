---
Description: Activating a computer creates a machine certificate that signs the computer into an Active Directory Rights Management Services (AD RMS) Pre-production (or Production) hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dc0263cc-3675-43ba-b0db-e613cc1ddcbc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Activate the Development Computer
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Activate the Development Computer

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Activating a computer creates a [*machine certificate*](https://www.bing.com/search?q=*machine certificate*) that signs the computer into an Active Directory Rights Management Services (AD RMS) Pre-production (or Production) hierarchy. Machine certificates are saved on a per user basis. That is, each user who has activated the computer has a unique machine certificate saved in the user's certificate store. You can obtain a machine certificate by performing any of the following tasks:

-   Run the Rmactivate\_isv.exe program (client Pre-production).
-   Run the Rmactivate\_ssp\_isv.exe program (server Pre-production).
-   Write your own program that calls the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function.
-   Run the MachineActivation sample included with the SDK.

Activation is performed entirely on the local computer. There is no server transaction. Activating a computer that has already been activated overwrites the existing machine certificate for the specified user, thereby requiring that you obtain a new rights account certificate for that user. For more information, see [Activate a User Account](activate-a-user-account.md).

Machine certificates are installed in the following folders.

| Version                                                                      | Certificate location                                                 |
|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| For AD RMS on Windows Vista and Windows Server 2008 using the client lockbox | %USERPROFILE%\\Application Data\\Local\\Microsoft\\DRM               |
| For AD RMS on Windows Vista and Windows Server 2008 using the server lockbox | %ALLUSERSPROFILE%\\Microsoft\\DRM\\Server\\UserSid                   |
| For RMS client 1.0 SP2 using the client lockbox                              | %USERPROFILE%\\Local Settings\\Application Data\\Microsoft\\DRM      |
| For RMS server 1.0 SP2 using the server lockbox                              | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\DRM\\Server\\UserSid |



 

## Related topics

<dl> <dt>

[Machine Certificates](machine-certificates.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



