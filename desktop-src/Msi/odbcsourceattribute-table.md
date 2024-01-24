---
description: The ODBCSourceAttribute table contains information about the attributes of data sources.
ms.assetid: 8ee50fd7-507e-484f-9a16-de5449470562
title: ODBCSourceAttribute Table
ms.topic: article
ms.date: 05/31/2018
---

# ODBCSourceAttribute Table

The ODBCSourceAttribute table contains information about the attributes of data sources.

The ODBCSourceAttribute table has the following columns.



| Column       | Type                         | Key | Nullable |
|--------------|------------------------------|-----|----------|
| DataSource\_ | [Identifier](identifier.md) | Y   | N        |
| Attribute    | [Text](text.md)             | Y   | N        |
| Value        | [Formatted](formatted.md)   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="DataSource_"></span><span id="datasource_"></span><span id="DATASOURCE_"></span>DataSource\_
</dt> <dd>

Internal token name for data source. A primary key for the table.

</dd> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>Attribute
</dt> <dd>

Name of data source attribute. A primary key for the table.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The localizable string value for the attribute.

</dd> </dl>

## Remarks

The [InstallODBC](installodbc-action.md) and [RemoveODBC](removeodbc-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
</dl>

 

 



