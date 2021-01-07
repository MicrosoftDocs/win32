---
description: ICEM05 verifies that the merge module is correctly associated with components in the module. Incorrectly associating a component with a module causes the component to be incorrectly associated with the target database.
ms.assetid: 1bf4041e-b198-4897-8719-8505fd8180ec
title: ICEM05
ms.topic: article
ms.date: 05/31/2018
---

# ICEM05

ICEM05 verifies that the merge module is correctly associated with components in the module. Incorrectly associating a component with a module causes the component to be incorrectly associated with the target database.

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM05 posts an error if the module database incorrectly associates components and the module.

## Example

ICEM05 posts the following error messages for a module containing the database entries shown below.

``` syntax
The component Component2.OtherModule.GUID2.1033 in the 
ModuleComponents table does not belong to this Merge Module.
The component Component1.MyModule.GUID1.1033 in the ModuleComponents 
table is not listed in the Component table.
The component 'Component3' in the Component table is not listed in the 
ModuleComponents table.
```

[ModuleSignature Table](modulesignature-table.md)



| ModuleID         | Language | Version |
|------------------|----------|---------|
| MyModule.*GUID1* | 1033     | 1.0     |



 

[**ModuleComponents Table**](modulecomponents-table.md)



| Component  | ModuleID            | Language |
|------------|---------------------|----------|
| Component1 | MyModule.*GUID1*    | 1033     |
| Component2 | OtherModule.*GUID2* | 1033     |



 

[Component Table](component-table.md) (partial)



| Component  | ComponentID |
|------------|-------------|
| Component3 | *GUID4*     |
| Component2 | *GUID5*     |



 

The merge module ICE reports the first error because the ModuleComponents table attempts to associate a component with another module that is not the current module specified in the ModuleSignature table. To fix this, change the ModuleID and Language columns of the ModuleComponents record for Component2 to that for the current module, MyModule.*GUID1*.

The merge module ICE reports the second error because the first record in the ModuleComponents table attempts to associate Component1 with the module. This component does not exist in the Component Table of the merge module. A module can only be associated with a component that exists in the module. To fix this, remove the record for the non-existent component.

The merge module ICE reports the third error because the module attempts to add Component3 to the target database. This component has not been associated with the module in the ModuleComponents table. To fix this error, add a record for Component3 to the ModuleComponents table.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



