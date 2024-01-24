---
description: Windows Installer can install, remove, and update Win32 assemblies and assemblies used by the common language runtime of the Microsoft .NET Framework.
ms.assetid: 88bee87c-fed2-45e9-8d8c-a5bbcc77f266
title: Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Assemblies

Windows Installer can install, remove, and update Win32 assemblies and assemblies used by the common language runtime of the Microsoft .NET Framework. An assembly is handled by the Windows Installer as a single installer component. All of the files that constitute an assembly must be contained by a single installer component that is listed in the [Component](component-table.md) table.

Windows Installer running on Windows Vista and Windows XP can install side-by-side assemblies. Side-by-side assemblies can safely share assemblies among multiple applications and can offset the negative effects of assembly sharing, such as DLL conflicts. Instead of a single version of an assembly that assumes backward compatibility with all applications, side-by-side assembly sharing enables multiple versions of a COM or Win32 assembly to run simultaneously on the system. This improved capability to isolate applications is an important part of the Microsoft .NET Framework. For more information, see [Isolated Applications and Side-by-side Assemblies](/windows/desktop/SbsCs/isolated-applications-and-side-by-side-assemblies-portal).

The following sections describe the use of assemblies with the Windows Installer.

-   [Adding Assemblies to a Package](adding-assemblies-to-a-package.md)
-   [Installing and Removing Assemblies](installing-and-removing-assemblies.md)
-   [Updating Assemblies](updating-assemblies.md)
-   [Reinstallation Modes of Common Language Runtime Assemblies](reinstallation-modes-of-common-language-runtime-assemblies.md)
-   [Assembly Registry Keys Written by Windows Installer](assembly-registry-keys-written-by-windows-installer-.md)

For information about installing COM and COM+ 1.0 applications, see [Installing a COM+ Application with the Windows Installer](installing-a-com--application-with-the-windows-installer.md), [Installing a COM Component to a Private Location](installing-a-com-component-to-a-private-location.md), and [Make a COM Component in an Existing Package Private](make-a-com-component-in-an-existing-package-private.md).

 

 
