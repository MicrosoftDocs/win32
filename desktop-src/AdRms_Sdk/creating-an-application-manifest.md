---
Description: A manifest is an XrML certificate that signs your application into the Active Directory Rights Management (AD RMS) Pre-production or Production hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dc5e2d57-bacc-43cc-8f97-a2962812fa6c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating an Application Manifest
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Application Manifest

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A manifest is an XrML certificate that signs your application into the Active Directory Rights Management (AD RMS) Pre-production or Production hierarchy. Like all AD RMS certificates, a signed manifest consists of a certificate chain with a Microsoft certification authority (CA) certificate as the root of trust.

An application manifest is a self-generated certificate. You create it by supplying a plaintext manifest configuration file to the [Genmanifest.exe](genmanifest-exe.md) program included with the SDK. The configuration file lists the modules that must load or can be loaded into the process space of your application and those that must not. The intent is to increase security by helping to prevent viruses from running in your application process and by preventing surreptitious replacement of libraries.

You provide the manifest as input to only one function, [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment), which loads the lockbox and returns a handle to a secure environment object. You do not need to create a manifest just to activate a computer or a user or to acquire any other type of AD RMS certificate, but you do need one to create licenses, load libraries, and encrypt or decrypt content.

The following functions require a handle to a secure environment created by calling [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment). Therefore, you must create a manifest before calling them.

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

Every time that you change and then rebuild your application, you must regenerate the associated manifest. The following topics discuss manifest creation in more detail.

| Topic                                                                                      | Description                                                                                                                    |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [Manifest Configuration File Syntax](manifest-configuration-file-syntax.md)               | Discusses the XML elements that make up a configuration file.                                                                  |
| [Manifest Configuration File Example](manifest-configuration-file-example.md)             | Provides a basic configuration file example that you can follow when creating a manifest.                                      |
| [Genmanifest.exe](genmanifest-exe.md)                                                     | Specifies the syntax of the Genmanifest.exe program used to create and sign a manifest.                                        |
| [Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md) | Discusses how to create a public key pair that can be used to sign a manifest into the Pre-production or Production hierarchy. |
| [Authenticode Signing Included Modules](authenticode-signing-included-modules.md)         | Discusses how to include Authenticode-signed modules in a manifest.                                                            |



 

## Related topics

<dl> <dt>

[Create an Application Manifest](create-an-application-manifest.md)
</dt> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



