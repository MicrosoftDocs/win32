---
description: The Condition table can be used to modify the selection state of any entry in the Feature table based on a conditional expression.
ms.assetid: 8e2d7c8d-5734-49aa-ad29-16d4d32cccb4
title: Condition Table
ms.topic: article
ms.date: 05/31/2018
---

# Condition Table

The Condition table can be used to modify the selection state of any entry in the [Feature table](feature-table.md) based on a conditional expression.

The Condition table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Feature\_ | [Identifier](identifier.md) | Y   | N        |
| Level     | [Integer](integer.md)       | Y   | N        |
| Condition | [Condition](condition.md)   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

External key into column one of the Feature table.

</dd> <dt>

<span id="Level"></span><span id="level"></span><span id="LEVEL"></span>Level
</dt> <dd>

A conditional install level for the feature in the Feature\_ column of this table. The installer sets the install level of this feature to the level specified in this column if the expression in the Condition column evaluates to TRUE.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

If this conditional expression evaluates to TRUE, then the Level column in the Feature table is set to the conditional install level.

The expression in the Condition column should not contain reference to the installed state of any feature or component. This is because the expressions in the Condition column are evaluated before the installer evaluates the installed states of features and components. Any expression in the Condition table that attempts to check the installed state of a feature or component always evaluates to false.

For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> </dl>

## Remarks

A feature can be permanently disabled by setting the Level column to 0.

The Level may be set based on any conditional statement, such as a test for platform, operating system, or a particular property setting.

Conditions should be carefully chosen so that a feature is not enabled on install and then disabled on uninstall. This will orphan the feature and the product will not be able to be uninstalled.

This table is referred to when the [CostFinalize action](costfinalize-action.md) is executed.

If the [**Preselected**](preselected.md) property has been set to 1, the installer does not evaluate the Condition table. The Condition table affects only the installation of features when none of the following properties have been set:

<dl>

[**ADDLOCAL**](addlocal.md)  
[**REMOVE**](remove.md)  
[**ADDSOURCE**](addsource.md)  
[**ADDDEFAULT**](adddefault.md)  
[**REINSTALL**](reinstall.md)  
[**ADVERTISE**](advertise.md)  
[**COMPADDLOCAL**](compaddlocal.md)  
[**COMPADDSOURCE**](compaddsource.md)  
[**COMPADDDEFAULT**](compadddefault.md)  
[**FILEADDLOCAL**](fileaddlocal.md)  
[**FILEADDSOURCE**](fileaddsource.md)  
[**FILEADDDEFAULT**](fileadddefault.md)  
</dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE79](ice79.md)  
[ICE86](ice86.md)  
</dl>

 

 



