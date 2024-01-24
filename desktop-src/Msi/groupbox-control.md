---
description: The GroupBox control displays a rectangle, possibly with caption text, that serves to group other controls together on the dialog box.
ms.assetid: e1cdcf71-876f-4115-96a4-95d8a0f61a9b
title: GroupBox Control (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# GroupBox Control

The GroupBox control displays a rectangle, possibly with caption text, that serves to group other controls together on the dialog box.

## Control Attributes

You can use the following attributes with the GroupBox control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                               | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md)         |                                  | Position of control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                                                                         |
| [Text](text-control-attribute.md)                 |                                  | Displays a caption in the upper left corner of the control. To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&style}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used.<br/> |
| [Visible](visible-control-attribute.md)           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md) to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                             |
| [Sunken](sunken-control-attribute.md)             | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                                                                                               |
| [RTLRO](rtlro-control-attribute.md)               | 0x00000000 0x00000020<br/> | Text in the control is displayed in left-to-right reading order. Text in the control is displayed in right-to-left reading order.<br/>                                                                                                                                                                                                                                                                                                                |
| [RightAligned](rightaligned-control-attribute.md) | 0x00000000 0x00000040<br/> | Text in the control is aligned to the left. Text in the control is aligned to the right.<br/>                                                                                                                                                                                                                                                                                                                                                         |



 

## Remarks

This control can be created from the BUTTON class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **BS\_GROUPBOX**, **WS\_CHILD**, and **WS\_GROUP** styles.

There is always a gap between the top of the control's window and the visible frame, even when there is no caption.

 

 
