---
description: ICE25 validates that a .msi file satisfies all of its internal merge module dependencies and exclusions.
ms.assetid: e6e3ea44-a1d4-451a-b326-e8fb7ed4adeb
title: ICE25
ms.topic: article
ms.date: 05/31/2018
---

# ICE25

ICE25 validates that a .msi file satisfies all of its internal [merge module](merge-modules.md) dependencies and exclusions. ICE validates the following:

-   That all merge module dependencies indicated in the .msi file's [ModuleDependency table](moduledependency-table.md) are satisfied by at least one merge module listed in the [ModuleSignature table](modulesignature-table.md).
-   That none of the excluded merge modules in the [ModuleExclusion table](moduleexclusion-table.md) are incompatible with the merge modules listed in the [ModuleSignature table](modulesignature-table.md).

## Result

ICE25 posts an error message if .msi file has previously been merged with an incompatible merge module or if it has not been merged with a necessary merge module.

## Example

ICE25 posts the following errors for the example shown.

``` syntax
Dependency failure: Need ModuleX@0 v2.0 
Module ModuleB@1033 v1.0 is excluded.
```

[ModuleSignature Table](modulesignature-table.md)



| ModuleID | Language | Version |
|----------|----------|---------|
| ModuleA  | 0        | 1.0     |
| ModuleB  | 1033     | 1.0     |



 

[ModuleDependency Table](moduledependency-table.md)



| ModuleID | ModuleLanguage | RequiredID | RequiredLanguage | RequiredVersion |
|----------|----------------|------------|------------------|-----------------|
| ModuleA  | 0              | ModuleX    | 0                | 2.0             |



 

[ModuleExclusion Table](moduleexclusion-table.md)



| ModuleID | ModuleLanguage | ExcludedID | ExcludedLanguage | ExcludedMinVersion | ExcludedMaxVersion |
|----------|----------------|------------|------------------|--------------------|--------------------|
| ModuleA  | 0              | ModuleB    | 1033             |                    |                    |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



