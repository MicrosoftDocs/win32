---
description: Radio buttons are not treated as individual controls, but they are part of a radio button group that functions as a RadioButtonGroup control. The RadioButton table lists the buttons for all the groups.
ms.assetid: 7f8f278a-a737-4116-9938-2850dbb611fa
title: RadioButton Table
ms.topic: article
ms.date: 05/31/2018
---

# RadioButton Table

Radio buttons are not treated as individual controls, but they are part of a radio button group that functions as a [RadioButtonGroup control](radiobuttongroup-control.md). The RadioButton table lists the buttons for all the groups.

The RadioButton table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Order    | [Integer](integer.md)       | Y   | N        |
| Value    | [Formatted](formatted.md)   | N   | N        |
| X        | [Integer](integer.md)       | N   | N        |
| Y        | [Integer](integer.md)       | N   | N        |
| Width    | [Integer](integer.md)       | N   | N        |
| Height   | [Integer](integer.md)       | N   | N        |
| Text     | [Formatted](formatted.md)   | N   | Y        |
| Help     | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

A named property to be tied to this radio button. All the buttons tied to the same property become part of the same group.

</dd> <dt>

<span id="Order"></span><span id="order"></span><span id="ORDER"></span>Order
</dt> <dd>

A positive integer used to determine the ordering of the items within one list. The integers do not have to be consecutive.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

The value string associated with this button. Selecting the button sets the associated property to this value.

</dd> <dt>

<span id="X"></span><span id="x"></span>X
</dt> <dd>

The horizontal coordinate within the group of the upper-left corner of the bounding rectangle of the radio button. This must be a non-negative number.

</dd> <dt>

<span id="Y"></span><span id="y"></span>Y
</dt> <dd>

The vertical coordinate within the group of the upper-left corner of the bounding rectangle of the radio button. This must be a non-negative number.

</dd> <dt>

<span id="Width"></span><span id="width"></span><span id="WIDTH"></span>Width
</dt> <dd>

The width of the button. This must be a non-negative number.

</dd> <dt>

<span id="Height"></span><span id="height"></span><span id="HEIGHT"></span>Height
</dt> <dd>

The height of the button. This must be a non-negative number.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

The localizable, visible title to be assigned to the radio button. If the text is too long to be fit on the control, then it is truncated. If the button displays an icon or a bitmap, then this column contains the name of the picture, which is a key into the [Binary table](binary-table.md). There is no way to show both a picture and text on a button.

</dd> <dt>

<span id="Help"></span><span id="help"></span><span id="HELP"></span>Help
</dt> <dd>

The Help strings used with the button. The text is optional and is localizable. The string is divided into two parts separated by a character (\|). The first part of the string is used as ToolTip text. This text is shown by screen readers for controls that contain a picture. The second part is used for context-sensitive Help, although context-sensitive help has not yet been implemented. The separator character is required even if only one of the two kinds of text is present.

</dd> </dl>

## Remarks

The integer values for x, y, width, and height are in the [installer units](installer-units.md), not dialog units. An installer unit is equal to one-twelfth the height of the 10-point MS Sans Serif font size. Coordinates for the controls are relative to the billboard.

The coordinates of the buttons are given relative to the group. If the coordinates of the group are changed, then the buttons within the group remain in the same relative position to each other.

The contents of the Value and Text fields are formatted by the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function when the control is created, therefore they can contain any expression that the **MsiFormatRecord** function can interpret. The formatting occurs only when the control is created, and it is not updated if a property involved in the expression is modified during the life of the control.

Every RadioButtonGroup control is associated with a property. The default value for this property must be initialized in the [Property table](property-table.md). Within each RadioButtonGroup specified in the RadioButton table, there may be one radio button that has a value in the Value field that matches the default value for this property. This is the default button for the RadioButtonGroup control. The default button is initially shown as selected in the control.

Note that the user cannot change focus in a dialog box by pressing the TAB key to a RadioButtonGroup Control until one of the buttons in the group has been selected. To make the focus move to this button group by pressing the TAB key, specify one of the buttons as a default button for the group.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE34](ice34.md)  
[ICE46](ice46.md)  
</dl>

 

 



