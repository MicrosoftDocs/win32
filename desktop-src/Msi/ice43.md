---
description: ICE43 validates that shortcuts that do not reference a feature as their Target (non-advertised shortcuts) are in components having a HKCU registry entry as their key path.
ms.assetid: 7e58e303-e512-4707-a0bf-2095ec8ec502
title: ICE43
ms.topic: article
ms.date: 05/31/2018
---

# ICE43

ICE43 validates that shortcuts that do not reference a feature as their Target (non-advertised shortcuts) are in components having a HKCU registry entry as their key path.

## Result

ICE43 posts an error message if a non-advertised shortcut is in a component that does not have a HKCU registry entry as its key path.

## Example

ICE43 would report the following errors for the example shown.



| ICE43 error                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Component Component1 has non-advertised shortcuts. It must use a registry key under HKCU as its KeyPath, not a file.                    | The attributes column of Component1 is 0, meaning that the component uses a file as its KeyPath. This causes non-advertised shortcuts in this component to be installed for the first user on the computer ONLY. Users who install the component later do not see the shortcuts because the component appear to the installer as already existing on the computer. To fix this error, set the RegistryKeyPath bit of the attributes to switch the Component to a Registry entry, then change the KeyPath value to a valid entry in the Registry table.<br/> |
| Component Component2 has non-advertised shortcuts. It must use a registry key under HKCU as its KeyPath. The KeyPath is currently null. | The Attributes column is set to use the registry, but the KeyPath is null. The KeyPath must refer to an entry in the Registry Table. To fix this error, change the KeyPath value to a valid entry in the Registry table.<br/>                                                                                                                                                                                                                                                                                                                               |
| Component Component3 has non-advertised shortcuts. Its KeyPath registry key must fall under HKCU.                                       | The Attributes column is set to use the registry, but the referenced registry entry is not under HKCU. To fix this error, either switch to a different registry entry as the KeyPath for this component, or change the Root value of the Registry entry to either -1 or 1.<br/>                                                                                                                                                                                                                                                                             |
| The KeyPath registry entry for component Component4 does not exist.                                                                     | The Registry entry referenced in the KeyPath column of the component is not in the Registry Table. To fix this error, create an entry.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The Registry Entry Reg5 is set as the KeyPath for component Component5, but that registry entry does not belong to Component5.          | There is a Registry entry referenced in the KeyPath column of the component that lies under the HKCU tree, but the registry entry's Component\_ column does not refer back to the same component that listed it as the KeyPath. This means that the registry entry used as the KeyPath of the component is only created if some other component was installed. To fix this error, change the KeyPath value to refer to a registry entry that belongs to the component or change the registry entry to belong to the component using it as a KeyPath.<br/>   |



 

[Component Table](component-table.md) (partial)



| Component  | Attributes | KeyPath |
|------------|------------|---------|
| Component1 | 0          | File1   |
| Component2 | 4          |         |
| Component3 | 4          | Reg3    |
| Component4 | 4          | Reg4    |
| Component5 | 4          | Reg5    |



 

[Registry Table](registry-table.md) (partial)



| Registry | Root | Value | Component\_ |
|----------|------|-------|-------------|
| Reg3     | 2    |       | Component3  |
| Reg5     | 0    |       | Component4  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




