---
description: The CheckBox table lists the values for the check boxes.
ms.assetid: 6881f358-74af-4160-ac69-36e848865ac0
title: CheckBox Table
ms.topic: article
ms.date: 05/31/2018
---

# CheckBox Table

The CheckBox table lists the values for the check boxes.

The CheckBox table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Value    | [Formatted](formatted.md)   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

A named property to be tied to this item.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value string associated with this item.

</dd> </dl>

## Remarks

If the check box is selected, then the corresponding property is set to the specified value. If there is no value specified or this table does not exist, then the property is set to its original value when the check box is selected. If the original value is null, the property is set to "1".

The contents of the Value column are formatted by the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function when the control is created. Therefore, it can contain any expression that the **MsiFormatRecord** function can interpret. The Value column is formatted only when the control is created, and it is not updated if a property involved in an expression is modified during the life of the control.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
</dl>

 

 



