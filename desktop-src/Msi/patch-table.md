---
description: The Patch table specifies the file that is to receive a particular patch and the physical location of the patch files on the media images.
ms.assetid: 1b624702-de25-4b1a-9dac-21f359ee97f7
title: Patch Table
ms.topic: article
ms.date: 05/31/2018
---

# Patch Table

The Patch table specifies the file that is to receive a particular patch and the physical location of the patch files on the media images.

The Patch table has the following columns.



| Column      | Type                               | Key | Nullable |
|-------------|------------------------------------|-----|----------|
| File\_      | [Identifier](identifier.md)       | Y   | N        |
| Sequence    | [Integer](integer.md)             | Y   | N        |
| PatchSize   | [DoubleInteger](doubleinteger.md) | N   | N        |
| Attributes  | [Integer](integer.md)             | N   | N        |
| Header      | [Binary](binary.md)               | N   | Y        |
| StreamRef\_ | [Identifier](identifier.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

The patch is applied to the file specified by the identifier in this column. This is a primary key for the table and it is a foreign key to the [File table](file-table.md).

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

This is the position of the patch file in the sequence order of files on the media images. The sequence order must correspond to the order of the files in the patch package cabinet file. This is a primary key for this table. The maximum limit is 32767 files, to create a Windows Installer package with more files, see [Authoring a Large Package](authoring-a-large-package.md).

</dd> <dt>

<span id="PatchSize"></span><span id="patchsize"></span><span id="PATCHSIZE"></span>PatchSize
</dt> <dd>

This column gives the size of the patch in bytes written as a long integer.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

Integer containing bit flags representing patch attributes. Insert a value of 1 in this column to indicate that the failure to apply this patch is not a fatal error.



| Constant                         | Hexadecimal | Decimal | Description                                                          |
|----------------------------------|-------------|---------|----------------------------------------------------------------------|
| (none)                           | 0x000       | 0       | Failure to apply this patch is a fatal error.                        |
| **msidbPatchAttributesNonVital** | 0x001       | 1       | Indicates that the failure to apply this patch is not a fatal error. |



 

</dd> <dt>

<span id="Header"></span><span id="header"></span><span id="HEADER"></span>Header
</dt> <dd>

This column is the binary stream patch header used for patch validation. This column should be null if the StreamRef\_ column is not null. In this case, the patch header stream is stored in the [MsiPatchHeaders table](msipatchheaders-table.md) to overcome the stream name limitation described in [OLE Limitations on Streams](ole-limitations-on-streams.md).

</dd> <dt>

<span id="StreamRef_"></span><span id="streamref_"></span><span id="STREAMREF_"></span>StreamRef\_
</dt> <dd>

External key into the MsiPatchHeaders table specifying the row that contains the patch header stream.

</dd> </dl>

## Remarks

This table is processed by the [PatchFiles action](patchfiles-action.md). It is usually added to the install package by a transform from a patch package. It is usually not authored directly into an install package.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE29](ice29.md)  
[ICE45](ice45.md)  
</dl>

 

 



