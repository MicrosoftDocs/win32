---
description: The RegisterFonts action registers installed fonts with the system. This action maps the font name in the FontTitle column of the Font table to the path of the font file installed.
ms.assetid: 3c6d3ec9-b36f-46f4-8b32-c97a75b9e238
title: RegisterFonts Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterFonts Action

The RegisterFonts action registers installed fonts with the system. This action maps the font name in the FontTitle column of the [Font table](font-table.md) to the path of the font file installed.

## Sequence Restrictions

The [InstallFiles](installfiles-action.md) action must be called before calling the RegisterFonts action.

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Font file.                 |



 

## Remarks

The RegisterFonts action is executed if the file specified in the File\_ column of the [Font table](font-table.md) belongs to a component being installed.

 

 



