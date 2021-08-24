---
description: ICEM08 ensures that a module does not exclude another module that it depends on.
ms.assetid: 56d115b4-7410-4db2-a9af-bc6716f3358d
title: ICEM08
ms.topic: article
ms.date: 05/31/2018
---

# ICEM08

ICEM08 ensures that a module does not exclude another module that it depends on.

## Result

ICEM08 posts an error when a module excludes another module that it depends on.

## Example

ICEM08 posts the following error message for a module containing the database entries shown in the example.

``` syntax
Error: This module requires module ModuleB.<GUID> (1033v1.0) but also 
lists it as an exclusion.
```

[ModuleDependency Table](moduledependency-table.md)



| ModuleID             | ModuleLanguage | RequiredID           | RequiredLanguage | RequiredVersion |
|----------------------|----------------|----------------------|------------------|-----------------|
| ModuleA.&lt;GUID&gt; | 1033           | ModuleB.&lt;GUID&gt; | 1033             | 1.0             |



 

[ModuleExclusion Table](moduleexclusion-table.md)



| ModuleID             | ModuleLanguage | ExcludedID           | ExcludedLanguage | ExcludedMinVersion | ExcludedMaxVersion |
|----------------------|----------------|----------------------|------------------|--------------------|--------------------|
| ModuleA.&lt;GUID&gt; | 1033           | ModuleB.&lt;GUID&gt; | 1033             |                    | 1.0                |



 

To fix the error, remove either the dependency or the exclusion. If ModuleB is a dependency (RequiredID) of ModuleA, you cannot exclude it (as shown in the ExludedID column of the ModuleExclusion table). If you must exclude ModuleB, then you must remove ModuleA's dependency on it.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



