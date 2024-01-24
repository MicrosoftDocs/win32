---
description: The MsiPublishAssemblies action manages the advertisement of common language runtime assemblies and Win32 assemblies.
ms.assetid: 4bc67f43-7a7e-4bd3-aa83-610b46a54e11
title: MsiPublishAssemblies Action
ms.topic: article
ms.date: 05/31/2018
---

# MsiPublishAssemblies Action

The MsiPublishAssemblies action manages the advertisement of common language runtime assemblies and Win32 assemblies. The action queries the [MsiAssembly table](msiassembly-table.md) to determine which assemblies have features being advertised or installed to the global assembly cache and which assemblies have a parent component being advertised or installed to a location isolated for a particular application. For information see, [Installation of Assemblies to the Global Assembly Cache](installation-of-assemblies-to-the-global-assembly-cache.md) and [Installation of Win32 Assemblies](installation-of-win32-assemblies.md).

On Microsoft Windows XP and later systems, Windows Installer can install Win32 assemblies as [side-by-side assemblies](side-by-side-assemblies.md). For more information, see [About Isolated Applications and Side-by-side Assemblies](../sbscs/about-isolated-applications-and-side-by-side-assemblies.md).

## Sequence Restrictions

The MsiPublishAssemblies action must come after the [InstallInitialize action](installinitialize-action.md) in the [InstallExecuteSequence table](installexecutesequence-table.md) or [AdvtExecuteSequence table](advtexecutesequence-table.md).

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Application context.       |
| \[2\] | Assembly name.             |



 

## Remarks

For more information, see [Assemblies](assemblies.md).

The [MsiUnpublishAssemblies Action](msiunpublishassemblies-action.md) manages the advertisement of assemblies being removed.

 

 
