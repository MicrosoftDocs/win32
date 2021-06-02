---
description: The ODBCTranslator table lists the ODBC translators belonging to the installation.
ms.assetid: fecb7454-29bb-4ddf-b4d5-2e56c20ff2dc
title: ODBCTranslator Table
ms.topic: article
ms.date: 05/31/2018
---

# ODBCTranslator Table

The ODBCTranslator table lists the ODBC translators belonging to the installation.

The ODBCTranslator table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Translator  | [Identifier](identifier.md) | Y   | N        |
| Component\_ | [Identifier](identifier.md) | N   | N        |
| Description | [Text](text.md)             | N   | N        |
| File\_      | [Identifier](identifier.md) | N   | N        |
| File\_Setup | [Identifier](identifier.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Translator"></span><span id="translator"></span><span id="TRANSLATOR"></span>Translator
</dt> <dd>

Internal token name for translator. A primary key for the table.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the Component table.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The description registered for this ODBC driver translator. This value cannot be localized.

</dd> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

The DLL file for the transfer listed in the Translator column. The File\_ column is an external key into the [File table](file-table.md). The filename entered in the Filename column of that File table record must be in the short filename format. The SFN\|LFN syntax cannot be used.

</dd> <dt>

<span id="File_Setup"></span><span id="file_setup"></span><span id="FILE_SETUP"></span>File\_Setup
</dt> <dd>

The setup DLL file for the translator if it is different from the Translator column. The File\_ column is an external key into the [File table](file-table.md). The filename entered in the Filename column of that File table record must be in the short filename format. The SFN\|LFN syntax cannot be used.

</dd> </dl>

## Remarks

The [InstallODBC](installodbc-action.md) and [RemoveODBC](removeodbc-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



