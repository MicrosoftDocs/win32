---
description: If a Windows Installer package installs or advertises assemblies, the installer stores information about those assemblies in the local system registry.
ms.assetid: 1a6b0530-b5ad-49db-bc08-5b20d32420ef
title: Assembly Registry Keys Written by Windows Installer
ms.topic: article
ms.date: 05/31/2018
---

# Assembly Registry Keys Written by Windows Installer

If a Windows Installer package installs or advertises assemblies, the installer stores information about those assemblies in the local system registry. Please note that these registry keys are only intended to be used internally by Windows Installer and they should not be relied upon by your application. The content, location, and structure of information stored in these keys is subject to change. Applications should rely upon [**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya) to manage assemblies.

Assemblies are registered by their assembly names. The names of the values stored in the following locations are the assembly names. The actual values are of the type REG\_MULTI\_SZ and contain data used by [**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya) to install or repair assemblies.

## Information About Private Assemblies

Windows Installer stores information about private assemblies carried by Windows Installer packages that have been installed as managed per-user applications under the following registry key:

**HKLM**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Installer**\\**Managed**\\***User SID***\\**Installer**\\**Assemblies**\\***path to config file***

Windows Installer stores information about private assemblies carried by Windows Installer packages that have been installed per-user under the following registry key:

**HKCU**\\**Software**\\**Microsoft**\\**Installer**\\**Assemblies**\\***path to config file***

Windows Installer stores information about private assemblies carried by Windows Installer packages and installed per-machine under the following registry key:

**HKLM**\\**SOFTWARE**\\**Classes**\\**Installer**\\**Assemblies**\\***path to config file***

## Information About Global or Shared Assemblies

Windows Installer stores information about shared assemblies carried by Windows Installer packages that have been installed as managed per-user applications under the following registry key:

**HKLM**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Installer**\\**Managed**\\***User SID***\\**Installer**\\**Assemblies**\\**Global**

Windows Installer stores information about shared assemblies carried by Windows Installer packages that have been installed per-user under the following registry key:

**HKCU**\\**Software**\\**Microsoft**\\**Installer**\\**Assemblies**\\**Global**

Windows Installer stores information about shared assemblies carried by Windows Installer packages and installed per-machine under the following registry key:

**HKLM**\\**SOFTWARE**\\**Classes**\\**Installer**\\**Assemblies**\\**Global**

 

 



