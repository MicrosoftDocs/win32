---
description: The File Table contains a complete list of source files with their various attributes, ordered by a unique, non-localized, identifier.
ms.assetid: '31d0e727-a9eb-4cd2-a211-ea7b138d0173'
title: File Table
ms.topic: article
ms.date: 05/31/2018
---

# File Table

The File Table contains a complete list of source files with their various attributes, ordered by a unique, non-localized, identifier. Files can be stored on the source media as individual files or compressed within a [*cabinet file*](c-gly.md). For more information, see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

The File Table has the following columns.



| Column      | Type                               | Key | Nullable |
|-------------|------------------------------------|-----|----------|
| File        | [Identifier](identifier.md)       | Y   | N        |
| Component\_ | [Identifier](identifier.md)       | N   | N        |
| FileName    | [Filename](filename.md)           | N   | N        |
| FileSize    | [DoubleInteger](doubleinteger.md) | N   | N        |
| Version     | [Version](version.md)             | N   | Y        |
| Language    | [Language](language.md)           | N   | Y        |
| Attributes  | [Integer](integer.md)             | N   | Y        |
| Sequence    | [Integer](integer.md)             | N   | N        |



 

## Columns

<dl> <dt>

<span id="File"></span><span id="file"></span><span id="FILE"></span>File
</dt> <dd>

A non-localized token that uniquely identifies the file. This field is insensitive to case. Do not assign identifiers to different files that differ only by their case.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

The external key into the first column of the [Component Table](component-table.md). This field identifies the Component that controls the file.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The file name used for installation. The name may be localized.

Because some web servers can be case sensitive, FileName should match the case of the source files exactly to ensure support of Internet downloads.

</dd> <dt>

<span id="FileSize"></span><span id="filesize"></span><span id="FILESIZE"></span>FileSize
</dt> <dd>

The size of the file in bytes. This must be a non-negative number.

</dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

This field is the version string for a versioned file. This field is blank for non-versioned files. The file version entered into this field must be identical to the version of the file included with the installation package.

The Version field can also be set to contain the primary key of another record in the File table. The referenced file then determines the versioning logic for this file. For more information, see [Companion Files](companion-files.md). Note that if this file is the key path for its component, it must not be specified as a companion file.

</dd> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

A list of decimal language IDs separated by commas.

Font files should not be authored with a language ID, as fonts do not have an embedded language ID resource. Thus this column should be left null for font files.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

The integer that contains bit flags that represent file attributes.

The following table shows the definition of the bit field.



| Constant                             | Hexadecimal | Decimal | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------|-------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **msidbFileAttributesReadOnly**      | 0x000001    | 1       | Read-Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **msidbFileAttributesHidden**        | 0x000002    | 2       | Hidden                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **msidbFileAttributesSystem**        | 0x000004    | 4       | System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **msidbFileAttributesVital**         | 0x000200    | 512     | The file is vital for the accurate operation of the component to which it belongs. If the installation of a file with the msidbFileAttributesVital attribute fails, the installation stops and is rolled back. In this case, the Installer displays a dialog box without an Ignore button. If this attribute is not set, and the installation of the file fails, the Installer displays a dialog box with an Ignore button. In this case, the user can choose to ignore the failure to install the file and continue. <br/> |
| **msidbFileAttributesChecksum**      | 0x000400    | 1024    | The file contains a valid [*checksum*](c-gly.md). A checksum is required to repair a file that has become corrupted.                                                                                                                                                                                                                                                                                                                                                                                           |
| **msidbFileAttributesPatchAdded**    | 0x001000    | 4096    | This bit must only be added by a patch and if the file is being added by the patch.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **msidbFileAttributesNoncompressed** | 0x002000    | 8192    | The file's source type is uncompressed. If set, ignore the [**Word Count Summary**](word-count-summary.md) Property. If neither **msidbFileAttributesNoncompressed** or **msidbFileAttributesCompressed** are set, the compression state of the file is specified by the **Word Count Summary** Property. Do not set both **msidbFileAttributesNoncompressed** and **msidbFileAttributesCompressed**.                                                                                                                            |
| **msidbFileAttributesCompressed**    | 0x004000    | 16384   | The file's source type is compressed. If set, ignore the [**Word Count Summary**](word-count-summary.md) Property. If neither **msidbFileAttributesNoncompressed** or **msidbFileAttributesCompressed** are set, the compression state of the file is specified by the **Word Count Summary** Property. Do not set both **msidbFileAttributesNoncompressed** and **msidbFileAttributesCompressed**.                                                                                                                              |



 

