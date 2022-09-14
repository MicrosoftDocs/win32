---
description: The BBControl table lists the controls to be displayed on each billboard.
ms.assetid: 2ab31a32-6d33-46b7-a295-199560efa7fb
title: BBControl Table
ms.topic: article
ms.date: 05/31/2018
---

# BBControl Table

The BBControl table lists the controls to be displayed on each billboard.

The BBControl table has the following columns.



| Column      | Type                               | Key | Nullable |
|-------------|------------------------------------|-----|----------|
| Billboard\_ | [Identifier](identifier.md)       | Y   | N        |
| BBControl   | [Identifier](identifier.md)       | Y   | N        |
| Type        | [Identifier](identifier.md)       | N   | N        |
| X           | [Integer](integer.md)             | N   | N        |
| Y           | [Integer](integer.md)             | N   | N        |
| Width       | [Integer](integer.md)             | N   | N        |
| Height      | [Integer](integer.md)             | N   | N        |
| Attributes  | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Text        | [Text](text.md)                   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Billboard_"></span><span id="billboard_"></span><span id="BILLBOARD_"></span>Billboard\_
</dt> <dd>

Name of the billboard.

External key to column one of the [Billboard table](billboard-table.md).

</dd> <dt>

<span id="BBControl"></span><span id="bbcontrol"></span><span id="BBCONTROL"></span>BBControl
</dt> <dd>

Name of the control. This name must be unique within a billboard but can be repeated on different billboards. This column combined with the Billboard\_ column forms the primary key to the table.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

The type of the control. Only static controls, such as a [Text](text-control.md), [Bitmap](bitmap-control.md), [Icon](icon-control.md), or custom control can be placed on a billboard. For a complete list of controls, see the [Controls](controls.md) section.

</dd> <dt>

<span id="X"></span><span id="x"></span>X
</dt> <dd>

Horizontal coordinate of the upper-left corner of the rectangular boundary of the control. The units are [installer units](installer-units.md). This coordinate is measured relative to the billboard control and not relative to the dialog. Use only non-negative numbers.

</dd> <dt>

<span id="Y"></span><span id="y"></span>Y
</dt> <dd>

Vertical coordinate of the upper-left corner of the rectangular boundary of the control. The units are [installer units](installer-units.md). This coordinate is measured relative to the billboard control and not relative to the dialog. This number must be non-negative.

</dd> <dt>

<span id="Width"></span><span id="width"></span><span id="WIDTH"></span>Width
</dt> <dd>

Width of the rectangular boundary of the control. The units are [installer units](installer-units.md). This number must be non-negative.

</dd> <dt>

<span id="Height"></span><span id="height"></span><span id="HEIGHT"></span>Height
</dt> <dd>

Height of the rectangular boundary of the control. The units are [installer units](installer-units.md). This number must be non-negative.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

A 32-bit word specifying the attribute flags to be applied to this control. This number must be non-negative and specify an attribute for a static control that is valid for placement on a billboard. For information on the numeric values to enter into this field, see the particular attribute under [Control Attributes](control-attributes.md).

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

This column contains a localizable string used to set the initial text in the control if the control displays text. The string is truncated if the text is too long to fit on the control. This column contains a key into the [Binary table](binary-table.md) if the control is a push button or a check box containing an icon or bitmap. It is not possible to show both text and a picture on the same button. This column may be left blank.

</dd> </dl>

## Remarks

The integer values for x, y, width, and height are in the [installer units](installer-units.md), not dialog units. An installer unit is equal to one-twelfth the height of the 10-point MS Sans Serif font size. Coordinates for the controls are relative to the billboard control not the dialog.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE95](ice95.md)  
</dl>

## Related topics

<dl> <dt>

[**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)
</dt> </dl>

 

 



