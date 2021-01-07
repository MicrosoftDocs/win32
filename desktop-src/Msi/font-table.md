---
description: The Font table contains the information for registering font files with the system.
ms.assetid: 5ddff430-a6f8-473b-8006-ac0124469a99
title: Font Table
ms.topic: article
ms.date: 05/31/2018
---

# Font Table

The Font table contains the information for registering font files with the system.

The Font table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| File\_    | [Identifier](identifier.md) | Y   | N        |
| FontTitle | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

External key into the [File table](file-table.md) entry for the font file. It is recommended that the component containing the font file have the FontsFolder specified in the Directory\_ column of the [Component table](component-table.md).

</dd> <dt>

<span id="FontTitle"></span><span id="fonttitle"></span><span id="FONTTITLE"></span>FontTitle
</dt> <dd>

Font name. It is recommended that you leave this column null for TrueType Fonts and TrueType Collections because the installer can register the font after reading the correct font title from the font file. If the font name is entered, it must be identical to font title from the font file. You must specify a title for fonts that do not have embedded names, such as .fon files.

</dd> </dl>

## Remarks

This table is referred to when the [RegisterFonts action](registerfonts-action.md) or the [UnregisterFonts action](unregisterfonts-action.md) is executed.

If the FontTitle field is left Null, the Font name is read directly from the font file specified. If the font name recorded into the FontTitle field differs from the internal font name recorded in the font file, the font is registered twice by the [RegisterFonts action](registerfonts-action.md).

Font files should not be authored with a language ID, as fonts do not have an embedded language ID resource.Thus the Language column of the [File table](file-table.md) should be left null for font files.

Because the installer does not refcount font files by default, preexisting font files may be removed with their component when uninstalling an application. To ensure that a font file is not removed, authors may set the **msidbComponentAttributesSharedDllRefCount** or **msidbComponentAttributesPermanent** bit flags in the Attributes column of the Component Table\_msi\_Component\_Table for the component containing the font file.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE07](ice07.md)  
[ICE32](ice32.md)  
[ICE51](ice51.md)  
[ICE60](ice60.md)  
</dl>

 

 



