---
Description: The following topics discuss how to setup your environment and program typical scenarios using the Active Directory Rights Management Services (AD RMS) SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dc21c680-c9e9-427a-baf0-b5204a466491
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Using the AD RMS SDK
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the AD RMS SDK

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following topics discuss how to setup your environment and program typical scenarios using the Active Directory Rights Management Services (AD RMS) SDK.



| Topic                                                                                                              | Description                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md) | Discusses the steps necessary to enroll in the Pre-production certificate hierarchy and begin writing an AD RMS application.                                                                                                                                                                 |
| [Switching to the Production Environment](switching-to-the-production-environment.md)                             | Discusses how to move from the Pre-production to the Production certificate hierarchy when you have finished developing and testing your application and intend to release it to customers.                                                                                                  |
| [Working with Licenses and Templates](working-with-licenses-and-templates.md)                                     | Contains miscellaneous topics about end-user licenses and rights policy templates.                                                                                                                                                                                                           |
| [Creating a Callback Function](creating-a-callback-function.md)                                                   | Discusses how to create a callback function used by various AD RMS asynchronous functions to deliver status information to your application.                                                                                                                                                 |
| [Activating a Computer](activating-a-computer.md)                                                                 | Discusses how to sign a computer into a Pre-production or Production certificate hierarchy. For a C++ sample, see [Machine Certificate Code Example](machine-certificate-code-example.md).                                                                                                  |
| [Activating a User](activating-a-user.md)                                                                         | Discusses how to sign an Active Directory domain user account into a Pre-production or Production certificate hierarchy. For a C++ sample, see [Rights Account Certificate Code Example](rights-account-certificate-code-example.md).                                                       |
| [Creating an Application Manifest](creating-an-application-manifest.md)                                           | Discusses how to create an application manifest to sign your application into a Pre-production or Production certificate hierarchy.                                                                                                                                                          |
| [Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)                                   | Discusses how to create an issuance license that identifies who can use an item of content and the rights governing that use. For C++ code samples, see [Online Signing Code Example](online-signing-code-example.md) and [Offline Signing Code Example](offline-signing-code-example.md). |
| [Encrypting Content](encrypting-content.md)                                                                       | Discusses how to use the AD RMS SDK to encrypt content. For a C++ sample, see [Encrypting Content Code Example](encrypting-content-code-example.md).                                                                                                                                        |
| [Decrypting Content](decrypting-content.md)                                                                       | Discusses how to use the AD RMS SDK to decrypt content. For a C++ sample, see [Decrypting Content Code Example](decrypting-content-code-example.md).                                                                                                                                        |
| [Revoking a Certificate](revoking-a-certificate.md)                                                               | Discusses how to revoke licenses and certificates. For a C++ sample, see [Revocation Code Example](revocation-code-example.md)                                                                                                                                                              |
| [Publishing Content](publishing-content.md)                                                                       | Discusses how to use the compound file binary format (CFBF) to publish encrypted content, issuance licenses, and end-user licenses.                                                                                                                                                          |
| [Debugging an Application](debugging-an-application.md)                                                           | Discusses how to debug an application that creates a secure environment.                                                                                                                                                                                                                     |



 

> [!Note]  
> If you call the AD RMS SDK client functions from managed code (using Platform Invocation Services – P/Invoke) it is important to remember that when you run a managed 32-bit client application on a 64-bit operating system, you must build the application by specifying "x64" for the /platform compiler option. If you specify "x86" or "anycpu", an **E\_DRM\_MANIFEST\_POLICY\_VIOLATION** error code is returned. For more information about the /platform command line option, see the [/platform (Specify Output Platform) (C# Compiler Options)](http://go.microsoft.com/fwlink/p/?linkid=87258) topic on MSDN. For more information about identifying the output platform when using Visual Studio, see [Build Page, Project Designer (C#)](http://go.microsoft.com/fwlink/p/?linkid=87259).

 

## Related topics

<dl> <dt>

[About the AD RMS SDK](about-the-ad-rms-sdk.md)
</dt> <dt>

[Active Directory Rights Management Services SDK](active-directory-rights-management-services-sdk-portal.md)
</dt> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



