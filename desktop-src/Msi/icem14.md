---
description: ICEM14 validates the Value Column of the ModuleSubstitution table.
ms.assetid: e07ba63a-e748-4835-ae1b-9f7d30e46d39
title: ICEM14
ms.topic: article
ms.date: 05/31/2018
---

# ICEM14

ICEM14 validates the Value Column of the [ModuleSubstitution table](modulesubstitution-table.md).

## Result

ICEM14 posts the following errors.



| Error                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The replacement string in ModuleSubstitution.Value column in row \[1\].\[2\].\[3\] is not found in ModuleConfiguration table.                                 | \[1\].\[2\].\[3\] refers to a *table.row.column* primary key for a row in the ModuleSubstitution table. The formatting template in the Value field of this row does not correspond to a row of configurable attributes in the [ModuleConfiguration Table](moduleconfiguration-table.md).                                                            |
| In ModuleSubstitution table in row \[1\].\[2\].\[3\], a configurable item is indicated in the table '%s'. The table '%s' must not contain configurable items. | One of the following tables is listed in the Table column of the ModuleSubstitution table: [ModuleSubstitution](modulesubstitution-table.md), [ModuleConfiguration](moduleconfiguration-table.md), [ModuleExclusion](moduleexclusion-table.md), or [ModuleSignature](modulesignature-table.md). These tables cannot contain configurable fields. |
| In ModuleSubstitution table in row \[1\].\[2\].\[3\], an empty replacement string is specified.                                                               | The formatting template in the Value field of this row does not correspond to a row of configurable attributes in the [ModuleConfiguration Table](moduleconfiguration-table.md).                                                                                                                                                                    |



 

ICEM14 posts the following warning.



| Warning                                                                  | Meaning                                  |
|--------------------------------------------------------------------------|------------------------------------------|
| ModuleSubstitution table exists but ModuleConfiguration table is missing | The ModuleConfiguration table is absent. |



 

## Table Used During Execution

[ModuleSubstitution table](modulesubstitution-table.md)

[ModuleConfiguration table](moduleconfiguration-table.md)

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



