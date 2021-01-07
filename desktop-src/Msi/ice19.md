---
description: ICE19 validates that advertised components reference a file in the KeyPath column of the Component table and that an advertised shortcut references a directory in this column.
ms.assetid: 438153c1-bc4b-4ecf-ab85-d66ad69c987c
title: ICE19
ms.topic: article
ms.date: 05/31/2018
---

# ICE19

ICE19 validates that advertised components reference a file in the KeyPath column of the [Component table](component-table.md) and that an advertised shortcut references a directory in this column.

ICE19 validates that advertised components or shortcuts have a ComponentId. Components in the [PublishComponent table](publishcomponent-table.md), which are not advertised in another table, are only checked to see whether they have a ComponentId.

## Result

ICE19 posts an error message if the KeyPath column of the Component table does not reference a file in the case of an advertised component or a directory in the case of an advertised shortcut. ICE19 posts an error message if any advertised components or shortcuts do not have a ComponentId.

## Example

ICE19 posts the following error messages for the example shown:

-   Extension flp references the component Comp1 which does not have a ComponentId specified in the [Component table](component-table.md).
-   Extension exe references the component Comp4 which references a directory as its KeyPath. The KeyPath is Null in the Component table.
-   Shortcut Shortcut2 references the component Comp3 which references a Registry entry as the key path. The value of the Attributes column in the Component table is 4.

[Component Table](component-table.md) (partial)



| Component | ComponentId                            | Attributes | KeyPath |
|-----------|----------------------------------------|------------|---------|
| Comp1     | Null                                   | 0          | File1   |
| Comp2     | {00000002-0003-0000-0000-624474736554} | 0          | File2   |
| Comp3     | {00000003-0003-0000-0000-624474736554} | 4          | Reg3    |
| Comp4     | {00000004-0003-0000-0000-624474736554} | 0          | Null    |



 

[Extension Table](extension-table.md) (partial)



| Extension | Component\_ |
|-----------|-------------|
| flp       | Comp1       |
| tst       | Comp2       |
| exe       | Comp4       |



 

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Component\_ | Feature\_      |
|-----------|-------------|----------------|
| Shortcut1 | Comp4       | ProductFeature |
| Shortcut2 | Comp3       | ProductFeature |



 

[Feature Table](feature-table.md) (partial)



| Feature        |
|----------------|
| ProductFeature |



 

> [!Note]  
> If the extension flp and exe both reference the same component, the EXE or COM server that opens them must be the same. This EXE is normally the KeyPath for the Component. For OFFICE, the extensions doc and xls cannot reference the same component because the same EXE does not open both extensions. You need winword.exe to open doc extensions and you need excel.exe to open xls extensions.

 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



