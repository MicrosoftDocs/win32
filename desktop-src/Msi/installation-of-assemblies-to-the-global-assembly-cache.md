---
description: The Windows Installer installs common language runtime assemblies into the global assembly cache using the Microsoft .NET Framework.
ms.assetid: 21d535d5-f05b-411a-8719-2662e6046fbd
title: Installation of Assemblies to the Global Assembly Cache
ms.topic: article
ms.date: 05/31/2018
---

# Installation of Assemblies to the Global Assembly Cache

The Windows Installer installs common language runtime assemblies into the global assembly cache using the Microsoft .NET Framework. When installing assemblies to the global assembly cache, the installer cannot use the same directory structure and file version rules it uses when installing regular Windows Installer components. Regular Windows Installer components may be installed into multiple directory locations by different products. Assemblies can exist only once in the assembly cache. Each assembly is added and removed from the assembly cache as an indivisible whole; therefore, all the files comprising an assembly are always installed or removed together.

The disk cost of regular Windows Installer components and common language runtime assemblies are calculated differently. The total disk cost of a regular Windows Installer component includes local costs, source costs, and removal costs. For details, see [File Costing](file-costing.md). This method cannot be used to cost common language runtime assemblies because these may have clients other than the Windows Installer. The cost of common language runtime assemblies must be determined by querying the Microsoft .NET Framework common language runtime.

The Windows Installer uses a two-step transactional process to install products containing common language runtime assemblies. This enables the rollback of assembly installation and removal. For more information, see [Rollback of Assemblies in the Global Assembly Cache](rollback-of-assemblies-in-the-global-assembly-cache.md).

Note that assemblies installed to the global assembly cache by an installation in the per-user [installation context](installation-context.md) are not protected by Windows File Protection. Assemblies that are installed to the global assembly cache by an installation in the per-machine installation context are protected by [Windows Resource Protection](../wfp/windows-resource-protection-portal.md).

 

 
