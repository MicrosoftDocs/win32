---
description: The Media table describes the set of disks that make up the source media for the installation.
ms.assetid: f9789f1d-35bf-40d6-9724-d5a160a0d06d
title: Media Table
ms.topic: article
ms.date: 05/31/2018
---

# Media Table

The Media table describes the set of disks that make up the source media for the installation.

The Media table contains the columns shown in the following table.



| Column       | Type                     | Key | Nullable |
|--------------|--------------------------|-----|----------|
| DiskId       | [Integer](integer.md)   | Y   | N        |
| LastSequence | [Integer](integer.md)   | N   | N        |
| DiskPrompt   | [Text](text.md)         | N   | Y        |
| Cabinet      | [Cabinet](cabinet.md)   | N   | Y        |
| VolumeLabel  | [Text](text.md)         | N   | Y        |
| Source       | [Property](property.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="DiskId"></span><span id="diskid"></span><span id="DISKID"></span>DiskId
</dt> <dd>

Determines the sort order for the table. This number must be equal to or greater than 1.

</dd> <dt>

<span id="LastSequence"></span><span id="lastsequence"></span><span id="LASTSEQUENCE"></span>LastSequence
</dt> <dd>

File sequence number for the last file for this media. The numbers in the LastSequence column specify which of the files in the [File](file-table.md) table are found on a particular source disk. Each source disk contains all files with sequence numbers (as shown in the Sequence column of the File table) less than or equal to the value in the LastSequence column, and greater than the LastSequence value of the previous disk (or greater than 0, for the first entry in the Media table). This number must be non-negative; the maximum limit is 32767 files. For more information about creating a Windows Installer package with more files, see [Authoring a Large Package](authoring-a-large-package.md).

</dd> <dt>

<span id="DiskPrompt"></span><span id="diskprompt"></span><span id="DISKPROMPT"></span>DiskPrompt
</dt> <dd>

The disk name, which is usually the visible text printed on the disk. This localizable text is used to prompt the user when this disk needs to be inserted.

</dd> <dt>

<span id="Cabinet"></span><span id="cabinet"></span><span id="CABINET"></span>Cabinet
</dt> <dd>

The name of the cabinet if some or all of the files stored on the media are compressed into a cabinet file. If no cabinets are used, this column must be blank. The name of the cabinet must use the syntax of the [Cabinet](cabinet.md) data type. Windows Installer always requires a valid source to repair files included in embedded cabinet files. When Windows Installer installs a package containing an embedded cabinet file, a copy of the cabinet file can be saved by the system. This copy cannot be used to repair the cabinet file. To conserve disk space, use external cabinet files instead of embedded cabinet files.

</dd> <dt>

<span id="VolumeLabel"></span><span id="volumelabel"></span><span id="VOLUMELABEL"></span>VolumeLabel
</dt> <dd>

The label attributed to the volume. This is the volume label returned by the [**GetVolumeInformation**](/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationa) function. If the [**SourceDir**](sourcedir.md) property refers to a removable (floppy or CD-ROM) volume, then this volume label is used to verify that the proper disk is in the drive before attempting to install files. The entry in this column must match the volume label of the physical media.

</dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>Source
</dt> <dd>

This field is only used by patching and is otherwise left blank. A patch transform can enter a property here that is the location of the cabinet file containing the patch files or any new files added by the patch. A different source needs to be specified for these files because the source of the patch package can be stored separately from the product's source. If the Cabinet field is empty, the installer ignores the value in this column. If this field is empty, the installer uses the value of the [**SourceDir**](sourcedir.md) property as the source of the cabinet.

</dd> </dl>

## Remarks

If the cabinet name is preceded by a number sign (\#), then the files referencing this Media table record are packed in a cabinet file that is stored within the database as a separate stream.

For more information about how to add cabinets to the File tables and Media tables, see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

Windows Installer requires that the .msi file be on the first disk of removable media (CD, DVD or floppy) used for the product's installation.

**Determining the SourceMode**

The [**Word Count Summary**](word-count-summary.md) property determines the source mode for the current install. If this property is set to 2 or 3, a cabinet install is assumed. In this mode, the cabinet files are assumed to exist in the directory indicated by the [**SourceDir**](sourcedir.md) property. If the Source Type value is 0 or 1, all source files are assumed to exist in the tree whose root is indicated by the **SourceDir** property.

Note that this only applies to files in the File table that do not have either the Compressed or Uncompressed bits set in the attributes column. These bits override the value of the [**Word Count Summary**](word-count-summary.md) property when determining if a particular file is compressed or uncompressed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE04](ice04.md)  
[ICE06](ice06.md)  
[ICE35](ice35.md)  
[ICE58](ice58.md)  
[ICE71](ice71.md)  
[ICE81](ice81.md)  
</dl>

 

 
