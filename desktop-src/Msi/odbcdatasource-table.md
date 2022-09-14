---
description: The ODBCDataSource table lists the data sources belonging to the installation.
ms.assetid: dea28324-e48d-49e8-a4d2-309f7e7cb4b0
title: ODBCDataSource Table
ms.topic: article
ms.date: 05/31/2018
---

# ODBCDataSource Table

The ODBCDataSource table lists the data sources belonging to the installation.

The ODBCDataSource table has the following columns.



| Column            | Type                         | Key | Nullable |
|-------------------|------------------------------|-----|----------|
| DataSource        | [Identifier](identifier.md) | Y   | N        |
| Component\_       | [Identifier](identifier.md) | N   | N        |
| Description       | [Text](text.md)             | N   | N        |
| DriverDescription | [Text](text.md)             | N   | N        |
| Registration      | [Integer](integer.md)       | N   | N        |



 

## Columns

<dl> <dt>

<span id="DataSource"></span><span id="datasource"></span><span id="DATASOURCE"></span>DataSource
</dt> <dd>

Internal token name for data source. A primary key for the table.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the [Component table](component-table.md).

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The description registered for this data source. This value cannot be localized. ODBC data source descriptions cannot exceed SQL\_MAX\_DSN\_LENGTH.

</dd> <dt>

<span id="DriverDescription"></span><span id="driverdescription"></span><span id="DRIVERDESCRIPTION"></span>DriverDescription
</dt> <dd>

Associated driver which may be pre-existing. This value cannot be localized.

</dd> <dt>

<span id="Registration"></span><span id="registration"></span><span id="REGISTRATION"></span>Registration
</dt> <dd>

This field specifies the type of registration for the data source.



| Constant                                      | Hexadecimal | Decimal | Description                            |
|-----------------------------------------------|-------------|---------|----------------------------------------|
| **msidbODBCDataSourceRegistrationPerMachine** | 0x000       | 0       | Data source is registered per machine. |
| **msidbODBCDataSourceRegistrationPerUser**    | 0x001       | 1       | Data source is registered per user.    |



 

</dd> </dl>

## Remarks

The [InstallODBC](installodbc-action.md) and [RemoveODBC](removeodbc-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE98](ice98.md)  
</dl>

 

 



