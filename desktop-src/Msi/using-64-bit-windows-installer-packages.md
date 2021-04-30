---
description: Adhere to the following guidelines when authoring a 64-bit Windows Installer package.
ms.assetid: e7dfd188-fd4d-49d6-8cf5-c17182b697ca
title: Using 64-Bit Windows Installer Packages
ms.topic: article
ms.date: 05/31/2018
---

# Using 64-Bit Windows Installer Packages

When you create [64-bit Windows Installer Packages](64-bit-windows-installer-packages.md) or applications that call Windows Installer to install 64-bit packages, do the following:

-   Use a Windows Installer database schema of 200 or higher. Specify that version 2.0 is the minimum version of the installer required to install the package by setting the [**Page Count Summary**](page-count-summary.md) property to the integer 200. Earlier Windows Installer versions reject attempts to install 64-bit packages. For 64-bit packages on the Arm64 platform, the Windows Installer database schema must be 500 or higher.
-   Indicate in the [**Template Summary**](template-summary.md) property of the package summary information stream that this is a 64-bit package. Enter "Intel64" into the platform field of the **Template Summary** property if the package is to be run on an Intel64 processor. Enter "x64" if the package is to be run on a 64-bit extended processor. Enter “Arm64” if the package is to be run on an Arm64 processor. A package cannot be marked as supporting both Intel64 and x64 platforms, a **Template Summary** property value of "Intel64,x64" is invalid. A package cannot be marked as supporting both 32-bit and 64-bit platforms, the **Template Summary** property values of "Intel,x64" or "Intel,Intel64" are invalid.
-   Identify every 64-bit component by setting the **msidbComponentAttributes64bit** in the Attributes column of the [Component](component-table.md) table.
-   Use optional conditional statements that check the version of the 64-bit operating system by referencing the [**VersionNT64**](versionnt64.md) property. Windows Installer sets this property to the 64-bit Windows version and leaves VersionNT64 undefined if the operating system is not 64-bit Windows. For more information, see [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md).
-   Use optional conditional statements that check the numeric processor level of the computer by referencing the [**Intel64**](intel64.md) or [**Msix64**](msix64.md) property. The Windows Installer  sets these properties to the current numeric processor level of the computer and leaves the **Intel64** Property undefined if this is not an Itanium-based processor. For more information, see [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md).
-   Use the [AppSearch Table](appsearch-table.md) and [AppSearch Action](appsearch-action.md) to do optional searches of the registry for existing 64-bit components. To search for existing 64-bit components, include the **msidbLocatorType64bit** bit in the Type column of the [RegLocator Table](reglocator-table.md). For more information, see [Searching for Existing Applications, Files, Registry Entries or .ini File Entries Property](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md)
-   Obtain the paths to system folders by referencing the [**System64Folder**](system64folder.md)Property, [**ProgramFiles64Folder**](programfiles64folder.md) Property, and [**CommonFiles64Folder**](commonfiles64folder.md) Property for the 64-bit folders and the [**SystemFolder**](systemfolder.md) Property, [**ProgramFilesFolder**](programfilesfolder.md) Property, and [**CommonFilesFolder**](commonfilesfolder.md) Property for the 32-bit folders.
-   Verify that the application uses the correct GUID when referencing a 64-bit component. If there are 32-bit and 64-bit versions of a specific component, these should have different component ID GUIDs.
-   Determine whether any new environment variables need to be defined when installing 64-bit applications.
-   If a 64-bit ODBC Driver Manager is to be installed, the component that carries it should be named ODBCDriverManager64. The ODBC Driver Manager must be authored in the installer package and a component named ODBCDriverManager64 must be included. The manager will be installed if necessary.
-   Verify that the application only calls 32-bit services that run as executables. Applications should not call 32-bit services that run in DLLs.
-   If the application installs coexisting 32-bit and 64-bit versions of a component, verify that the application shares .ini file information correctly.
-   Verify that the application only applies 32-bit patches to 32-bit binaries and 64-bit patches to 64-bit binaries.
-   Consider future upgrade scenarios for both 32-bit and 64-bit versions and maintain upgrade codes. For more information, see [Patching and Upgrades](patching-and-upgrades.md).
-   When using a [bootstrapping](bootstrapping.md) application to install a [64-bit Windows Installer Package](64-bit-windows-installer-packages.md), compile the bootstrapping application as a 64-bit application.
-   To disable [Registry Reflection](../winprog64/registry-reflection.md) for registry keys that are affected by a particular component, set the **msidbComponentAttributesDisableRegistryReflection** bit in the Attributes field of the [Component](component-table.md) table. This may be necessary to have 32-bit and 64-bit copies of the same application coexist. If this bit is set, the Windows Installer calls the [**RegDisableReflectionKey**](/windows/win32/api/winreg/nf-winreg-regdisablereflectionkey) function on each key that is being accessed by the component. This bit is available with Windows Installer version 4.0. This bit is ignored on 32-bit systems. This bit is ignored on the 64-bit versions of Windows XP and Windows 2000.

> [!Note]  
> The value of the numeric registry root returned by the *lpPathBuf* parameter of the [**MsiGetComponentPath**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpatha) function distinguishes between components on 32-bit and 64-bit operating systems. For more information, see **MsiGetComponentPath** function.

 

## Related topics

<dl> <dt>

[64-Bit Custom Actions](64-bit-custom-actions.md)
</dt> </dl>

 

 
