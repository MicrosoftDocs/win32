---
description: The ODBCDriver table lists the ODBC drivers belonging to the installation.
ms.assetid: 3518b370-0652-4b54-8057-9871365d5e8c
title: ODBCDriver Table
ms.topic: article
ms.date: 05/31/2018
---

# ODBCDriver Table

The ODBCDriver table lists the ODBC drivers belonging to the installation.

The ODBCDriver table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Driver      | [Identifier](identifier.md) | Y   | N        |
| Component\_ | [Identifier](identifier.md) | N   | N        |
| Description | [Text](text.md)             | N   | N        |
| File\_      | [Identifier](identifier.md) | N   | N        |
| File\_Setup | [Identifier](identifier.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Driver"></span><span id="driver"></span><span id="DRIVER"></span>Driver
</dt> <dd>

Internal token name for driver. A primary key for the table

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the Component table.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The description registered for this ODBC driver. This value cannot be localized.

</dd> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

The DLL file for drivers listed in the Driver column. The File\_ column is an external key into the [File table](file-table.md). The filename entered in the Filename column of that File table record must be in the short filename format. The SFN\|LFN syntax cannot be used.

</dd> <dt>

<span id="File_Setup"></span><span id="file_setup"></span><span id="FILE_SETUP"></span>File\_Setup
</dt> <dd>

The setup DLL file for the driver if it is different than from Driver. The File\_ column is an external key into the [File table](file-table.md). The filename entered in the Filename column of that File table record must be in the short filename format. The SFN\|LFN syntax cannot be used.

</dd> </dl>

## Remarks

The [InstallODBC](installodbc-action.md) and [RemoveODBC](removeodbc-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



