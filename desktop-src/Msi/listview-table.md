---
description: The lines of a listview are not treated as individual controls, but they are part of a listview that functions as a control. The ListView table defines the values for all listviews.
ms.assetid: 0da4eab9-cabc-4bcc-8267-4aa1cd79e78b
title: ListView Table
ms.topic: article
ms.date: 05/31/2018
---

# ListView Table

The lines of a listview are not treated as individual controls, but they are part of a listview that functions as a control. The ListView table defines the values for all listviews.

The ListView table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Order    | [Integer](integer.md)       | Y   | N        |
| Value    | [Formatted](formatted.md)   | N   | N        |
| Text     | [Formatted](formatted.md)   | N   | Y        |
| Binary\_ | [Identifier](identifier.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

A named property to be tied to this item. All the items tied to the same property become part of the same listview.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

A positive integer used to determine the ordering of the items that appear in a single listview list. The integers do not have to be consecutive. If a listview is defined as ordered, then all the items should have an Ordering value. If the listview is defined as unordered, then this column is ignored.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value string associated with this item. Selecting the line sets the associated property to this value.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

The visible, localizable text to be assigned to the item. If this entry or the entire column is missing, then the text defaults to the corresponding entry in Value.

</dd> <dt>

<span id="Binary_"></span><span id="binary_"></span><span id="BINARY_"></span>Binary\_
</dt> <dd>

The image data for the icon. This is a foreign key to the [Binary table](binary-table.md).

</dd> </dl>

## Remarks

The contents of the Value and Text fields are formatted by the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function when the control is created, therefore they can contain any expression that the MsiFormatRecord function can interpret. The formatting occurs only when the control is created, and it is not updated if a property involved in the expression is modified during the life of the control.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE32](ice32.md)  
</dl>

 

 



