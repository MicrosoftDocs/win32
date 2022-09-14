---
description: The PathEdit control displays an edit field that enables a user to select the end section of a path.
ms.assetid: 074ef4d5-3ac1-4bdb-90c5-9798d89a749f
title: PathEdit Control
ms.topic: article
ms.date: 05/31/2018
---

# PathEdit Control

The PathEdit control displays an edit field that enables a user to select the end section of a path. This control supports entering the selected folder name or the entire path in the edit field. A user can also enter a Universal Naming Convention (UNC) path to a drive that has no drive letter. If the user enters an end segment for the path that is invalid for the present volume, PathEdit control cannot transfer the focus to the next control.

The PathEdit control, [DirectoryCombo](directorycombo-control.md), and [DirectoryList](directorylist-control.md) controls are associated with the same string valued property. That property is the path selected by the user. Enter the property's name into the Property column of the [Control table](control-table.md). This property must have an initial value containing at least a one volume and one sublevel. Specify the initial value for the property in the Value column of the [Property table](property-table.md).

This control is intended to be used on a [Browse Dialog](browse-dialog.md) together with the PathEdit and [DirectoryList](directorylist-control.md) controls.

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                                               | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IndirectPropertyName](indirectpropertyname-control-attribute.md) |                                  | This is the name of an indirect property associated with the control. If the Indirect attribute bit is set, the control displays or changes the value of the property having this name. If the Indirect attribute bit is set, this name is also the value of the property listed in the Property column of the [Control table](control-table.md).                                                                                                                                                                              |
| [Position](position-control-attribute.md)                         |                                  | Position of the control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                                                                                                                                                                                   |
| [PropertyName](propertyname-control-attribute.md)                 |                                  | This is the name of the property associated with this control. If the Indirect attribute bit is not set, the control displays or changes the value of the property having this name. This attribute is specified in the Property column of the [Control table](control-table.md).                                                                                                                                                                                                                                              |
| [PropertyValue](propertyvalue-control-attribute.md)               |                                  | Current value of the property displayed or changed by this control. If the Indirect attribute bit is not set, this is the value of PropertyName. If the Indirect attribute bit is set, this is the value of IndirectPropertyName. If the attribute changes, the control reflects the new value.                                                                                                                                                                                                                                 |
| [Text](text-control-attribute.md)                                 |                                  | To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&style}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used.To specify the number of characters the user can enter, append {n} after any font specifications, where n is a positive integer.<br/> |
| [Visible](visible-control-attribute.md)                           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                                                                                                                                           |
| [Enabled](enabled-control-attribute.md)                           | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the bit word in the Attributes column of the [Control](control-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                                                                                                                                         |
| [Sunken](sunken-control-attribute.md)                             | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                                                                                                                                                                  |
| [Indirect](indirect-control-attribute.md)                         | 0x00000000 0x00000008<br/> | The control displays or changes the value of the property in the Property column of the [Control table](control-table.md). The control displays or changes the value of the property that has the Identifier listed in the Property column of the Control table.<br/> Determines if the property associated with this control is referenced indirectly.<br/>                                                                                                                                                       |
| [RTLRO](rtlro-control-attribute.md)                               | 0x00000000 0x00000020<br/> | Text in the control is displayed in left-to-right reading order. Text in the control is displayed in right-to-left reading order.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| [RightAligned](rightaligned-control-attribute.md)                 | 0x00000000 0x00000040<br/> | Text in the control is aligned to the left. Text in the control is aligned to the right.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Remarks

The PathEdit control is derived from the [Edit](edit-control.md) control.

For compatibility with screen readers, when authoring a dialog box with a PathEdit control as the first active control, you must make the text field belonging to the edit field the first active control in the [Dialog table](dialog-table.md). Since the static text cannot take focus, when the dialog box is created, the edit field will have the focus initially as intended; this ensures that screen readers show the correct information.

 

 




