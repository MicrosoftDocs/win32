---
description: The RemoveRegistry table contains the registry information the application needs to delete from the system registry.
ms.assetid: 8be382f1-f5ab-4a9d-bf0e-05275310c5b5
title: RemoveRegistry Table
ms.topic: article
ms.date: 05/31/2018
---

# RemoveRegistry Table

The RemoveRegistry table contains the registry information the application needs to delete from the system registry.

The RemoveRegistry table has the following columns.



| Column         | Type                         | Key | Nullable |
|----------------|------------------------------|-----|----------|
| RemoveRegistry | [Identifier](identifier.md) | Y   | N        |
| Root           | [Integer](integer.md)       | N   | N        |
| Key            | [RegPath](regpath.md)       | N   | N        |
| Name           | [Formatted](formatted.md)   | N   | Y        |
| Component\_    | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="RemoveRegistry"></span><span id="removeregistry"></span><span id="REMOVEREGISTRY"></span>RemoveRegistry
</dt> <dd>

The key for this table.

</dd> <dt>

<span id="Root"></span><span id="root"></span><span id="ROOT"></span>Root
</dt> <dd>

The predefined root key for the registry value.



| Constant                          | Hexadecimal | Decimal | Root key                                                                                                                                                                                                           |
|-----------------------------------|-------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (none)                            | \- 0x001    | -1      | **HKEY\_CURRENT\_USER** Installer sets this key while doing a per-user installation.<br/>                                                                                                                    |
| (none)                            | -0x001      | -1      | **HKEY\_LOCAL\_MACHINE**Installer sets this key while doing an all-users installation with [**ALLUSERS**](allusers.md) set to 1.<br/>                                                                       |
| **msidbRegistryRootClassesRoot**  | 0x000       | 0       | **HKEY\_CLASSES\_ROOT**The installer removes the value from the **HKCU\\Software\\Classes** hive during installations in the per-user and per-machine [installation context](installation-context.md).<br/> |
| **msidbRegistryRootCurrentUser**  | 0x001       | 1       | **HKEY\_CURRENT\_USER**                                                                                                                                                                                            |
| **msidbRegistryRootLocalMachine** | 0x002       | 2       | **HKEY\_LOCAL\_MACHINE**                                                                                                                                                                                           |
| **msidbRegistryRootUsers**        | 0x003       | 3       | **HKEY\_USERS**                                                                                                                                                                                                    |



 

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

The localizable key for the registry value.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

The localizable registry value name.

The following string in the Name column has special significance.



| String | Meaning                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------|
| "-"    | The key is to be deleted, if present, with all of its values and subkeys, when the component is installed. |



 

Note that the [Registry table](registry-table.md) should be used to create or remove a registry key when the component is removed.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the first column of the [Component table](component-table.md) referencing the component that controls the deletion of the registry value.

</dd> </dl>

## Remarks

The registry information is deleted from the system registry when the corresponding component has been selected to be installed locally or run from source.

This table is referred to when the [RemoveRegistryValues action](removeregistryvalues-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 




