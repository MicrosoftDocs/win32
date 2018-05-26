---
Description: To encrypt or decrypt content, a user must be signed into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 768f8db0-52f7-425e-a9be-10c86dafb441
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights Account Certificate Code Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rights Account Certificate Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

To encrypt or decrypt content, a user must be signed into the Active Directory Rights Management Services (AD RMS) Pre-production or Production certificate hierarchy. This process, called activating a user, returns a certificate chain. The root of the chain is a Microsoft certification authority (CA) certificate, and the chain ends with a signed [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly). You can use the [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) function to activate a user. This is an asynchronous function that returns immediately to your application while processing the activation request on another thread. It periodically delivers status information to a callback function that you must create. For more information, see [Creating a Callback Function](creating-a-callback-function.md).

Activation is performed by an AD RMS certification service running on an AD RMS server in your enterprise or on the Internet. The logged-on user must have an associated machine certificate before activation can succeed. You can obtain a machine certificate by activating the computer. For more information, see [Activating a Computer](activating-a-computer.md). Also verify that the following are true:

-   The account is a member of the Active Directory Domain Users group.
-   The client can browse the http(s)://*ServerName*/\_wmcs/certification website on the AD RMS server. If this is not possible, verify that:
    -   The logon setting in the local Internet zone is set to automatic logon with the current user name and password.
    -   The logon setting in the local intranet zone is set to automatic logon with the current user name and password.
    -   Directory browsing is enabled for the http(s)://*site*/\_wmcs/certification website.
    -   The AD RMS Service Group and the Domain Users group have been granted read and execute access privileged for the ../\_wmcs/certification/ServerCertification.asmx webpage.

The example discussed in the following topics requires that you enter the email address of the user account to be activated. Service discovery is used to find the URL of the AD RMS certification service. For a more complete listing, see the UserActivation sample included with the Microsoft Windows Software Development Kit (SDK).

-   [UserActivation\_Main.cpp](useractivation-main-cpp.md)
-   [UserActivation\_GetServiceURL.cpp](useractivation-getserviceurl-cpp.md)
-   [UserActivation\_Callback.cpp](useractivation-callback-cpp.md)
-   [UserActivation.h](useractivation-h.md)

## Related topics

<dl> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[Rights Account Certificates](rights-account-certificates.md)
</dt> </dl>

 

 



