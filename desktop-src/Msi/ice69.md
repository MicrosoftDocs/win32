---
description: ICE69 checks that all substrings of the form \[$componentkey\] within a formatted string do not cross-reference components.
ms.assetid: 6ab8f3b7-19e9-46f3-b09e-36bdb43d6f55
title: ICE69
ms.topic: article
ms.date: 05/31/2018
---

# ICE69

ICE69 checks that all substrings of the form \[$componentkey\] within a [formatted](formatted.md) string do not cross-reference components. A cross-component reference occurs when the \[$componentkey\] property of a formatted string refers to a component other than the component stored in the Component\_ column of your tables.

Problems with cross-component referencing arise from the way [formatted](formatted.md) strings are evaluated. If the component referenced with the \[$componentkey\] property is already installed and is not being changed during the current installation (for example, being reinstalled, moved to source, and so forth), the expression \[$componentkey\] evaluates to null, because the action state of the component in \[$componentkey\] is null. Similar problems can occur during upgrade and repair operations.

## Result

ICE69 returns an error if a \[$componentkey\] substring within a [formatted](formatted.md) string cross-references a component in another feature. ICE69 returns a warning if a \[$componentkey\] substring within a formatted string cross-references a component in the same feature. (The [FeatureComponents](featurecomponents-table.md) table is used to determine this mapping. It must map to the same feature for the warning. Referencing components in parent features or referencing components in child features is considered to be an error.)

ICE69 reports an error if the \[\#FileKey\] substring within a [formatted](formatted.md) string references a file which is not specified in the [File](file-table.md) table as belonging to the same component.

## Example

ICE69 reports the following for the examples shown.

``` syntax
WARNING: "Mismatched component reference. Entry 'Test' of the Shortcut table belongs to component 'QuickTest'. However, the formatted string in column 'Argument' references component 'Test'. Components are in the same feature."
ERROR: "Mismatched component reference. Entry 'Shortcut2' of the Shortcut table belongs to component 'QuickTest'. However, the formatted string in column 'Argument' references component 'Test2'. Components are not in the same feature."
```

To fix this error, do not cross-reference components. Change the \[$componentkey\] to match the component of the shortcut.

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Component\_ | Argument     |
|-----------|-------------|--------------|
| Test      | QuickTest   | -v \[$Test\] |
| Shortcut2 | QuickTest   | \[$Test2\]   |



 

The [Verb](verb-table.md) and [Extension](extension-table.md) tables are special cases in that the Verb table references an extension that belongs to a component. An Extension, however, can belong to multiple components because the primary key for the extension table is made up of the Extension and Component\_ columns. You can logically have the following situation.

[Verb Table](verb-table.md) (partial)



| Extension | Verb\_ | Argument                |
|-----------|--------|-------------------------|
| tst       | open   | -v \[$comp1\]\[$comp2\] |



 

[Extension Table](extension-table.md) (partial)



| Extension | Component\_ |
|-----------|-------------|
| tst       | comp1       |
| tst       | comp2       |



 

[FeatureComponents Table](featurecomponents-table.md)



| Feature\_ | Component\_ |
|-----------|-------------|
| Feature1  | QuickTest   |
| Feature1  | Test        |
| Feature2  | Test2       |



 

In this case, you must ensure that at least one of the \[$componentkey\] properties evaluates to a non-null value. However, every \[$componentkey\] property in the Argument column of the Verb table (\[$comp1\] and \[$comp2\] in the above example) must reference a possible component included with the extension associated with the verb. A reference like \[$comp3\] would result in a warning from ICE69.

The [AppId table](appid-table.md) has a similar situation to the Verb table. It uses the [Class table](class-table.md) for its component reference. In this case, the AppId table is validated in the same way as the Verb-Extension validation (now AppId-Class).

The Class table's Argument column is validated like the [Shortcut](shortcut-table.md), [Registry](registry-table.md), and similar tables.

## Table used during execution (only if found)

[IniFile](inifile-table.md)

[RemoveIniFile](removeinifile-table.md)

[Registry](registry-table.md)

[RemoveRegistry](removeregistry-table.md)

[ServiceControl](servicecontrol-table.md)

[ServiceInstall](serviceinstall-table.md)

[Shortcut](shortcut-table.md)

[Verb](verb-table.md)

[Extension](extension-table.md)

[Class](class-table.md)

[AppId](appid-table.md)

[Environment](environment-table.md)

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



