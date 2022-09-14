---
description: The Windows Installer determines whether to allow the removal of a common language runtime assembly based upon a client list it keeps independently of the assembly.
ms.assetid: 3f83ad88-e6a4-484b-bcf5-8e2e65f1f41f
title: Removal of Assemblies from the Global Assembly Cache
ms.topic: article
ms.date: 05/31/2018
---

# Removal of Assemblies from the Global Assembly Cache

The Windows Installer determines whether to allow the removal of a common language runtime assembly based upon a client list it keeps independently of the assembly. The Windows Installer keeps one pin bit to represent Windows Installer clients of the assembly. The installer pins the assembly for the first Windows Installer client and unpins it when the last Windows Installer client is removed. The assembly maintains a pin bit for every client of an assembly.

The Windows Installer is not directly responsible for the physical removal of common language runtime assemblies from the computer. The installer unpins the assembly when the last Windows Installer client is removed. If the Windows Installer is the last client of the assembly, the common language runtime provides the option to force a synchronous cleanup of the assembly. The cleanup process is atomic and there is no provision for a "rollback" at this point. All unpinning of common language runtime assemblies must occur after the user has had a chance to cancel the installation or removal.

 

 



