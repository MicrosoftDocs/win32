---
Description: A manifest is a self-generated XrML certificate that signs your application into the Pre-production or Production hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 63df9238-ce23-4ab3-94c4-476d37bb95db
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Create an Application Manifest
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create an Application Manifest

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A manifest is a self-generated XrML certificate that signs your application into the Pre-production or Production hierarchy. It is used primarily to protect your application from viruses. By specifying required, optional, and prohibited files, the manifest enables you to control what is loaded into the process space and what is allowed to access protected content. This increases security by helping to prevent viruses from running in the same space as your application and by preventing an attacker from surreptitiously replacing libraries. For more information, see [Creating an Application Manifest](creating-an-application-manifest.md).

You provide the manifest as input to only one function, [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment), which loads the lockbox and returns a handle to a secure environment object. The following functions require the environment handle, and many other functions indirectly require a secure environment:

-   [**DRMCheckSecurity**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmchecksecurity)
-   [**DRMCreateBoundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateboundlicense)
-   [**DRMCreateEnablingPrincipal**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateenablingprincipal)
-   [**DRMCreateLicenseStorageSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreatelicensestoragesession)
-   [**DRMGetEnvironmentInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetenvironmentinfo)
-   [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense)
-   [**DRMGetTime**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgettime)
-   [**DRMLoadLibrary**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmloadlibrary)
-   [**DRMRegisterProtectedWindow**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmregisterprotectedwindow)
-   [**DRMRegisterRevocationList**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmregisterrevocationlist)

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



