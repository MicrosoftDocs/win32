---
description: A DirectoryList control displays a part of the path that is currently displayed in the PathEdit control. The DirectoryList control displays the folders below the directory currently displayed by the DirectoryCombo control.
ms.assetid: 05e70381-28c0-4568-808e-ff2dee8ff790
title: DirectoryList Control
ms.topic: article
ms.date: 05/31/2018
---

# DirectoryList Control

A DirectoryList control displays a part of the path that is currently displayed in the [PathEdit control](pathedit-control.md). The DirectoryList control displays the folders below the directory currently displayed by the [DirectoryCombo control](directorycombo-control.md).

The PathEdit, DirectoryCombo, and DirectoryList controls are associated with the same string valued property. That property is the path selected by the user. Enter the property's name into the Property column of the [Control table](control-table.md). This property must have an initial value containing at least one volume and one sublevel. Specify the initial value for the property in the Value column of the [Property table](property-table.md).

This control is intended to be used on a [Browse Dialog](browse-dialog.md) together with the [PathEdit](pathedit-control.md) and DirectoryList control.

The DirectoryList control publishes the following ControlEvents.



| ControlEvent                                            | Description                                                       |
|---------------------------------------------------------|-------------------------------------------------------------------|
| [DirectoryListNew](directorylistnew-controlevent.md)   | Creates a new folder and selects the name field for editing.      |
| [IgnoreChange](ignorechange-controlevent.md)           | Highlights, but does not open, a folder in the current directory. |
| [DirectoryListUp](directorylistup-controlevent.md)     | Selects the parent of the present directory.                      |
| [DirectoryListOpen](directorylistopen-controlevent.md) | Selects and highlights a directory.                               |



 

The contents of the Text field of the [Control table](control-table.md) is never displayed by the DirectoryList control. Instead this field specifies the style of text to be displayed by the control and contains a description of the control used by screen review utilities. To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&*style*}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used. The information following this is read by screen review utilities as the description of the control. See [Accessibility](accessibility.md).

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                                               | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IndirectPropertyName](indirectpropertyname-control-attribute.md) |                                  | This is the name of an indirect property associated with the control. If the Indirect attribute bit is set, the control displays or changes the value of the property having this name. If the Indirect attribute bit is set, this name is also the value of the property listed in the Property column of the [Control table](control-table.md).                        |
| [Position](position-control-attribute.md)                         |                                  | Position of the control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                             |
| [PropertyName](propertyname-control-attribute.md)                 |                                  | This is the name of the property associated with this control. If the Indirect attribute bit is not set, the control displays or changes the value of the property having this name. This attribute is specified in the Property column of the [Control table](control-table.md).                                                                                        |
| [PropertyValue](propertyvalue-control-attribute.md)               |                                  | Current value of the property displayed or changed by this control. If the Indirect attribute bit is not set, this is the value of PropertyName. If the Indirect attribute bit is set, this is the value of IndirectPropertyName. If the attribute changes, the control reflects the new value.                                                                           |
| [Text](text-control-attribute.md)                                 |                                  | To display text in screen readers, enter the text into the Text column of the [Control table](control-table.md). See [Accessibility](accessibility.md).                                                                                                                                                                                                                 |
| [Visible](visible-control-attribute.md)                           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md).to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                     |
| [Enabled](enabled-control-attribute.md)                           | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the bit word in the Attributes column of the [Control](control-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                   |
| [Sunken](sunken-control-attribute.md)                             | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                             |
| [Indirect](indirect-control-attribute.md)                         | 0x00000000 0x00000008<br/> | The control displays or changes the value of the property in the Property column of the [Control table](control-table.md). The control displays or changes the value of the property that has the Identifier listed in the Property column of the Control table.<br/> Determines if the property associated with this control is referenced indirectly.<br/> |
| [RTLRO](rtlro-control-attribute.md)                               | 0x00000000 0x00000020<br/> | Text in the control is displayed in left-to-right reading order. Text in the control is displayed in right-to-left reading order.<br/>                                                                                                                                                                                                                              |
| [RightAligned](rightaligned-control-attribute.md)                 | 0x00000000 0x00000040<br/> | Text in the control is aligned to the left. Text in the control is aligned to the right.<br/>                                                                                                                                                                                                                                                                       |
| [LeftScroll](leftscroll-control-attribute.md)                     | 0x00000000 0x00000080<br/> | The scroll bar is located on the right side of the control. The scroll bar is located on the left side of the control.<br/>                                                                                                                                                                                                                                         |
| [BiDi Control](bidi-control-attribute.md)                         | 0x000000E0                       | Set this value for a combination of the [RTLRO](rtlro-control-attribute.md), [RightAligned](rightaligned-control-attribute.md), and [LeftScroll](leftscroll-control-attribute.md) attributes.                                                                                                                                                                          |



 

## Remarks

This control can be created from the WC\_LISTVIEW class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **LVS\_LIST**, **LVS\_EDITLABELS**, **WS\_VSCROLL**, **LVS\_SHAREIMAGELISTS**, **LVS\_AUTOARRANGE**, **LVS\_SINGLESEL**, **WS\_BORDER**, **LVS\_SORTASCENDING**, **WS\_CHILD**, **WS\_GROUP**, and **WS\_TABSTOP** styles.

This control lets the user select a subfolder of the current selection. With additional buttons it also lets the user select a new folder in the current selection or step up one level in the path. If the user chooses the **Create New Folder** button in a folder where a new folder already exists, a second new folder is not created and the existing new folder's name is selected for editing.

 

