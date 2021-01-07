---
description: This table contains the icon files. Each icon from the table is copied to a file as a part of product advertisement to be used for advertised shortcuts and OLE servers. See OLE Limitations on Streams.
ms.assetid: a59c552a-21c0-4dd4-9146-88a5f9a22962
title: Icon Table
ms.topic: article
ms.date: 05/31/2018
---

# Icon Table

This table contains the icon files. Each icon from the table is copied to a file as a part of product advertisement to be used for advertised shortcuts and OLE servers. See [OLE Limitations on Streams](ole-limitations-on-streams.md).

The Icon table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| Name   | [Identifier](identifier.md) | Y   | N        |
| Data   | [Binary](binary.md)         | N   | N        |



 

## Columns

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

Name of the icon file.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

The binary icon data in PE (.dll or .exe) or icon (.ico) format.

</dd> </dl>

## Remarks

This table is referred to when the [PublishProduct action](publishproduct-action.md) is executed.

The icons for shortcuts, file name extensions, and CLSIDs must be stored in files that are separate from the target file itself. This is required because the installer should copy only the small icon files to the user's machine when advertising the resource. A developer of an installation package therefore needs to author separate files containing only the icons. These icon files are then stored as binary data in the Icon table.

Icon files that are associated strictly with file name extensions or CLSIDs can have any extension, such as .ico. However, Icon files that are associated with shortcuts must be in the EXE binary format and must be named such that their extension matches the extension of the target. The shortcut will not work if this rule is not followed. For example, if a shortcut is to point to a resource having the key file Red.bar, then the icon file must also have the extension .bar. Multiple icons can be stuffed into the same icon file as long as all of the target files have the same extension.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE29](ice29.md)  
[ICE32](ice32.md)  
[ICE36](ice36.md)  
[ICE50](ice50.md)  
</dl>

 

 



