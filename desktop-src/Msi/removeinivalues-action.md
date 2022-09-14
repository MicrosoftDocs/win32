---
description: The RemoveIniValues action removes .ini file information specified for removal in the RemoveIniFile table if the component is set to be installed locally or run-from-source.
ms.assetid: a30793c8-4154-4990-a42a-d022e69f960a
title: RemoveIniValues Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveIniValues Action

The RemoveIniValues action removes .ini file information specified for removal in the [RemoveIniFile table](removeinifile-table.md) if the component is set to be installed locally or run-from-source. The RemoveIniValues action removes .ini file information that has been associated with a component in the [IniFile table](inifile-table.md). This action also removes .ini file information if the information was written by the [WriteIniValues action](writeinivalues-action.md) and the component is scheduled to be uninstalled.

## Sequence Restrictions

The [InstallValidate](installvalidate-action.md) action must be called before the RemoveIniValues action. If a [WriteIniValues](writeinivalues-action.md) action is used in the sequence, it must appear after RemoveIniValues.

## ActionData Messages



| Field | Description of action data    |
|-------|-------------------------------|
| \[1\] | Identifier of .ini file.      |
| \[2\] | An .ini file key section.     |
| \[3\] | Item removed from .ini file.  |
| \[4\] | Value removed from .ini file. |



 

## Related topics

<dl> <dt>

[RemoveIniFile table](removeinifile-table.md)
</dt> <dt>

[IniFile table](inifile-table.md)
</dt> <dt>

[WriteIniValues action](writeinivalues-action.md)
</dt> <dt>

[InstallValidate](installvalidate-action.md)
</dt> </dl>

 

 



