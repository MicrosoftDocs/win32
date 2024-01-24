---
description: ICE38 validates that every component being installed under the current user's profile also specifies a registry key under the HKEY\_CURRENT\_USER root in the KeyPath column of the Component table.
ms.assetid: f1548b04-78c2-461a-a729-9a8c4856d0d8
title: ICE38
ms.topic: article
ms.date: 05/31/2018
---

# ICE38

ICE38 validates that every component being installed under the current user's profile also specifies a registry key under the **HKEY\_CURRENT\_USER** root in the KeyPath column of the [Component table](component-table.md).

## Result

ICE38 posts an error if a component installed under the user's profile does not specify a HKCU registry key.

## Example

ICE38 reports the following errors for the sample shown.



| ICE38 error                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Component Component1 installs to user profile. It must use a registry key under HKCU as its KeyPath, not a file.                    | The value of the attributes column of Component1 is 0, meaning that the component must use a file as its KeyPath. This causes difficulties when multiple users install the component on the same computer. To fix this error on Component1, set the RegistryKeyPath bit in the Attributes column of the [Component table](component-table.md) and change the entry in the KeyPath column to a value listed in the Registry column of the [Registry table](registry-table.md).<br/>                                                                                |
| Component Component2 installs to user profile. It must use a registry key under HKCU as its KeyPath. The KeyPath is currently NULL. | Component2 has the RegistryKeyPath bit set in the Attributes column of the [Component table](component-table.md). The KeyPath field must therefore contain a key to the Registry column of the [Registry Table](registry-table.md) but the KeyPath column is Null. To fix this error, change the KeyPath value to a valid entry into the Registry table.<br/>                                                                                                                                                                                                     |
| Component Component3 installs to user profile. It's KeyPath registry key must fall under HKCU.                                      | Component3 has the RegistryKeyPath bit set in the Attributes column of the [Component table](component-table.md) but the root of the registry entry specified in the Root column of the Registry table specifies **HKEY\_LOCAL\_MACHINE** rather than **HKEY\_CURRENT\_USER**. To fix this error, use a valid registry entry under **HKEY\_LOCAL\_MACHINE** as the KeyPath for this component or change the value in the Root column of the [Registry table](registry-table.md) to -1 or 1.<br/>                                                                  |
| The KeyPath registry entry for component Component4 does not exist.                                                                 | Component4 has the RegistryKeyPath bit set in the Attributes column of the [Component table](component-table.md) but the entry in the KeyPath column does not exist in the [Registry Table](registry-table.md). To fix this error, add an entry for Reg4 to the Registry table that is a under **HKEY\_CURRENT\_USER**.<br/>                                                                                                                                                                                                                                      |
| The Registry Entry Reg5 is set as the KeyPath for component Component5, but that registry entry does not belong to Component5.      | The Registry entry referenced in the KeyPath column of the component was found and lies under the HKCU tree, but the registry entry's Component\_ column does not refer back to the same component that listed it as the KeyPath. This means that the registry entry used as the KeyPath of the component would only be created when some other component was installed. To fix this error change the KeyPath value to refer to a registry entry that belongs to the component, or change the registry entry to belong to the component using it as a KeyPath.<br/> |



 

[Directory Table](directory-table.md) (partial)



| Directory | Directory\_Parent | DefaultDir      |
|-----------|-------------------|-----------------|
| Dir1      |                   | StartMenuFolder |
| Dir2      |                   | DesktopFolder   |
| Dir3      | Dir3              | AppData         |
| Dir4      | Dir3              | SubDir          |



 

[Component Table](component-table.md) (partial)



| Component  | Directory\_ | Attributes | KeyPath |
|------------|-------------|------------|---------|
| Component1 | Dir1        | 0          | File1   |
| Component2 | Dir2        | 4          |         |
| Component3 | Dir3        | 4          | Reg3    |
| Component4 | Dir4        | 4          | Reg4    |
| Component5 | Dir5        | 4          | Reg5    |



 

[Registry Table](registry-table.md) (partial)



| Registry | Root | Value | Component\_ |
|----------|------|-------|-------------|
| Reg3     | 2    |       | Component3  |
| Reg5     | 0    |       | Component4  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




