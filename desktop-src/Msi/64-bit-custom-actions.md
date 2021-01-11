---
description: On 64-bit operating systems, Windows Installer may call custom actions that have been compiled for 32-bit or 64-bit systems.
ms.assetid: fc370ab4-93f3-4e1e-9468-3454d4fee0be
title: 64-Bit Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# 64-Bit Custom Actions

On 64-bit operating systems, Windows Installer may call custom actions that have been compiled for 32-bit or 64-bit systems.

A 64-bit custom action based on [Scripts](scripts.md) must be explicitly marked as a 64-bit custom action by adding the **msidbCustomActionType64BitScript** bit to the custom actions numeric type in the Type column of the [CustomAction table](customaction-table.md).



| Constant                             | Hexadecimal | Decimal | Meaning                                                           |
|--------------------------------------|-------------|---------|-------------------------------------------------------------------|
| **msidbCustomActionType64BitScript** | 0x0001000   | 4096    | This is a 64-bit custom action written in [Scripts](scripts.md). |



 

Custom actions based on [Executable files](executable-files.md) or [Dynamic-Link Libraries](dynamic-link-libraries.md) that have been complied for a 64-bit operating systems do not require including this additional bit in the Type column of the CustomAction table.

 

 



