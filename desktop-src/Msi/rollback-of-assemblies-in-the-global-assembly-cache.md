---
description: A two-step process extends the Windows Installer's transaction model to products containing common language runtime assemblies. This enables the installer to rollback unsuccessful installations and removals of assemblies.
ms.assetid: 065a380c-4eb5-48a5-ab0a-7f1229b77898
title: Rollback of Assemblies in the Global Assembly Cache
ms.topic: article
ms.date: 05/31/2018
---

# Rollback of Assemblies in the Global Assembly Cache

A two-step process extends the Windows Installer's transaction model to products containing common language runtime assemblies. This enables the installer to rollback unsuccessful installations and removals of assemblies.

During the first step, the Windows Installer uses the Microsoft .NET Framework to create one interface for each assembly. The Windows Installer uses as many interfaces as there are assemblies being installed. Committing an assembly using one of these interfaces only means that the assembly is ready to replace any existing assembly with the same name, it does not yet replace it. If the user cancels the installation, or if there is a fatal installation error, the Windows Installer can still rollback the assembly to its previous state by releasing these interfaces.

After the Windows Installer completes installing all assemblies and Windows Installer components, the installer may initiate the second step of the installation. The second step uses a separate function to do the final commit of all the new common language runtime assemblies. This replaces any existing assemblies with the same name.

 

 



