---
description: The ODBCAttribute table contains information about the attributes of Open Database Connectivity (ODBC) drivers and translators.
ms.assetid: 82fd83d4-22dd-4641-807b-d2b263918e4c
title: ODBCAttribute Table
ms.topic: article
ms.date: 05/31/2018
---

# ODBCAttribute Table

The ODBCAttribute table contains information about the attributes of Open Database Connectivity (ODBC) drivers and translators.

The ODBCAttribute table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Driver\_  | [Identifier](identifier.md) | Y   | N        |
| Attribute | [Text](text.md)             | Y   | N        |
| Value     | [Formatted](formatted.md)   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Driver_"></span><span id="driver_"></span><span id="DRIVER_"></span>Driver\_
</dt> <dd>

Internal token name for a driver. A primary key for the table. A foreign key into the [ODBCDriver table](odbcdriver-table.md).

</dd> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>Attribute
</dt> <dd>

Name of the driver attribute. A primary key for the table.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

Localizable string value for attribute.

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

 

 



