---
description: ICE67 checks that the target of a non-advertised shortcut belongs to the same component as the shortcut itself, or that the attributes of the target component ensure that it does not change installation locations.
ms.assetid: 3fc462e7-4c11-4167-a157-6c1e0791901d
title: ICE67
ms.topic: article
ms.date: 05/31/2018
---

# ICE67

ICE67 checks that the target of a non-advertised shortcut belongs to the same component as the shortcut itself, or that the attributes of the target component ensure that it does not change installation locations.

Failure to fix a warning or error reported by ICE67 can cause the shortcut to be invalid if the target component changes state and the source component does not. For example, when the target file's component is set to run from source, a reinstallation that changes the component to local results in the component containing the shortcut not being reinstalled. Thus the shortcut points to an invalid location.

Note that in some cases, using a different component for the shortcut is unavoidable. For example, if the shortcut is created in the user profile and the file is installed to a non-profile directory, you may not be able to use the same component for both pieces of data. (This results in failures in multi-user scenarios – such as those described in [ICE57](ice57.md)). In this case, you may be able to use advertised shortcuts to achieve the behavior you want, or you can simply ensure that the target component cannot change from run-from-source to local.

## Result

ICE67 returns an error or a warning if the target of a non-advertised shortcut does not belong to the same component as the shortcut itself, or if the attributes of the target component do not ensure that the installation locations will not change.

## Example

ICE67 reports the following warning and errors for the example shown.

``` syntax
The shortcut 'Shortcut1' is a non-advertised shortcut with a file target. The shortcut and target are installed by different components, and the target component can run locally or from source.
```

Shortcut1 is installed by Component2, but its target file, File1, is installed by component1. The target component is marked optional (meaning that it can be local or run-from-source). One possible situation that would cause a problem is if Component1 changes from run-from-source to local. This would cause Shortcut1 to point to an invalid location.

To fix this warning, Install the shortcut as part of Component1, or mark Component1 as LocalOnly or SourceOnly.

[File Table](file-table.md) (partial)



| File  | Component\_ |
|-------|-------------|
| File1 | Component1  |



 

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Component\_ | Target      |
|-----------|-------------|-------------|
| Shortcut1 | Component2  | \[\#File1\] |



 

[Component Table](component-table.md) (partial)



| Component  | Attributes |
|------------|------------|
| Component1 | 2          |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



