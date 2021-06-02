---
description: The LaunchCondition table is used by the LaunchConditions action. It contains a list of conditions that all must be satisfied for the installation to begin.
ms.assetid: 6e550cc7-c479-417e-ab89-882d8fece4e1
title: LaunchCondition Table
ms.topic: article
ms.date: 05/31/2018
---

# LaunchCondition Table

The LaunchCondition table is used by the [LaunchConditions action](launchconditions-action.md). It contains a list of conditions that all must be satisfied for the installation to begin.

The LaunchCondition table has the following columns.



| Column      | Type                       | Key | Nullable |
|-------------|----------------------------|-----|----------|
| Condition   | [Condition](condition.md) | Y   | N        |
| Description | [Formatted](formatted.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

Expression that must evaluate to True for installation to begin.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

Localizable text to display when the condition fails and the installation must be terminated.

</dd> </dl>

## Remarks

You cannot guarantee the order in which the launch conditions are evaluated by authoring this table. If it is necessary to control the order in which conditions are evaluated, you should do this by using Custom Action Type 19 custom actions in your installation.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
[ICE79](ice79.md)  
[ICE86](ice86.md)  
</dl>

 

 



