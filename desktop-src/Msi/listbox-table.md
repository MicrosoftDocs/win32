---
description: The lines of a list box are not treated as individual controls, but they are part of a list box that functions as a control. The ListBox table defines the values for all list boxes.
ms.assetid: 1963adcf-f682-4371-ab44-f91e90105dc0
title: ListBox Table
ms.topic: article
ms.date: 05/31/2018
---

# ListBox Table

The lines of a list box are not treated as individual controls, but they are part of a list box that functions as a control. The ListBox table defines the values for all list boxes.

The ListBox table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Order    | [Integer](integer.md)       | Y   | N        |
| Value    | [Formatted](formatted.md)   | N   | N        |
| Text     | [Formatted](formatted.md)   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

A named property to be tied to this item. All the items tied to the same property become part of the same list box.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

A positive integer used to determine the ordering of the items that appear in a single list box. If the list box is defined as ordered, then all items should have an Order value. The integers do not have to be consecutive. If the list box is defined as unordered, then this column is ignored.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value string associated with this item. Selecting the line sets the associated property to this value.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

The localizable, visible text to be assigned to the item. If this entry or the entire column is missing, the text defaults to the corresponding entry in Value.

</dd> </dl>

## Remarks

The contents of the Value and Text fields are formatted by the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function when the control is created, therefore they can contain any expression that the **MsiFormatRecord** function can interpret. The formatting occurs only when the control is created, and it is not updated if a property involved in the expression is modified during the life of the control.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE20](ice20.md)  
[ICE46](ice46.md)  
</dl>

 

 



