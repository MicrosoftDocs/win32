---
description: This topic describes the differences between the Tablet PC library binary versions.
ms.assetid: 708567b8-33bd-43cd-b56f-8ee9c96fb315
title: Which Library Version to Reference
ms.topic: article
ms.date: 05/31/2018
---

# Which Library Version to Reference

This topic describes the differences between the Tablet PC library binary versions.

## Tablet PC Library Versions

The Tablet PC library binaries (Microsoft.Ink.dll) have been updated in Windows Vista. Theses binaries are referred to as "version 6.0" to co-incide with the version of Windows in which they are being released.

The most recent release of the binaries that are compatible with Windows XP is referred to as "version 1.7".

The Windows SDK can be installed on both Vista and XP machines, and the Windows SDK includes both versions of Microsoft.Ink.dll.

These are installed in:

1. %programfiles%\\Reference Assemblies\\Microsoft\\Tablet PC\\v1.7\\Microsoft.Ink.dll

2. %programfiles%\\Reference Assemblies\\Microsoft\\Tablet PC\\v6.0\\Microsoft.Ink.dll

The version 6.0 binaries are only compatible with Windows Vista, and applications written against them should only ever be run on Windows Vista.

An application written against the version 1.7 binaries should run without modification when installed on Windows Vista.

 

 



