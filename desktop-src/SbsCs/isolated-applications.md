---
description: Isolated applications are self-describing applications installed with manifests. Isolated applications can use both private assemblies and shared assemblies.
ms.assetid: 66c65b92-7c49-4932-b8c5-91b20fb0a038
title: Isolated Applications
ms.topic: article
ms.date: 05/31/2018
---

# Isolated Applications

Isolated applications are self-describing applications installed with [manifests](manifests.md). Isolated applications can use both [private assemblies](/windows/desktop/Msi/private-assemblies) and [shared assemblies](/windows/desktop/Msi/shared-assemblies).

An application is considered fully isolated if all of its components are either shared [side-by-side assemblies](about-side-by-side-assemblies-.md) or private assemblies. It is called partially isolated if it uses some components that are not side-by-side assemblies. Note that if an application uses some components that are not side-by-side assemblies, or uses private assemblies, the application may be affected by the installation or removal of other applications on the system. For more information, see [Side-by-side Assembly Sharing](side-by-side-assembly-sharing.md).

Developers are encouraged to design isolated applications and to update existing applications into isolated applications for the following reasons:

-   Isolated applications are more stable and reliably updated because they are unaffected by the installation, removal, or upgrading of other applications on the system.
-   Isolated applications can be designed so that they always run using the same assembly versions with which they were built and tested.
-   Isolated applications can use functionality provided by the side-by-side assemblies made available by Microsoft. For more information, see [Supported Microsoft Side-by-side Assemblies](supported-microsoft-side-by-side-assemblies.md).
-   Isolated applications are not tied to the shipping schedule of their side-by-side assemblies because applications and administrators can update the configuration after deployment without having to reinstall the application. This would not apply in the case where only one version of the assembly is being made available.
-   A fully isolated application may be installed by using the **xcopy** command. [Windows Installer](../msi/windows-installer-portal.md) can also be used to install an isolated application without impact to the registry. For more information, see [Installation of Win32 Assemblies](../msi/installation-of-win32-assemblies.md).

In some cases, existing applications can be updated into an isolated application without having to rewrite the application code. An [application manifest](application-manifests.md) can be created that describes the application's dependencies on [side-by-side assemblies](about-side-by-side-assemblies-.md). If the application uses components that are not side-by-side assemblies, these may be deployed as [private assemblies](/windows/desktop/Msi/private-assemblies). Note that the possibility of doing this with third-party components may depend on licensing because the component will need to be authored as an assembly. For example, by creating an application manifest and specifying a dependence on the side-by-side common controls (COMCTL32), an application running on Windows XP can take advantage of Windows *theming*. You should always test your application to ensure it is compatible with the new version of the COMCTL32 assembly.

It may not be possible to update every existing application into a fully isolated application. For example, some [Windows File Protection (WFP)](/windows/desktop/Wfp/windows-resource-protection-portal) system assemblies are not available as side-by-side assemblies and cannot be installed with the application as a private assembly. It may be possible to partially isolate such applications by specifying side-by-side assembly dependencies for some of the application's assemblies in an application manifest.

 

 
