---
description: The Dialog Table contains all the dialogs that appear in the user interface (UI) in both the full and reduced modes.
ms.assetid: 981386dd-4fee-4003-8c62-16933cc5bd14
title: Dialog Table
ms.topic: article
ms.date: 05/31/2018
---

# Dialog Table

The Dialog Table contains all the dialogs that appear in the user interface (UI) in both the full and reduced modes.

The Dialog Table has the following columns.



| Column           | Type                               | Key | Nullable |
|------------------|------------------------------------|-----|----------|
| Dialog           | [Identifier](identifier.md)       | Y   | N        |
| HCentering       | [Integer](integer.md)             | N   | N        |
| VCentering       | [Integer](integer.md)             | N   | N        |
| Width            | [Integer](integer.md)             | N   | N        |
| Height           | [Integer](integer.md)             | N   | N        |
| Attributes       | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Title            | [Formatted](formatted.md)         | N   | Y        |
| Control\_First   | [Identifier](identifier.md)       | N   | N        |
| Control\_Default | [Identifier](identifier.md)       | N   | Y        |
| Control\_Cancel  | [Identifier](identifier.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Dialog"></span><span id="dialog"></span><span id="DIALOG"></span>Dialog
</dt> <dd>

The primary key and name of the dialog box.

</dd> <dt>

<span id="HCentering"></span><span id="hcentering"></span><span id="HCENTERING"></span>HCentering
</dt> <dd>

The horizontal position of the dialog box.

The range is 0 to 100, with 0 at the left edge of the screen and 100 at the right edge.

</dd> <dt>

<span id="VCentering"></span><span id="vcentering"></span><span id="VCENTERING"></span>VCentering
</dt> <dd>

The vertical position of the dialog box.

The range is 0 to 100, with 0 at the top edge of the screen and 100 at the bottom edge.

</dd> <dt>

<span id="Width"></span><span id="width"></span><span id="WIDTH"></span>Width
</dt> <dd>

The width of the rectangular boundary of the dialog box.

This number must be non-negative.

</dd> <dt>

<span id="Height"></span><span id="height"></span><span id="HEIGHT"></span>Height
</dt> <dd>

The height of the rectangular boundary of the dialog box.

This number must be non-negative.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

A 32-bit word that specifies the attribute flags to be applied to this dialog box.

This number must be non-negative. For more information, see [Dialog Style Bits](dialog-style-bits.md).

</dd> <dt>

<span id="Title"></span><span id="title"></span><span id="TITLE"></span>Title
</dt> <dd>

A localizable text string specifying the title to be displayed in the title bar of the dialog box.

</dd> <dt>

<span id="Control_First"></span><span id="control_first"></span><span id="CONTROL_FIRST"></span>Control\_First
</dt> <dd>

An external key to the second column of the [Control Table](control-table.md).

Combining this field with the Dialog field specifies a unique control in the [Control Table](control-table.md) that takes the focus when the dialog box is opened. Typically, this can be an [Edit Control](edit-control.md), [SelectionTree Control](selectiontree-control.md), or any other control that can take the focus. If the [PushButton Control](pushbutton-control.md) is the only control present on the dialog box that can take the focus, the PushButton entered in the ControlDefault field must also be entered into the Control First field. This column is ignored in an [Error Dialog](error-dialog.md) box.

Because static text cannot take the focus, a [Text Control](text-control.md) that describes an [Edit Control](edit-control.md), [PathEdit Control](pathedit-control.md), [ListView Control](listview-control.md), [ComboBox Control](combobox-control.md) or [VolumeSelectCombo Control](volumeselectcombo-control.md) must be made the first control in the dialog box to ensure compatibility with screen readers.

</dd> <dt>

<span id="Control_Default"></span><span id="control_default"></span><span id="CONTROL_DEFAULT"></span>Control\_Default
</dt> <dd>

An external key to the second column of the [Control Table](control-table.md).

Combining this field with the Dialog field specifies the default control that takes focus when the dialog box is opened. Typically, this can be a [PushButton Control](pushbutton-control.md). If no PushButton Control on the dialog box has the focus, the Return key is equivalent to clicking on the default control. If this column is left blank, then there is no default control. This column is ignored in an [Error Dialog](error-dialog.md) box.

</dd> <dt>

<span id="Control_Cancel"></span><span id="control_cancel"></span><span id="CONTROL_CANCEL"></span>Control\_Cancel
</dt> <dd>

An external key to the second column of the [Control Table](control-table.md).

Combining this field with the Dialog field specifies a control that cancels the installation. This control is coupled to events in the [ControlEvent Table](controlevent-table.md) used to cancel the installation. Hitting the ESC key or clicking the Close button is equivalent to clicking on the cancel control. This column is ignored in an [Error Dialog](error-dialog.md)

box.

The cancel control is hidden during rollback or the removal of backed up files. The internal UI handler hides the control upon receiving a INSTALLMESSAGE\_COMMONDATA message.

</dd> </dl>

## Remarks

The integer values for width and height are in the [Installer Units](installer-units.md), not dialog units.

The two centering values are ignored for subsequent dialog boxes in a wizard sequence. Dialog box positions are set by the user or as for the previous dialog box. These dialog box sequences are created by a [NewDialog ControlEvent](newdialog-controlevent.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE13](ice13.md)  
[ICE20](ice20.md)  
[ICE23](ice23.md)  
[ICE27](ice27.md)  
[ICE32](ice32.md)  
[ICE44](ice44.md)  
[ICE45](ice45.md)  
[ICE46](ice46.md)  
</dl>

 

 



