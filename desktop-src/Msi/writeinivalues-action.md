---
description: The WriteIniValues action writes the .ini file information that the application needs written to its .ini files.
ms.assetid: ec54db54-293c-4db3-81af-6e8669f27310
title: WriteIniValues Action
ms.topic: article
ms.date: 05/31/2018
---

# WriteIniValues Action

The WriteIniValues action writes the .ini file information that the application needs written to its .ini files. The writing of this information is gated by the [Component table](component-table.md). An .ini value is written if the corresponding component has been set to be installed either locally or run from source.

## Sequence Restrictions

The InstallValidate action must come before the WriteIniValues action. If there is a [RemoveIniValues action](removeinivalues-action.md) in the sequence, then it must come before the WriteIniValues action.

## ActionData Messages



| Field | Description of action data              |
|-------|-----------------------------------------|
| \[1\] | Identifier of .ini file.                |
| \[2\] | .ini file key in the following section. |
| \[3\] | Item removed from .ini file.            |
| \[4\] | Value removed from .ini file.           |



 

## Related topics

<dl> <dt>

[IniFile table](inifile-table.md)
</dt> </dl>

 

 



