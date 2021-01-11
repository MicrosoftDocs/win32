---
description: The lines of a combo box are not treated as individual controls; they are part of a single combo box that functions as a control. This table lists the values for each combo box.
ms.assetid: 1d3566ac-e95d-48ed-bce4-fb4604d5f762
title: ComboBox Table
ms.topic: article
ms.date: 05/31/2018
---

# ComboBox Table

The lines of a combo box are not treated as individual controls; they are part of a single combo box that functions as a control. This table lists the values for each combo box.

The ComboBox table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Order    | [Integer](integer.md)       | Y   | N        |
| Value    | [Formatted](formatted.md)   | N   | N        |
| Text     | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

A named property to be tied to this item. All the items tied to the same property become part of the same combo box.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

A positive integer used to determine the ordering of the items that appear in a single combo box list. The integers do not have to be consecutive. If a combo box is defined as ordered, then all the items should have an Order value. If the combo box is defined as unordered, then this column is ignored.

Positive numbers only.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value string associated with this item. Selecting this line of the combo box sets the associated property (specified in Property) to this value.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

The visible, localizable text to be assigned to the item. If this entry or the entire column is missing, then the text defaults to the entry in Value.

</dd> </dl>

## Remarks

The contents of the Value and Text fields are formatted by the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function when the control is created, therefore they can contain any expression that the **MsiFormatRecord** function can interpret. The formatting occurs only when the control is created and it is not updated if a property involved in the expression is modified during the life of the control.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE46](ice46.md)  
</dl>

 

 



