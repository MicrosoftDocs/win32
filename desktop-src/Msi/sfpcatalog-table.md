---
description: The SFPCatalog table contains the catalogs used by Windows Me.
ms.assetid: 'e9dc65a9-4ec9-4310-b03a-a2c38720ca8c'
title: SFPCatalog Table
ms.topic: article
ms.date: 05/31/2018
---

# SFPCatalog Table

The SFPCatalog table contains the catalogs used by Windows Me.

The SFPCatalog table has the following columns.



| Column     | Type                       | Key | Nullable |
|------------|----------------------------|-----|----------|
| SFPCatalog | [Filename](filename.md)   | Y   | N        |
| Catalog    | [Binary](binary.md)       | N   | N        |
| Dependency | [Formatted](formatted.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="SFPCatalog"></span><span id="sfpcatalog"></span><span id="SFPCATALOG"></span>SFPCatalog
</dt> <dd>

The short file name for the catalog. Because catalogs have no version, the catalog specified in this column can overwrite a catalog that has the same name and is already installed on the local system. See the file versioning topic [Neither File Has a Version](neither-file-has-a-version.md).

</dd> <dt>

<span id="Catalog"></span><span id="catalog"></span><span id="CATALOG"></span>Catalog
</dt> <dd>

Binary data for the catalog.

</dd> <dt>

<span id="Dependency"></span><span id="dependency"></span><span id="DEPENDENCY"></span>Dependency
</dt> <dd>

The catalog specified in this field is the parent of the dependent catalog specified in the SFPCatalog field. Enter the short file name of the parent catalog into the Dependency field. This field is a key back into the SFPCatalog column. The dependency match is case sensitive.

If the Dependency field references another record in this SFPCatalog table, the parent catalog is installed before the dependent catalog.

If the Dependency field references a parent catalog that is not present in the SFPCatalog field of this table, and if the parent catalog is not already installed, the installation fails.

</dd> </dl>

## Remarks

The [InstallSFPCatalogFile action](installsfpcatalogfile-action.md) queries the [Component table](component-table.md), [File table](file-table.md), [FileSFPCatalog table](filesfpcatalog-table.md) and SFPCatalog table.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE29](ice29.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE66](ice66.md)  
</dl>

 

 



