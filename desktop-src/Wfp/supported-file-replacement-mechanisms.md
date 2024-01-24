---
description: Replacement of protected resources is supported through the following mechanisms.
ms.assetid: a757e6cf-59df-4894-a0dc-40174b0aa147
title: Supported Resource Replacement Mechanisms
ms.topic: article
ms.date: 05/31/2018
---

# Supported Resource Replacement Mechanisms

Replacement of protected resources is supported through the following mechanisms.

Permission for full access to modify WRP-protected resources on Windows Vista and Windows Server 2008 is restricted to TrustedInstaller with the Windows Modules Installer service using the following mechanisms:

-   Windows Service Packs installed by TrustedInstaller.
-   Hotfixes installed by TrustedInstaller.
-   Operating system upgrades installed by TrustedInstaller.
-   Windows Update installed by TrustedInstaller.

Applications and installers attempting to replace a WRP-protected resource by means other than these specified methods are denied access to change the resource and generate an access denied error message.

For well-known installers attempting to replace WRP-protected resources, the access denied error and error message may be suppressed. In this case, the operation returns successfully, the error and error message are suppressed, but no changes are applied to the WRP-protected resource. The error may be suppressed for a well-known installer only when all of the following criteria are satisfied:

-   This is a legacy application. The application does not include a manifest with a requestedExecutionlevel that identifies the application as designed for Windows Vista or Windows Server 2008.
-   The access denied error is caused only by the attempt to modify a WRP-protected resource.
-   An Administrator is installing the application.

For information about using the Windows Installer with WRP, see [Using Windows Installer and Windows Resource Protection](/windows/desktop/Msi/windows-resource-protection-on-windows-vista) in the [Windows Installer](/windows/desktop/Msi/windows-installer-portal) SDK.

**Windows Server 2003 and Windows XP:** Replacement of WFP-protected system files is supported only through the following mechanisms:

-   Windows Service Pack installation using Update.exe
-   Hotfixes installed using Hotfix.exe
-   Operating system upgrades using Winnt32.exe
-   Windows Update

Replacing protected files by means other than these specified methods results in the original files being restored by WFP.

 

 
