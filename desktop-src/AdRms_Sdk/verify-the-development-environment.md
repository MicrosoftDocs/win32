---
Description: After you have set up your Pre-production development environment, you can verify that it is working correctly and that you can publish and consume protected content by running the OnlinePublishing sample included with the Active Directory Rights Management Services (AD RMS) SDK. Perform the following steps
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c3231ffa-ff28-4107-b80c-3733ad13813e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Verify the Development Environment
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Verify the Development Environment

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

After you have set up your Pre-production development environment, you can verify that it is working correctly and that you can publish and consume protected content by running the OnlinePublishing sample included with the Active Directory Rights Management Services (AD RMS) SDK. Perform the following steps:

1.  Create an AD domain user account on the AD RMS server and specify an email address for the account. For example, if the domain name is Contoso.com, create an account named RMSuser and specify an email address of rmsuser@contoso.com.
2.  Verify that your client development computer is joined to the domain discussed in the preceding step and that the computer is activated against the Pre-production hierarchy.
3.  Log on to the client computer by using the new account. If the account has not been activated into the Pre-production hierarchy, activate it now. For more information, see [Activating a Computer](activating-a-computer.md).
4.  Compile the OfflinePublishing sample on the client computer.
5.  Create a manifest called TestAppManifest.xml for OnlinePublishing. For more information, see [Create an Application Manifest](create-an-application-manifest.md).
6.  Run OfflinePublishing.exe using the email address of the activated user account that you created in step 1. The following command line shows how to do this. You must replace the user name and the service URL with the appropriate values from your own environment.

    **OfflinePublishing** **-U** *RMSuser@contoso.com***-L** *http://contoso.com/\_wmcs/licensing*

    If OfflinePublishing.exe is successful, it creates an [*end-user license*](e-gly.md#-rm-end-user-license-gly) (EUL) for the current user and saves it in the license store.

Successful completion of the preceding steps verifies that:

-   The AD RMS server is properly configured.
-   The development computer is activated.
-   The user is activated and has a valid rights account certificate.
-   The manifest creation process worked correctly.
-   The user can acquire an EUL and consume content.

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



