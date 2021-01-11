---
description: The MsiUnpublishAssemblies action manages the advertisement of common language runtime assemblies and Win32 assemblies that are being removed.
ms.assetid: 199d72be-bbe1-4777-a913-2e4b92576bfa
title: MsiUnpublishAssemblies Action
ms.topic: article
ms.date: 05/31/2018
---

# MsiUnpublishAssemblies Action

The MsiUnpublishAssemblies action manages the advertisement of common language runtime assemblies and Win32 assemblies that are being removed. The action queries the [MsiAssembly table](msiassembly-table.md) to determine which assemblies have advertised or installed features being removed from the global assembly cache and which assemblies have an advertised or installed parent component being removed from a location isolated for a particular application. For information see, [Installation of Assemblies to the Global Assembly Cache](installation-of-assemblies-to-the-global-assembly-cache.md) and [Installation of Win32 Assemblies](installation-of-win32-assemblies.md).

On systems running Windows XP and later, Windows Installer can install Win32 assemblies as [side-by-side assemblies](side-by-side-assemblies.md). For more information, see [About Isolated Applications and Side-by-side Assemblies](../sbscs/about-isolated-applications-and-side-by-side-assemblies.md).

## Sequence Restrictions

The MsiUnpublishAssemblies action must come after the [InstallInitialize action](installinitialize-action.md) in the [InstallExecuteSequence table](installexecutesequence-table.md).

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Application context.       |
| \[2\] | Assembly name.             |



 

## Remarks

The [MsiPublishAssemblies Action](msipublishassemblies-action.md) manages the advertisement of assemblies being advertised or installed.

 

 
