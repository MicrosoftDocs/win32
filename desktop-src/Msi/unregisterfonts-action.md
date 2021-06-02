---
description: The UnregisterFonts action removes registration information about installed fonts from the system.
ms.assetid: 97cbbcbe-eb1c-45f0-91d2-4b17984498ae
title: UnregisterFonts Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterFonts Action

The UnregisterFonts action removes registration information about installed fonts from the system.

## Sequence Restrictions

The [RemoveFiles](removefiles-action.md) action must be called after UnregisterFonts.

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Font file.                 |



 

## Remarks

The UnregisterFonts action is executed if the file specified in the File\_ column of the [Font table](font-table.md) belongs to a component being uninstalled.

 

 



