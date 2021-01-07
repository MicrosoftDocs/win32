---
description: The CompLocator Table contains the information needed to find a file or directory that is using the installer configuration data.
ms.assetid: 8b527307-51bf-47b3-a0b2-3421cc5278b7
title: CompLocator Table
ms.topic: article
ms.date: 05/31/2018
---

# CompLocator Table

The CompLocator Table contains the information needed to find a file or directory that is using the installer configuration data.

The CompLocator table contains the following information.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Signature\_ | [Identifier](identifier.md) | Y   | N        |
| ComponentId | [GUID](guid.md)             | N   | N        |
| Type        | [Integer](integer.md)       | N   | Y        |



 

## Column Information

<dl> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

This column represents a unique file signature and is also the external key into the [Signature Table](signature-table.md). If the key is absent from the Signature Table, the search is assumed to be for the presence of a directory pointed to by the CompLocator Table.

</dd> <dt>

<span id="ComponentId"></span><span id="componentid"></span><span id="COMPONENTID"></span>ComponentId
</dt> <dd>

The component ID of the component whose key path is to be used for the search. This should be the GUID of a component that appears in the ComponentId field of the [Component Table](component-table.md). It may be the component ID of a component belonging to another product installed on the computer. It should not be the GUID of a published component appearing in the ComponentId field of the [PublishComponent Table](publishcomponent-table.md).

To find the component ID GUID value for a file installed by another product, go to the installation package of the product. Go to the [File Table](file-table.md) and find the row that contains the file identifier for the file. The Component\_ column of this row contains the component identifier for the component that controls the file. Go to the [Component table](component-table.md) and find the row that contains this component identifier in the Component column. The ComponentId column of this row contains the component ID GUID.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

A Boolean value that determines if the key path of the component is a file name or a directory location.

The following table lists valid values. If absent, Type is set to be 1 (one).



| Constant                      | Hexadecimal | Decimal | Description              |
|-------------------------------|-------------|---------|--------------------------|
| **msidbLocatorTypeDirectory** | 0x000       | 0       | Key path is a directory. |
| **msidbLocatorTypeFileName**  | 0x001       | 1       | Key path is a file name. |



 

</dd> </dl>

## Remarks

This table is used with the [AppSearch Table](appsearch-table.md).

Typically, the columns in this table are not localized. If an author decides to search for products in multiple languages, then there can be a separate entry included in the table for each language.

For more information, see [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 



