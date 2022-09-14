---
description: The logical value of a property that has been set is True.
ms.assetid: aee818aa-912d-4e59-b061-61cd35993593
title: Using Properties in Conditional Statements
ms.topic: article
ms.date: 05/31/2018
---

# Using Properties in Conditional Statements

The logical value of a property that has been set is True. To determine whether a property is set without actually getting its value, test the logical expression "MyProperty" or "Not MyProperty". When the property MyProperty is set, the former evaluates as True and the latter as False.

One or more properties can be combined with operators to form logical expressions used in a conditional statements. For more information about the operators that can be used in conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

A conditional statement using properties can be entered into the Condition column of the [Condition table](condition-table.md) to modify the selection state of any entry in the [Feature table](feature-table.md).

Conditional statements with one or more properties are commonly used in the Condition column of database tables.

The following tables each have a column for conditional expressions:

-   [Condition table](condition-table.md)
-   [ControlEvent table](controlevent-table.md)
-   [LaunchCondition table](launchcondition-table.md)
-   [InstallUISequence table](installuisequence-table.md)
-   [InstallExecuteSequence table](installexecutesequence-table.md)
-   [ControlCondition table](controlcondition-table.md)
-   [AdminExecuteSequence table](adminexecutesequence-table.md)
-   [AdvtExecuteSequence table](advtexecutesequence-table.md)
-   [AdminUISequence table](adminuisequence-table.md)

Note that the six action sequence tables have fields for a condition. If the conditional expression in this field evaluates to False, the installer skips that action.

If you set a [private property](private-properties.md) in the UI sequence by authoring a custom action in one of the user interface sequence tables, that property is not set in the execution sequence. To set the property in the execution sequence you must also put a custom action in an execution sequence table. Alternatively, you can make the property a [public property](public-properties.md) and include it in the [**SecureCustomProperties**](securecustomproperties.md) property.

For more information, see [Using a Sequence Table](using-a-sequence-table.md) or [Using Properties](using-properties.md).

 

 



