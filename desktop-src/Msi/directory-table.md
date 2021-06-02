---
description: The Directory table specifies the directory layout for the product. Each row of the table indicates a directory both at the source and the target.
ms.assetid: eaca30cb-fec1-49ca-8b23-5e54c583e3e2
title: Directory Table
ms.topic: article
ms.date: 05/31/2018
---

# Directory Table

The Directory table specifies the directory layout for the product. Each row of the table indicates a directory both at the source and the target.

The Directory table has the following columns.



| Column            | Type                         | Key | Nullable |
|-------------------|------------------------------|-----|----------|
| Directory         | [Identifier](identifier.md) | Y   | N        |
| Directory\_Parent | [Identifier](identifier.md) | N   | Y        |
| DefaultDir        | [DefaultDir](defaultdir.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Directory"></span><span id="directory"></span><span id="DIRECTORY"></span>Directory
</dt> <dd>

The Directory column contains a unique identifier for a directory or directory path. This column can contain the name of a property that is set to the full path of a target directory. If this column contains a property, the target directory takes the name specified in the DefaultDir column and takes the parent directory specified in the Directory\_Parent column.

The source directory always takes the name specified in the DefaultDir column and takes the parent directory specified in the Directory\_Parent column.

If the Directory\_Parent column is either null or equal to the value of the Directory column, the Directory column represents a root target directory. Only one root directory may be specified in the Directory table.

</dd> <dt>

<span id="Directory_Parent"></span><span id="directory_parent"></span><span id="DIRECTORY_PARENT"></span>Directory\_Parent
</dt> <dd>

This column is a reference to the directory's parent directory. A record that has a Directory\_Parent column equal to null or equal to the Directory column represents a root directory. The full path of the parent directory is resolved by reference in the Directory\_Parent column is an external key into the Directory column. For example, if a folder has a parent directory named PDIR, the parent directory of PDIR is given in the Directory\_Parent column of the row with PDIR in the Directory column.

</dd> <dt>

<span id="DefaultDir"></span><span id="defaultdir"></span><span id="DEFAULTDIR"></span>DefaultDir
</dt> <dd>

The DefaultDir column contains the directory's name (localizable)under the parent directory. By default, this is the name of both the target and source directories. To specify different source and target directory names, separate the target and source names with a colon as follows: \[targetname\]:\[sourcename\].

If the value of the Directory\_Parent column is null or is equal to the Directory column, the DefaultDir column specifies the name of a root source directory.

For a non-root source directory, a period (.) entered in the DefaultDir column for the source directory name or the target directory name indicates the directory should be located in its parent directory without a subdirectory.

The directory names in this column may be formatted as short filename \| long filename pairs.

</dd> </dl>

## Remarks

Each record in the table represents a directory in both the source and the destination images. The Directory table must specify a single root directory with a Directory column value equal to the [**TARGETDIR**](targetdir.md) property.

For an [administrative installation](administrative-installation.md), install the administrative image into the root directory named TARGETDIR and use the source directory names to resolve the target directories.

Note the installer sets a number of standard [properties](properties.md) to system folder paths. See the [Property Reference](property-reference.md) for a list of the properties that are set to system folders.

Directory resolution is performed during the [CostFinalize action](costfinalize-action.md) and is done as follows:

### Root Destination Directory

There may only be a single root destination directory. To specify the root destination directory, set the Directory column to the [**TARGETDIR**](targetdir.md) property and the DefaultDir column to the [**SourceDir**](sourcedir.md) property. If the **TARGETDIR** property is defined, the destination directory is resolved to the property's value. If the **TARGETDIR** property is undefined, the [**ROOTDRIVE**](rootdrive.md) property is used to resolve the path.

### Root Source Directory

The value of the DefaultDir column for the root directory entry must be set to the [**SourceDir**](sourcedir.md) property.

### Non-root Destination Directories

The Directory value for a non-root directory is also interpreted as the name of a property defining the location of the destination. If the property is defined, the destination directory is resolved to the property's value. If the property is not defined, the destination directory is resolved to a subdirectory beneath the resolved destination directory for the Directory\_Parent entry. The DefaultDir value defines the name of the subdirectory.

### Non-root Source Directories

The source directory for a non-root directory is resolved to a subdirectory of the resolved source directory for the Directory\_Parent entry. Again, the DefaultDir value defines the name of the subdirectory.

### Short or Long File Names

When resolving destination directories, the short file names specified in the DefaultDir column are used if either the [**SHORTFILENAMES**](shortfilenames.md) property is set or the volume the directory is located on does not support long file names. Otherwise, the long file name is used.

Note that when the directories are resolved during the CostFinalize action, the keys in the Directory table become [properties](properties.md) set to directory paths.

[CreateFolder Table](createfolder-table.md)

For creating empty folders during an installation, see [CreateFolder Table](createfolder-table.md).

[Using the Directory Table](using-the-directory-table.md)

For more information about the Directory table, including samples, see [Using the Directory Table](using-the-directory-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE07](ice07.md)  
[ICE30](ice30.md)  
[ICE32](ice32.md)  
[ICE38](ice38.md)  
[ICE46](ice46.md)  
[ICE48](ice48.md)  
[ICE56](ice56.md)  
[ICE57](ice57.md)  
[ICE64](ice64.md)  
[ICE88](ice88.md)  
[ICE90](ice90.md)  
[ICE91](ice91.md)  
[ICE99](ice99.md)  
</dl>

 

 



