---
description: The Control table defines the controls that appear on each dialog box.
ms.assetid: 'cbe7acd6-b916-45f3-b694-d2345c5a892a'
title: Control Table
ms.topic: article
ms.date: 05/31/2018
---

# Control Table

The Control table defines the controls that appear on each dialog box.

The Control table has the following columns.



| Column        | Type                               | Key | Nullable |
|---------------|------------------------------------|-----|----------|
| Dialog\_      | [Identifier](identifier.md)       | Y   | N        |
| Control       | [Identifier](identifier.md)       | Y   | N        |
| Type          | [Identifier](identifier.md)       | N   | N        |
| X             | [Integer](integer.md)             | N   | N        |
| Y             | [Integer](integer.md)             | N   | N        |
| Width         | [Integer](integer.md)             | N   | N        |
| Height        | [Integer](integer.md)             | N   | N        |
| Attributes    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Property      | [Identifier](identifier.md)       | N   | Y        |
| Text          | [Formatted](formatted.md)         | N   | Y        |
| Control\_Next | [Identifier](identifier.md)       | N   | Y        |
| Help          | [Text](text.md)                   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Dialog_"></span><span id="dialog_"></span><span id="DIALOG_"></span>Dialog\_
</dt> <dd>

External key to the first column of the [Dialog table](dialog-table.md), the name of the dialog box.

</dd> <dt>

<span id="Control"></span><span id="control"></span><span id="CONTROL"></span>Control
</dt> <dd>

Name of the control. This name must be unique within a dialog box but can be repeated on different dialog boxes. The Control column combined with the Dialog\_ column form the primary key to this table.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

The type of the control. For a list of control types, see [Controls](controls.md).

</dd> <dt>

<span id="X"></span><span id="x"></span>X
</dt> <dd>

Horizontal coordinate of the upper-left corner of the rectangular boundary of the control. This must be a non-negative number. See [Position Control Attribute](position-control-attribute.md).

</dd> <dt>

<span id="Y"></span><span id="y"></span>Y
</dt> <dd>

Vertical coordinate of the upper-left corner of the rectangular boundary of the control. This must be a non-negative number. See [Position Control Attribute](position-control-attribute.md).

</dd> <dt>

<span id="Width"></span><span id="width"></span><span id="WIDTH"></span>Width
</dt> <dd>

Width of the rectangular boundary of the control. This must be a non-negative number. See [Position Control Attribute](position-control-attribute.md).

</dd> <dt>

<span id="Height"></span><span id="height"></span><span id="HEIGHT"></span>Height
</dt> <dd>

Height of the rectangular boundary of the control. This must be a non-negative number. See [Position Control Attribute](position-control-attribute.md).

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

A 32-bit word that specifies the bit flags to be applied to this control. This must be a non-negative number, and the allowed values depend upon the type of control. For a list of all control attributes, and the value to enter in this field, see [Control Attributes](control-attributes.md).

</dd> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

The name of a defined property to be linked to this control. Radio button, list box, and combo box values are tied into a group by being linked to the same property. This column is required for active controls.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

A localizable string used to set the initial text contained in a control. The string can also contain embedded properties. For the syntax of a formatted string containing properties see the [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) function. Specify the size, font, and color of the text by prefixing the text string with {\\style}, where style is a text style authored into the TextStyle column of the [TextStyle table](textstyle-table.md). The text string is truncated if it is too long to fit on to the control. The text string may be blank.

Special authoring of the [Formatted](formatted.md) text string in this field is required if the text is to be displayed by a [Text Control](text-control.md) located on a dialog box having the TrackDiskpace attribute. This is the case specified by the [TrackDiskSpace Dialog Style Bit](trackdiskspace-dialog-style-bit.md) appearing in the Attributes of the [Dialog table](dialog-table.md). In this case, if the Formatted string in the Text column of the Control table begins with "\[" and ends with "\]" then you must add a space at the end of the string. For example, if DlgTextFont is a property that will be set to "{\\DlgFontBold}" the formatted string "\[DlgTextFont\]MyText\[ProductName\] " requires the space at the end after the closing bracket. This extra space is required by the installer to correctly display the text in the Text control.

You can enter a short descriptive text string for the [VolumeCostList](volumecostlist-control.md), [ListView](listview-control.md), [DirectoryList](directorylist-control.md), and the [SelectionTree controls](selectiontree-control.md). This text is not seen by the user but it can be read by screen readers as the description of the control.

See also [Accessibility](accessibility.md).

</dd> <dt>

<span id="Control_Next"></span><span id="control_next"></span><span id="CONTROL_NEXT"></span>Control\_Next
</dt> <dd>

The name of another control on the same dialog box and an external key to the second column of the Control table. If the focus in the dialog box is on the control in the Control column, hitting the tab key moves the focus to the control listed in the Control\_Next column. Therefore this column is used to specify the tab order of the controls on the dialog box. The links between the controls must form a closed cycle. Some controls, such as static text controls, can be left out of the cycle. In this case, this field may be left blank.

See also [Accessibility](accessibility.md).

</dd> <dt>

<span id="Help"></span><span id="help"></span><span id="HELP"></span>Help
</dt> <dd>

Optional, localizable text strings that are used with the Help button. The string is divided into two parts by a separator character (\|). The first part of the string is used as ToolTip text. This text is used by screen readers for controls that contain a picture. The second part of the string is reserved for future use. The separator character is required even if only one of the two kinds of text is present.

</dd> </dl>

## Remarks

The integer values for x, y, width, and height are in the [installer units](installer-units.md), not dialog units. An installer unit is equal to one-twelfth the height of the 10-point MS Sans Serif font size. Coordinates for the controls are relative to the billboard.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE20](ice20.md)  
[ICE23](ice23.md)  
[ICE31](ice31.md)  
[ICE32](ice32.md)  
[ICE34](ice34.md)  
[ICE45](ice45.md)  
[ICE46](ice46.md)  
[ICE95](ice95.md)  
</dl>

 

 