If the **msidbFileAttributesVital** bit within the Attributes column is set, and if the component to which the file belongs is selected for installation, then the installer must be able to install this file for the installation to be completed successfully. If the installer is unable to install the file for some reason (for example, if the source file cannot be located within the source image), then an error dialog box will appear with the options "Retry" or "Cancel". For a file that does not have **msidbFileAttributesVital** set, the options in case of an install error will be "Abort", "Retry", and "Ignore" (that is, the user will have the option to complete the install successfully without installing that file).

The **msidbFileAttributesChecksum** bit within the Attributes column should be set for every executable file in the installation that has a valid [*checksum*](c-gly.md) stored in the Portable Executable (PE) file header. Only those files that have this bit set will ever be verified for valid checksum during a reinstall. For more information, see the [**REINSTALLMODE**](reinstallmode.md).

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

Sequence position of this file on the media images. This order must correspond to the order of the files in the cabinet if the files are compressed. The integers in this field must be equal or greater than 1.

The sequence numbers in the Sequence column are used to specify both the order of installation for files and the source media upon which the file is located (in conjunction with the [Media Table](media-table.md)). For example, suppose a file has a sequence number of 92. To determine the source disk this file resides on, look in the Media table for the entry with the smallest Last Sequence value that is larger than 92.

Although compressed files are assigned internal sequence numbers within cabinets, those absolute numbers do not need to match the sequence numbers within the File table. It is, however, important that the sequence of files in the File table be identical to the sequence of the files within the cabinets.

For files that are not compressed, the sequence numbers need not be unique. For instance, if all your files are uncompressed, and all reside on one disk, you could give all the files the same sequence number.

The maximum limit is 32767 files. To create a Windows Installer package with more files, see [Authoring a Large Package](authoring-a-large-package.md).

</dd> </dl>

## Remarks

The [InstallFiles](installfiles-action.md) and [RemoveFiles](removefiles-action.md) actions in the [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

The table is initially generated from the file list, but if cabinet compression is used, the table is regenerated from the output of the compression engine. For more information, see [Cabinet Files](cabinet-files.md).

To move an existing file on the user's computer during the installation use the [MoveFiles Action](movefiles-action.md) and [MoveFile Table](movefile-table.md). To install a file to multiple locations use the [DuplicateFiles Action](duplicatefiles-action.md) and the [DuplicateFile Table](duplicatefile-table.md).

The following table summarizes the possible combinations of values in the Version column and the Language column. For more information, see [File Versioning Rules](file-versioning-rules.md).



| Version | Language | Description                                                                     |
|---------|----------|---------------------------------------------------------------------------------|
| 1.2.3.4 | 1033     | The version and language.                                                       |
| 1.2.3.4 | (Null)   | The version but no language.                                                    |
| 1.2.3.4 | 0        | The version and language are neutral.                                           |
| Testdb  | (Null)   | The companion file with no language associated with it.                         |
| Testdb  | 1033     | The companion file and language.                                                |
| (Null)  | 1033     | No version, but has a language associated with it (that is, typelib, helpfile). |



 

For more information, see the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) and [LockPermissions Table](lockpermissions-table.md).

## Validation

<dl>

[ICE02](ice02.md)  
[ICE03](ice03.md)  
[ICE04](ice04.md)  
[ICE06](ice06.md)  
[ICE18](ice18.md)  
[ICE30](ice30.md)  
[ICE32](ice32.md)  
[ICE35](ice35.md)  
[ICE39](ice39.md)  
[ICE42](ice42.md)  
[ICE45](ice45.md)  
[ICE50](ice50.md)  
[ICE51](ice51.md)  
[ICE54](ice54.md)  
[ICE55](ice55.md)  
[ICE57](ice57.md)  
[ICE59](ice59.md)  
[ICE60](ice60.md)  
[ICE67](ice67.md)  
[ICE69](ice69.md)  
[ICE76](ice76.md)  
[ICE91](ice91.md)  
</dl>

 

 




