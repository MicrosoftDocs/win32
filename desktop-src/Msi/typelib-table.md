---
description: The TypeLib table contains the information that needs to be placed in the registry registration of type libraries.
ms.assetid: 86b827ed-e707-4627-9488-78eafb444d32
title: TypeLib Table
ms.topic: article
ms.date: 05/31/2018
---

# TypeLib Table

The TypeLib table contains the information that needs to be placed in the registry registration of type libraries.

The TypeLib table has the following columns.



| Column      | Type                               | Key | Nullable |
|-------------|------------------------------------|-----|----------|
| LibID       | [GUID](guid.md)                   | Y   | N        |
| Language    | [Integer](integer.md)             | Y   | N        |
| Component\_ | [Identifier](identifier.md)       | Y   | N        |
| Version     | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Description | [Text](text.md)                   | N   | Y        |
| Directory\_ | [Identifier](identifier.md)       | N   | Y        |
| Feature\_   | [Identifier](identifier.md)       | N   | N        |
| Cost        | [DoubleInteger](doubleinteger.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="LibID"></span><span id="libid"></span><span id="LIBID"></span>LibID
</dt> <dd>

The GUID that identifies the library.

</dd> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

The language of the type library. This must be a non-negative number.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the first column of the [Component table](component-table.md). This column identifies the component belonging to Feature\_ whose key file is the type library being registered.

</dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

This is the version of the library. The major and minor versions are encoded in the four byte integer value. The minor version is in the lower eight bits. The major version is in the middle sixteen bits.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

A localizable description of the library.

</dd> <dt>

<span id="Directory_"></span><span id="directory_"></span><span id="DIRECTORY_"></span>Directory\_
</dt> <dd>

External key into the first column of the [Directory table](directory-table.md). This column identifies the Help path for the type library. This column is ignored during advertising.

</dd> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

External key into the first column of the [Feature table](feature-table.md). This column specifies the feature that must be installed for the type library to be operational.

</dd> <dt>

<span id="Cost"></span><span id="cost"></span><span id="COST"></span>Cost
</dt> <dd>

The cost associated with the registration of the type library in bytes. This must be a non-negative number or null.

</dd> </dl>

## Remarks

This table is referred to when the [RegisterTypeLibraries action](registertypelibraries-action.md) or the [UnregisterTypeLibraries action](unregistertypelibraries-action.md) is executed.

The installer writes all type library registration information into the HKEY\_LOCAL\_MACHINE (HKLM) registry location. This is the case even for per-user installations. Type libraries cannot be registered in per-user locations (HKCU).

Installation package authors are strongly advised against using the TypeLib table. Instead, they should register type libraries by using the [Registry](registry-table.md) table. Reasons for avoiding self registration include:

-   If an installation using the TypeLib table fails and must be rolled back, the rollback may not restore the computer to the same state that existed prior to the rollback. Type libraries registered prior to rollback may not be registered after rollback.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE19](ice19.md)  
[ICE32](ice32.md)  
</dl>

 

 



