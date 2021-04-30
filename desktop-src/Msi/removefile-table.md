---
description: The RemoveFile table contains a list of files to be removed by the RemoveFiles action. Setting the FileName column of this table to Null supports the removal of empty folders.
ms.assetid: 8b3cb0e3-ccc0-4030-8f57-aa124c3b5588
title: RemoveFile Table
ms.topic: article
ms.date: 05/31/2018
---

# RemoveFile Table

The RemoveFile table contains a list of files to be removed by the [RemoveFiles action](removefiles-action.md). Setting the FileName column of this table to Null supports the removal of empty folders.

The RemoveFile table has the following columns.



| Column      | Type                                     | Key | Nullable |
|-------------|------------------------------------------|-----|----------|
| FileKey     | [Identifier](identifier.md)             | Y   | N        |
| Component\_ | [Identifier](identifier.md)             | N   | N        |
| FileName    | [WildCardFilename](wildcardfilename.md) | N   | Y        |
| DirProperty | [Identifier](identifier.md)             | N   | N        |
| InstallMode | [Integer](integer.md)                   | N   | N        |



 

## Columns

<dl> <dt>

<span id="FileKey"></span><span id="filekey"></span><span id="FILEKEY"></span>FileKey
</dt> <dd>

Primary key used to identify this particular table entry.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key the first column of the [Component table](component-table.md). This field references the component that controls the file to be removed.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

This column contains the localizable name of the file to be removed. If this column is null, then the specified folder will be removed if it is empty. All of the files that match the wildcard will be removed from the specified directory.

</dd> <dt>

<span id="DirProperty"></span><span id="dirproperty"></span><span id="DIRPROPERTY"></span>DirProperty
</dt> <dd>

Name of a property whose value is assumed to resolve to the full path to the folder of the file to be removed. The property can be the name of a directory in the [Directory table](directory-table.md), a property set by the [AppSearch table](appsearch-table.md), or any other property that represents a full path.

</dd> <dt>

<span id="InstallMode"></span><span id="installmode"></span><span id="INSTALLMODE"></span>InstallMode
</dt> <dd>

Must be one of the following values.



| Constant                                | Hexadecimal | Decimal | Description                                                                                                   |
|-----------------------------------------|-------------|---------|---------------------------------------------------------------------------------------------------------------|
| **msidbRemoveFileInstallModeOnInstall** | 0x001       | 1       | Remove only when the associated component is being installed (msiInstallStateLocal or msiInstallStateSource). |
| **msidbRemoveFileInstallModeOnRemove**  | 0x002       | 2       | Remove only when the associated component is being removed (msiInstallStateAbsent).                           |
| **msidbRemoveFileInstallModeOnBoth**    | 0x003       | 3       | Remove in either of the above cases.                                                                          |



 

</dd> </dl>

## Remarks

The file references in this table are processed by the [RemoveFiles action](removefiles-action.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE18](ice18.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE64](ice64.md)  
</dl>

 

 



