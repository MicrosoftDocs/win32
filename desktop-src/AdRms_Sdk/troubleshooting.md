---
Description: Locating the source of errors is difficult in an Active Directory Rights Management (AD RMS) application because the debugging mode is prohibited and because the error may occur on either the client or the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 09083fba-b973-438a-84be-7c92c66e4ed3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Troubleshooting
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Troubleshooting

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Locating the source of errors is difficult in an Active Directory Rights Management (AD RMS) application because the debugging mode is prohibited and because the error may occur on either the client or the server. Most errors occur in two locations: building the application manifest or in the [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) function.

## Manifest Errors

-   Have you included a signed certificate chain that contains your public key when running Genmanifest.exe? Did you include the matching public and private keys in the MCF file entered to Genmanifest.exe?
-   Did you re-create your manifest after compiling the most current version of your application in the MODULELIST block? Is the version in the MODULELIST block indeed the most recent version?
-   If you included NOHASH, did you include a public key file path in the INCLUSION block?

## DRMInitEnvironment Errors

-   Many errors in [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) stem from an incorrect manifest being passed in. It is possible for Genmanifest.exe to create a manifest without failing, but the created manifest may be not valid.
-   Are you in debugging mode, or is any other application accessing Msdrm.dll in debugging mode? Are any kernel debuggers running in any process?

## Other Errors

-   Are you using the proper [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly) (RAC) (with the correct issuer, user ID, and root) for your task?
-   Are your computer and RAC activated to the same root? If they are not, you may receive **E\_DRM\_INVALID\_LICENSE\_SIGNATURE**. Are the [*issuance license*](i-gly.md#-rm-issuance-license-gly) and [*end-user license*](e-gly.md#-rm-end-user-license-gly) activated to the same root as your computer and RAC?

## Related topics

<dl> <dt>

[Debugging an Application](debugging-an-application.md)
</dt> <dt>

[Debugging With the LCP](debugging-with-the-lcp.md)
</dt> <dt>

[Debugging Without the LCP](debugging-without-the-lcp.md)
</dt> </dl>

 

 



