---
description: A list of possible reasons why a Windows Installer uninstallation was unable to remove all the files of an application.
ms.assetid: 0a856f0f-a829-478e-a83b-dade7b05b4f2
title: Removing Stranded Files
ms.topic: article
ms.date: 05/31/2018
---

# Removing Stranded Files

If a file that should have been removed from the user's computer remains installed after running an uninstall, the installer may not be removing the component containing the file for one or more of the following reasons:

-   The msidbComponentAttributesPermanent bit was set for the component in the Attributes column of the [Component table](component-table.md).
-   No value was entered for the component in the ComponentId column of the Component table.
-   The component is used by another application or feature that is still installed.
-   There is a condition specified in the [Condition](condition-table.md) table that enables a feature during installation and disables the feature during uninstallation.
-   The key file for the component has a previous reference count under **HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**SharedDLLs**.
-   The component is installed in the System folder and any file in the component has a previous reference count under **HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**SharedDLLs**.
-   The Windows Installer does not remove any files or registry keys that are protected by [Windows Resource Protection](../wfp/windows-resource-protection-portal.md) (WRP). For more information, see [Using Windows Installer and Windows Resource Protection](windows-resource-protection-on-windows-vista.md). On Windows Server 2003, Windows XP, and Windows 2000, the installer does not remove any files that are protected by Windows File Protection (WFP). If a component's key path file or registry key is protected by WFP or WRP, the installer does not remove the component.
    > [!Note]  
    > Because Windows Installer does not install, update, or remove any resource that is protected by WRP, you should not include protected resources in an installation package. Instead, use only the [supported resource replacement mechanisms](../wfp/supported-file-replacement-mechanisms.md) described in the [Windows Resource Protection](../wfp/windows-resource-protection-portal.md) section.

     

 

 
