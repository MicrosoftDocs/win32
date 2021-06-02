---
description: ICEM11 verifies that a Configurable Merge Module lists the ModuleConfiguration table and ModuleSubstitution table in the ModuleIgnoreTable table of the module.
ms.assetid: f0199137-0a40-40ca-b3cf-ff8eef4309cc
title: ICEM11
ms.topic: article
ms.date: 05/31/2018
---

# ICEM11

ICEM11 verifies that a Configurable Merge Module lists the [ModuleConfiguration table](moduleconfiguration-table.md) and [ModuleSubstitution table](modulesubstitution-table.md) in the [ModuleIgnoreTable table](moduleignoretable-table.md) of the module. This ensures that merge tools that do not recognize configurable merge modules(less than version 2.0) do not copy these tables into the target database.

This ICEM is available in the Mergemod.cub file provided in the Windows Installer 2.0 SDK and later. For details, see [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Result

ICEM11 posts an error if the module contains a ModuleConfiguration or ModuleSubstitution table not listed in the ModuleIgnoreTable table.

## Example

ICEM11 posts the following error messages for a module containing the database entries shown below.

``` syntax
Error The module contains a ModuleConfiguration or ModuleSubstitution 
table. These tables must be listed in the ModuleIgnoreTable table.
```

[ModuleConfiguration](moduleconfiguration-table.md) (partial)



| Name     | Format | Type   | ContextData | DefaultValue |
|----------|--------|--------|-------------|--------------|
| IconKey1 | 1      | Binary | Icon        | DefaultIcon  |



 

[ModuleSubstitution](modulesubstitution-table.md)



| Table   | Row              | Column | Value        |
|---------|------------------|--------|--------------|
| Control | Dialog1;Control1 | Text   | \[IconKey1\] |



 

[ModuleIgnoreTable](moduleignoretable-table.md)



| Table               |
|---------------------|
| ModuleConfiguration |



 

To fix this error include both the ModuleSubstitution and ModuleConfiguration tables in the ModuleIgnoreTable table.

## Table Used During Execution

[ModuleSubstitution](modulesubstitution-table.md)

[ModuleConfiguration](moduleconfiguration-table.md)

[ModuleIgnoreTable](moduleignoretable-table.md)

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



