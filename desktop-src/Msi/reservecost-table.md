---
description: The ReserveCost table is an optional table that allows the author to reserve an amount of disk space in any directory that depends on the installation state of a component.
ms.assetid: 371e72f1-40a2-4ed2-b0ab-33840075ff47
title: ReserveCost Table
ms.topic: article
ms.date: 05/31/2018
---

# ReserveCost Table

The ReserveCost table is an optional table that allows the author to reserve an amount of disk space in any directory that depends on the installation state of a component.

The ReserveCost table has the following columns.



| Column        | Type                               | Key | Nullable |
|---------------|------------------------------------|-----|----------|
| ReserveKey    | [Identifier](identifier.md)       | Y   | N        |
| Component\_   | [Identifier](identifier.md)       | N   | N        |
| ReserveFolder | [Identifier](identifier.md)       | N   | Y        |
| ReserveLocal  | [DoubleInteger](doubleinteger.md) | N   | N        |
| ReserveSource | [DoubleInteger](doubleinteger.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="ReserveKey"></span><span id="reservekey"></span><span id="RESERVEKEY"></span>ReserveKey
</dt> <dd>

Primary key that uniquely identifies a ReserveCost table entry.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key to column one of the [Component](component-table.md) table. Reserves a specified amount of space if this component is to be installed.

</dd> <dt>

<span id="ReserveFolder"></span><span id="reservefolder"></span><span id="RESERVEFOLDER"></span>ReserveFolder
</dt> <dd>

This column contains the name of a property that is the full path to the destination directory. This property name is typically the name of a directory in the [Directory](directory-table.md) table or the name of a property set obtained using the [Appsearch](appsearch-action.md) action. This adds the amount of disk space specified in ReserveLocal or ReserveSource to the volume cost of the device containing the directory.

</dd> <dt>

<span id="ReserveLocal"></span><span id="reservelocal"></span><span id="RESERVELOCAL"></span>ReserveLocal
</dt> <dd>

The number of bytes of disk space to reserve if the linked component is installed to run locally.

</dd> <dt>

<span id="ReserveSource"></span><span id="reservesource"></span><span id="RESERVESOURCE"></span>ReserveSource
</dt> <dd>

The number of bytes of disk space to reserve if the linked component is installed to run from source.

</dd> </dl>

## Remarks

Reserving cost in this way could be useful for authors who want to ensure that a minimum amount of disk space will be available after the installation is completed. For example, this disk space might be reserved for user documents or for application files (such as index files) that are created only after the application is started following installation.

You can use the ReserveCost table to enable custom actions to specify an approximate cost for any files, registry entries, or other items that the custom action might install. Custom actions that add entries to the ReserveCost table should be sequenced between the [CostInitialize](costinitialize-action.md) and [FileCost](filecost-action.md) actions. This is necessary for the FileCost action to correctly initialize the costing of all components affected by entries in the ReserveCost table.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



