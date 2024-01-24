---
description: ICEM02 verifies that all the module dependencies and exclusions are related to the current module.
ms.assetid: c7d77cb6-0ee6-4857-a749-7908e1c5fcda
title: ICEM02
ms.topic: article
ms.date: 05/31/2018
---

# ICEM02

ICEM02 verifies that all the module dependencies and exclusions are related to the current module.

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM02 posts error messages if the module database attempts to specify dependencies or exclusions that do not relate to the current module. ICEM02 posts an error message if the module database attempts to specify the current module as dependent or as excluded by itself.

## Example

ICEM02 would post the following error messages for a module containing the database entries shown below.

``` syntax
The dependency OtherModule.GUID2.1033.OtherModule.GUID3.0 in the 
ModuleDependency table creates a dependency for an unrelated module. A 
module can only define dependencies for itself

This module is listed as depending on itself!

The exclusion OtherModule.GUID2.1033.OtherModule.GUID3.0 in the 
ModuleExclusion table creates an excluded module for an unrelated 
module. A module can only define exclusions for itself.

This module excludes itself from the target database!
```

[ModuleSignature Table](modulesignature-table.md)



| ModuleID         | Language | Version |
|------------------|----------|---------|
| MyModule.*GUID1* | 1033     | 1.0     |



 

[ModuleDependency Table](moduledependency-table.md)



| ModuleID            | ModuleLanguage | RequiredID          | RequiredLanguage | RequiredVersion |
|---------------------|----------------|---------------------|------------------|-----------------|
| OtherModule.*GUID2* | 1033           | OtherModule.*GUID3* | 0                | 1.0             |
| MyModule.*GUID1*    | 1033           | MyModule.*GUID1*    | 1033             | 1.2             |



 

[ModuleExclusion Table](moduleexclusion-table.md) (partial)



| ModuleID            | ModuleLanguage | ExcludedID          | ExcludedLanguage |
|---------------------|----------------|---------------------|------------------|
| OtherModule.*GUID2* | 1033           | OtherModule.*GUID3* | 0                |
| MyModule.*GUID1*    | 1033           | MyModule.*GUID1*    | 1033             |



 

The merge module ICE posts the first error because the of the first row in the ModuleDependency table, which does not specify a required dependency for the current module specified in the ModuleSignature table. The dependencies of a module can only be specified in its own ModuleDependency table. If OtherModule.*GUID3* is required by the current module, replace the first two columns of the row with the data from the ModuleSignature table. If OtherModule.*GUID3* is not required by this module, delete this row.

The merge module ICE posts the second error because a module cannot specify a dependency upon itself.

The merge module ICE posts the third error because of the first row in the ModuleExclusion table, which does not specify a required exclusion for the current module specified in the ModuleSignature table. The exclusions of a module can only be specified in its own ModuleExclusion table. If the current module excludes OtherModule.*GUID3*, replace the first two columns of the row with the data from the ModuleSignature table. If the current module does not exclude OtherModule.*GUID3*, delete this row.

The merge module ICE posts the fourth error because a module cannot specify that it exclude itself.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



