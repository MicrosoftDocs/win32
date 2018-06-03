---
Description: The Active Directory Rights Management Services (AD RMS) SDK includes sample projects that demonstrate how to use the AD RMS client functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 88c39fa0-d967-496a-8758-b50a8f0f42fb
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: View the Included Samples
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View the Included Samples

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK includes sample projects that demonstrate how to use the AD RMS client functions. The projects were created by using Visual Studio 2005. You can find the samples in the Samples\\Security\\ADRMS folder in the Microsoft Windows Software Development Kit (SDK) installation path.

To build a project, use the solution (.sln) file in the appropriate folder. To run the AcquireClientLicensor, AcquireTemplates, OnlinePublishing, or OfflinePublishing samples, you must have access to an AD RMS licensing service.

The following topics summarize the available samples:

-   [AcquireClientLicensor](#acquireclientlicensor)
-   [AcquireTemplates](#acquiretemplates)
-   [Consumption](#consumption)
-   [MachineActivation](#machineactivation)
-   [OfflinePublishing](#offlinepublishing)
-   [OnlinePublishing](#onlinepublishing)
-   [PublishingACL](#publishingacl)
-   [PublishingTemplate](#publishingtemplate)
-   [SbActivation](#sbactivation)
-   [UserActivation](#useractivation)
-   [Related topics](#related-topics)

## AcquireClientLicensor

The AcquireClientLicensor sample shows how to acquire a client licensor certificate. You must provide a user ID, and you can optionally specify the URL of an activation and certification server. If you do not provide an URL, the sample uses service discovery to find a server. This sample performs the following actions:

-   Creates a client session.
-   Activates the machine if necessary.
-   Activates the user if necessary.
-   Uses service discovery to find a licensing server if an appropriate URL was not passed in.
-   Acquires the client licensor certificate from the licensing server.

## AcquireTemplates

The AcquireTemplates sample shows how to download and enumerate templates from an AD RMS server. You can optionally specify the URL of a certification server. If you do not provide a URL, the sample uses service discovery to find a server. This sample performs the following actions:

-   Creates a client session.
-   Uses service discovery to find a licensing server if an appropriate URL was not passed in.
-   Creates an empty issuance license from a template.
-   Downloads the templates from the server to the license store.
-   Enumerates the templates from the local store.

> [!Note]
>
> This sample cannot be run on operating systems before Windows Vista with Service Pack 1 (SP1) and Windows Server 2008. Beginning with these systems, the AD RMS client can automatically obtain templates from an AD RMS server by using a Windows Management Instrumentation (WMI) job in the task scheduler. Therefore, if WMI distribution is enabled, you can call [**DRMEnumerateLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmenumeratelicense) to enumerate the rights policy templates from the local template store. Applications should avoid calling [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate).
>
> Also, to run this sample on a 64-bit computer, you must open the solution (.sln) file and run the Configuration Manager to add Itanium and x64 to the list of available platforms in the operating system drop-down list.

 

## Consumption

The Consumption sample shows how to decrypt protected content. You must specify the user ID and the name of the manifest file (Consumption.mcf included with the SDK). You can specify the URLs of an activation server and a licensing server. If you do not, the sample uses service discovery to find the appropriate server(s). This sample performs the following actions:

-   Creates a client session.
-   Activates the machine if necessary.
-   Enumerates the machine certificates.
-   Activates the user if necessary.
-   Acquires a client licensor certificate if one does not already exist.
-   Reads the manifest file into a buffer.
-   Retrieves the cryptographic service provider and initializes the environment.
-   Creates an unsigned issuance license from scratch and sets metadata and rights on the license.
-   Signs the issuance license offline.
-   Encrypts the content.
-   Acquires an end-user license, retrieves the content ID, and binds to the license.
-   Creates a decrypting object and decrypts the content.

## MachineActivation

The MachineActivation sample shows how to activate a machine. You can specify the URL of an activation server. If you do not, the sample uses service discovery to find a server. This sample performs the following actions:

-   Creates a client session.
-   Calls the [**DRMGetServiceLocation**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetservicelocation) function to find a licensing server if a URL was not provided as input.
-   Calls the [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate) function to activate the machine.

## OfflinePublishing

The OfflinePublishing sample shows how to create and sign a license offline. The sample acquires the appropriate licenses and certificates, initializes the environment, and signs the publishing license. You can specify the URL of an activation server. If you do not, the sample uses service discovery to find a server. This sample performs the following actions:

-   Creates a client session.
-   Activates the machine if necessary.
-   Enumerates the machine certificates.
-   Activates the user if necessary.
-   Acquires a client licensor certificate if one does not already exist.
-   Retrieves the cryptographic service provider and initializes the environment.
-   Creates an unsigned issuance license and sets metadata and rights on the license.
-   Signs the issuance license offline.

## OnlinePublishing

The OnlinePublishing sample shows how to publish content online. You can specify the URL of a licensing server. If you do not, the sample uses service discovery to find a server. A user ID is required. This sample performs the following actions:

-   Creates a client session.
-   Creates an unsigned issuance license and sets metadata and rights on the issuance license for a specific user.
-   Uses service discovery, if necessary, to find the licensing server.
-   Signs the issuance license online.

## PublishingACL

The PublishingACL sample shows how to create an unsigned issuance license. You must specify the path of the folder where the content will be saved, and at least one domain user must have access granted to that folder. This sample performs the following actions:

-   Creates an unsigned issuance license.
-   Identifies the access control list (ACL) for the input folder.
-   Creates a user and right for each ACL and adds these to the license.
-   Sets the metadata into the issuance license
-   Generates a template from the unsigned issuance license and copies the template to a file.

## PublishingTemplate

The PublishingTemplate sample shows how to create an unsigned issuance license from an existing template. You must specify the name of the template to use. This sample performs the following actions:

-   Copies the template file into memory.
-   Creates an unsigned issuance license by using the template.

## SbActivation

The SbActivation sample shows how to activate a machine and user by using the server lockbox. This sample performs the following actions:

-   Calls the [**DRMSetGlobalOptions**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetglobaloptions) function to specify that the server lockbox is being used.
-   Calls [**DRMSetGlobalOptions**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetglobaloptions) again to specify the WinHTTP transport protocol.
-   Creates a client session.
-   Activates the machine if necessary.
-   Activates the user if necessary.

> [!Note]  
> The SbActivation sample does not work with a version 1.0 client.

 

## UserActivation

The UserActivation sample shows how to activate a user. The sample requires a user ID and an activation server URL. If you do not provide a URL, the sample uses service discovery to find an appropriate server. This sample performs the following actions:

-   Creates a client session.
-   Activates the machine if necessary.
-   Activates the user.

## Related topics

<dl> <dt>

[Setting Up the Pre-production Development Environment](setting-up-the-pre-production-development-environment.md)
</dt> </dl>

 

 



