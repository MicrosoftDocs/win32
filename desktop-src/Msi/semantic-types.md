---
description: The following entries in the Format, Type, and ContextData columns of the ModuleConfiguration table specify the semantic type of information being substituted into the configurable item specified in the Name column of this table.
ms.assetid: f44e234e-b45a-40be-993d-956b8966c321
title: Semantic Types
ms.topic: article
ms.date: 05/31/2018
---

# Semantic Types

The following entries in the Format, Type, and ContextData columns of the [ModuleConfiguration table](moduleconfiguration-table.md) specify the semantic type of information being substituted into the configurable item specified in the Name column of this table.

[Text Format Types](text-format-types.md)



| Format | Type       | ContextData                                                 | Description                                                                                                |
|--------|------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Text   |            |                                                             | Arbitrary text. See [Arbitrary Text Type](arbitrary-text-type.md).                                        |
| Text   | Enum       | <A>=<a>;<B>=<b>;<C>=<c> | Value selected from a set. See [Enum Type](enum-type.md).                                                 |
| Text   | Formatted  |                                                             | Value meeting the definition of Formatted Text in the installer. See [Formatted Type](formatted-type.md). |
| Text   | RTF        |                                                             | An RTF text string. See [RTF Type](rtf-type.md).                                                          |
| Text   | Identifier |                                                             | A text string conforming to a Windows Installer [Identifier](identifier.md).                              |



 

[Integer Format Types](integer-format-types.md)



| Format  | Type | ContextData | Description                                                                  |
|---------|------|-------------|------------------------------------------------------------------------------|
| Integer |      |             | Any integer value. See [Arbitrary Integer Type](arbitrary-integer-type.md). |



 

[Key Format Types](key-format-types.md)



| Format | Type      | ContextData      | Description                                                                                                            |
|--------|-----------|------------------|------------------------------------------------------------------------------------------------------------------------|
| Key    | File      | AssemblyContext  | Enable users to configure foreign keys to Win32 or common language runtime assemblies. See [File Type](file-type.md). |
| Key    | Binary    | Bitmap           | Foreign key to a Binary table row holding a bitmap for use in UI. See [Binary Type](binary-type.md).                  |
| Key    | Binary    | Icon             | Foreign key to a Binary table row holding an Icon for use in UI. See [Binary Type](binary-type.md).                   |
| Key    | Binary    | EXE              | Foreign key to a Binary table row holding a 32bit EXE. See [Binary Type](binary-type.md).                             |
| Key    | Binary    | EXE64            | Foreign key to a Binary table row holding a 32 or 64bit EXE. See [Binary Type](binary-type.md).                       |
| Key    | Icon      | ShortcutIcon     | Foreign key to an Icon table row holding an Icon for use by a shortcut. See [Icon Type](icon-type.md).                |
| Key    | Dialog    | DialogNext       | Foreign key to a Dialog table row. See [Dialog Type](dialog-type.md).                                                 |
| Key    | Dialog    | DialogPrev       | Foreign key to a Dialog table row. See [Dialog Type](dialog-type.md).                                                 |
| Key    | Directory | IsolationDir     | Foreign key to a Directory table row where isolated files belong. See [Directory Type](directory-type.md).            |
| Key    | Directory | ShortcutLocation | Foreign key to a Directory table row where a shortcut should be installed. See [Directory Type](directory-type.md).   |
| Key    | Property  |                  | Foreign key to a property row. See [Property Type](property-type.md).                                                 |
| Key    | Property  | Public           | Foreign key to a property row. See [Property Type](property-type.md).                                                 |
| Key    | Property  | Private          | Foreign key to a property row. See [Property Type](property-type.md).                                                 |



 

[Bitfield Format Types](bitfield-format-types.md)



| Format   | Type | ContextData                                  | Description                                                                                       |
|----------|------|----------------------------------------------|---------------------------------------------------------------------------------------------------|
| Bitfield |      | <mask>;<A>=<a>;<B>=b | Changes a subset of bits in a column. See [Arbitrary Bitfield Type](arbitrary-bitfield-type.md). |



 

 

 



