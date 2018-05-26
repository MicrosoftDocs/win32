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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Create an Application Manifest

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A manifest is a self-generated XrML certificate that signs your application into the Pre-production or Production hierarchy. It is used primarily to protect your application from viruses. By specifying required, optional, and prohibited files, the manifest enables you to control what is loaded into the process space and what is allowed to access protected content. This increases security by helping to prevent viruses from running in the same space as your application and by preventing an attacker from surreptitiously replacing libraries. For more information, see [Creating an Application Manifest](creating-an-application-manifest.md).

You provide the manifest as input to only one function, [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master), which loads the lockbox and returns a handle to a secure environment object. The following functions require the environment handle, and many other functions indirectly require a secure environment:

-   [**DRMCheckSecurity**](/windows/previous-versions/Msdrm/nf-msdrm-drmchecksecurity?branch=master)
-   [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master)
-   [**DRMCreateEnablingPrincipal**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateenablingprincipal?branch=master)
-   [**DRMCreateLicenseStorageSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreatelicensestoragesession?branch=master)
-   [**DRMGetEnvironmentInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetenvironmentinfo?branch=master)
-   [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master)
-   [**DRMGetTime**](/windows/previous-versions/Msdrm/nf-msdrm-drmgettime?branch=master)
-   [**DRMLoadLibrary**](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master)
-   [**DRMRegisterProtectedWindow**](/windows/previous-versions/Msdrm/nf-msdrm-drmregisterprotectedwindow?branch=master)
-   [**DRMRegisterRevocationList**](/windows/previous-versions/Msdrm/nf-msdrm-drmregisterrevocationlist?branch=master)

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



