---
description: ICE57 validates that individual components do not mix per-machine and per-user data. This ICE custom action checks registry entries, files, directory key paths, and non-advertised shortcuts.
ms.assetid: 3c82efa7-9cf3-4bcd-8ec4-b81d1d7aa0a6
title: ICE57
ms.topic: article
ms.date: 05/31/2018
---

# ICE57

ICE57 validates that individual components do not mix per-machine and per-user data. This ICE custom action checks registry entries, files, directory key paths, and non-advertised shortcuts.

Mixing per-user and per-machine data in the same component could result in only partial installation of the component for some users in a multi-user environment.

See the [**ALLUSERS**](allusers.md) property.

## Result

ICE57 posts an error if it finds any component that contains both a per-machine and per-user registry entries, files, directory key paths, or non-advertised shortcuts.

## Example

ICE57reports the following errors for the example shown.

``` syntax
Component 'Component1' has both per-user and per-machine 
    data with a per-machine KeyPath. 
 
WARNING: Component 'Component2' has both per-user and 
    per-machine data with an HKCU Registry KeyPath. 
 
Component 'Component3' has a registry entry that 
    can be either per-user or per-machine and a per-machine KeyPath. 
 
Component 'Component4' has both per-user data and 
    a keypath that can be either per-user or per-machine.
```

[Component Table](component-table.md) (partial)



| Component  | Directory  | Attributes | KeyPath |
|------------|------------|------------|---------|
| Component1 | DirectoryA | 0          | FileA   |
| Component2 | DirectoryA | 4          | RegKeyB |
| Component3 | DirectoryA | 0          | FileC   |
| Component4 | DirectoryA | 4          | RegKeyD |



 

[Registry Table](registry-table.md) (partial)



| Registry | Root | Component\_ |
|----------|------|-------------|
| RegKeyA  | 1    | Component1  |
| RegKeyB  | 1    | Component2  |
| RegKeyC  | -1   | Component3  |
| RegKeyD  | -1   | Component4  |



 

[File Table](file-table.md) (partial)



| File  | Component\_ |
|-------|-------------|
| FileA | Component1  |
| FileB | Component2  |
| FileC | Component3  |
| FileD | Component4  |



 

[Directory Table](directory-table.md)



| Directory  | Directory\_Parent | DefaultDir |
|------------|-------------------|------------|
| TARGETDIR  |                   | SourceDir  |
| DirectoryA | TARGETDIR         | DirectoryA |



 

To fix the errors, reorganize the application such that each component contains only per-user or per-machine resources, and not both.

The first error message is posted because Component1 contains FileA (per-machine) and the HKCU registry key RegKeyA (per user).

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



