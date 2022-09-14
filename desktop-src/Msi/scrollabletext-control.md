---
description: This control displays a long string of text that cannot fit entirely on the page. A common use for this control is displaying the license agreement.
ms.assetid: a49209f3-043c-4360-b1e3-9fa9538c2c9b
title: ScrollableText Control
ms.topic: article
ms.date: 05/31/2018
---

# ScrollableText Control

This control displays a long string of text that cannot fit entirely on the page. A common use for this control is displaying the license agreement.

Note that the string of text used with this control cannot contain an embedded property. To display text with embedded properties use instead the [Text Control](text-control.md).

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                               | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md)         |                                  | Position of control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                            |
| [Text](text-control-attribute.md)                 |                                  | Text displayed by the control. Enter the RTF text string into the Text column of the [Control table](control-table.md).                                                                                                                                                                                                                                                       |
| [Visible](visible-control-attribute.md)           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> To make the control visible or hidden on its creation, include this bit in the bit word of the Attributes column in the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md).<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/> |
| [Enabled](enabled-control-attribute.md)           | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the Attributes column of the [Control](control-table.md) or [BBControl tables](bbcontrol-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition table](controlcondition-table.md).<br/>             |
| [Sunken](sunken-control-attribute.md)             | 0x00000000 0x00000004<br/> | Display the default visual style. Display the control with a sunken, 3D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                    |
| [RTLRO](rtlro-control-attribute.md)               | 0x00000000 0x00000020<br/> | Text in the control is displayed in a left-to-right reading order. Text in the control is displayed in a right-to-left reading order.<br/>                                                                                                                                                                                                                               |
| [RightAligned](rightaligned-control-attribute.md) | 0x00000000 0x00000040<br/> | Text in the control is aligned on the left. Text in the control is aligned on the right.<br/>                                                                                                                                                                                                                                                                            |
| [LeftScroll](leftscroll-control-attribute.md)     | 0x00000000 0x00000080<br/> | The scroll bar is located on the right side of the control. The scroll bar is located on the left side of the control.<br/>                                                                                                                                                                                                                                              |
| [BiDi](bidi-control-attribute.md)                 | 0x000000E0                       | Set this value for a combination of the [RTLRO](rtlro-control-attribute.md), [RightAligned](rightaligned-control-attribute.md), and [LeftScroll](leftscroll-control-attribute.md) attributes.                                                                                                                                                                               |



 

## Remarks

This control can be created from the RICHEDIT class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **ES\_MULTILINE**, **WS\_VSCROLL**, **ES\_READONLY**, **WS\_TABSTOP**, **ES\_AUTOVSCROLL**, **WS\_CHILD**, **WS\_GROUP**, and **ES\_NOOLEDRAGDROP** styles.

 

 
