---
description: On 64-bit operating systems, Windows Installer can call custom actions that are compiled for 32-bit or 64-bit systems.
ms.assetid: e9ef684d-e22c-43b3-a5ea-75a4cce663c1
title: Using 64-bit Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Using 64-bit Custom Actions

On 64-bit operating systems, Windows Installer can call custom actions that are compiled for 32-bit or 64-bit systems. A 64-bit custom action based on [Scripts](scripts.md) must be explicitly marked as a 64-bit custom action by adding the **msidbCustomActionType64BitScript** bit to the custom action numeric type in the Type column of the [CustomAction Table](customaction-table.md). Custom actions based on [Executable files](executable-files.md) or [Dynamic-Link Libraries](dynamic-link-libraries.md) that are complied for 64-bit operating systems do not require including this additional bit in the Type column of the CustomAction Table.

For more information, see [64-Bit Custom Actions](64-bit-custom-actions.md).

 

 



