---
description: The ModuleComponents table contains a list of the components found in the merge module.
ms.assetid: def96d52-c9fa-4fac-b575-f9de8eb82d1c
title: ModuleComponents Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleComponents Table

The ModuleComponents table contains a list of the components found in the merge module.

The ModuleComponents table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Component | [Identifier](identifier.md) | Y   | N        |
| ModuleID  | [Identifier](identifier.md) | Y   | N        |
| Language  | [Integer](integer.md)       | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Component"></span><span id="component"></span><span id="COMPONENT"></span>Component
</dt> <dd>

An identifier referring to a component in the merge module. The Component column is a foreign key to the [Component table](component-table.md). The entry in the Component column must follow the naming convention in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md).

</dd> <dt>

<span id="ModuleID"></span><span id="moduleid"></span><span id="MODULEID"></span>ModuleID
</dt> <dd>

The identifier for the merge module. This is a foreign key to the [ModuleSignature table](modulesignature-table.md).

</dd> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

The Language identifier describes the default language for the merge module. The language identifier is in decimal format, for example, U.S. English is 1033. Foreign key to the [ModuleSignature table](modulesignature-table.md).

</dd> </dl>

## Remarks

Language transforms must be able to update this table if the merge module supports multiple languages.

 

 



