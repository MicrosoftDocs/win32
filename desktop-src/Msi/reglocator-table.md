---
description: The RegLocator table holds the information needed to search for a file or directory using the registry, or to search for a particular registry entry itself. This table has the following columns.
ms.assetid: dc88b083-cc1d-46d7-9be8-29ebbf3767a0
title: RegLocator Table
ms.topic: article
ms.date: 05/31/2018
---

# RegLocator Table

The RegLocator table holds the information needed to search for a file or directory using the registry, or to search for a particular registry entry itself. This table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Signature\_ | [Identifier](identifier.md) | Y   | N        |
| Root        | [Integer](integer.md)       | N   | N        |
| Key         | [RegPath](regpath.md)       | N   | N        |
| Name        | [Formatted](formatted.md)   | N   | Y        |
| Type        | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

The value in the Signature\_ field represents a unique signature that is an external key into column one of the [Signature](signature-table.md) table. If this signature is present in the Signature table, the search is for a file. If this signature is absent from the Signature table, and the value of the Type column is **msidbLocatorTypeRawValue**, the search is for the registry key name pointed to by the RegLocator table. Otherwise the search is for a directory pointed to by the RegLocator table.

</dd> <dt>

<span id="Root"></span><span id="root"></span><span id="ROOT"></span>Root
</dt> <dd>

The predefined root key for the registry value.



| Constant                          | Hexadecimal | Decimal | Root key             |
|-----------------------------------|-------------|---------|----------------------|
| **msidbRegistryRootClassesRoot**  | 0x000       | 0       | HKEY\_CLASSES\_ROOT  |
| **msidbRegistryRootCurrentUser**  | 0x001       | 1       | HKEY\_CURRENT\_USER  |
| **msidbRegistryRootLocalMachine** | 0x002       | 2       | HKEY\_LOCAL\_MACHINE |
| **msidbRegistryRootUsers**        | 0x003       | 3       | HKEY\_USERS          |



 

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

The key for the registry value.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

The registry value name. If this value is null, then the value from the key's unnamed or default value, if any, is retrieved.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

A value that determines if the registry value is a file name, a directory location, or raw registry value.

The following table lists valid values. Set one of the first three values and **msidbLocatorType64bit** if necessary. If the entry in this field is absent, Type is set to be 1.



| Constant                      | Hexadecimal | Decimal | Description                                                                                                                                                        |
|-------------------------------|-------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **msidbLocatorTypeDirectory** | 0x000       | 0       | Key path is a directory.                                                                                                                                           |
| **msidbLocatorTypeFileName**  | 0x001       | 1       | Key path is a file name.                                                                                                                                           |
| **msidbLocatorTypeRawValue**  | 0x002       | 2       | Key path is a registry value.                                                                                                                                      |
| **msidbLocatorType64bit**     | 0x010       | 16      | Set this bit to have the installer search the 64-bit portion of the registry. Do not set this bit to have the installer search the 32-bit portion of the registry. |



 

</dd> </dl>

## Remarks

Note that if the value in the Type field is **msidbLocatorTypeRawValue**, the installer sets the value of the property specified in the Property field of the [AppSearch](appsearch-table.md) table to the registry value. The installer adds a prefix to the registry value that identifies the type of registry value. For more information about types of registry values, see [Registry Value Types](../sysinfo/registry-value-types.md).



| Registry type   | Prefix added by Installer                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| REG\_SZ         | None, but if the first character of the registry value is \#, the installer escapes the character by prefixing a another \#.            |
| DWORD           | "\#" optionally followed by '+' or '-'                                                                                                  |
| REG\_EXPAND\_SZ | "\#%"                                                                                                                                   |
| REG\_MULTI\_SZ  | Null. The installer sets the property to a value beginning with a null and ending with a null.                                          |
| REG\_BINARY     | "\#x" In case of REG\_BINARY, the installer converts and saves each hexadecimal digit (nibble) as an ASCII character prefixed by "\#x". |



 

Typically, the columns in this table are not localized. If an author decides to search for products in multiple languages, then there must be a separate entry included in the table for each language.

Note that it is not possible to use the RegLocator table to check only for the presence of the key. However, you can search for the default value of a key and retrieve its value if it is not empty.

For more information, see [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
[ICE80](ice80.md)  
</dl>

 

 
