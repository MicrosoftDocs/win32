---
description: The AppSearch table contains properties needed to search for a file having a particular file signature. The AppSearch table can also be used to set a property to the existing value of a registry or .ini file entry.
ms.assetid: d560096f-6baa-4fea-8786-f4e3d5ee6bf4
title: AppSearch Table
ms.topic: article
ms.date: 05/31/2018
---

# AppSearch Table

The AppSearch table contains properties needed to search for a file having a particular file signature. The AppSearch table can also be used to set a property to the existing value of a registry or .ini file entry.

The AppSearch table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Property    | [Identifier](identifier.md) | Y   | N        |
| Signature\_ | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

Running the [AppSearch](appsearch-action.md) action sets this property to the location of the file indicated by the Signature\_ column. This property is set if the file signature exists on the user's computer. The properties used in this column must be [public](public-properties.md) properties and have an identifier that contains no lowercase letters.

The property listed in the Property field may be initialized in the [Property](property-table.md) table or from a command line. If the [AppSearch](appsearch-action.md) action locates the signature, the installer overrides the initialized property value with the found value. If the signature is not found, then the initial property value is used. If the property was never initialized, then the property will only be set if the signature is found. Otherwise, the property is undefined.

</dd> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

The Signature\_ column contains a unique identifier called a signature and is also an external key into the [RegLocator](reglocator-table.md), [IniLocator](inilocator-table.md), [CompLocator](complocator-table.md), and [DrLocator](drlocator-table.md) tables. When searching for a file, the value in this column must also be a foreign key into the [Signature](signature-table.md) table. If the value in this column is not listed in the Signature table, the installer determines that the search is for a directory.

</dd> </dl>

## Remarks

The [AppSearch](appsearch-action.md) action in [*sequence tables*](s-gly.md) processes the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

The [AppSearch](appsearch-action.md) action searches for signatures using the [CompLocator](complocator-table.md) table first, the [RegLocator](reglocator-table.md) table second, the [IniLocator](inilocator-table.md) table third, and finally the [DrLocator](drlocator-table.md) table. File signatures are listed in the [Signature](signature-table.md) table. A signature that is not in the Signature table denotes a directory and the action sets the property to the directory path for that signature.

See [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE52](ice52.md)  
[ICE88](ice88.md)  
</dl>

 

 



