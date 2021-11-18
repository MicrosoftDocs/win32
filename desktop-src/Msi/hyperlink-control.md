---
description: The Hyperlink control displays a HTML link to an address, which opens in the default browser for the computer.
ms.assetid: 06678b10-0915-4649-b917-ec90c40d5160
title: Hyperlink Control
ms.topic: article
ms.date: 05/31/2018
---

# Hyperlink Control

The Hyperlink control displays a HTML link to an address, which opens in the default browser for the computer. Links are not supported for protocols other than HTML.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This Control is available beginning with Windows Installer 5.0.

The Text value of the HyperLink control uses the anchor <a> tag and the HREF attribute value to specify the URL and displayed text of the link.

``` syntax
<a href="https://www.blueyonderairlines.com">Blue Yonder Airlines</a>
```

## Control Attributes

You can use the following attributes with the Hyperlink control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                             | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md)       |                                  | Position of control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                                                                                                                       |
| [Text](text-control-attribute.md)               |                                  | Text displayed by the control. To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&style}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used. The text value will also resolve \[Property\] to the referenced property. <br/> |
| [Visible](visible-control-attribute.md)         | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md).to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                                                                           |
| [Enabled](enabled-control-attribute.md)         | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the bit word in the Attributes column of the [Control](control-table.md) or [BBControl tables](bbcontrol-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                                                                        |
| [Sunken](sunken-control-attribute.md)           | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                                                                                                                                            |
| [Transparent](transparent-control-attribute.md) | 0x00000000 0x00010000<br/> | Opaque control. Background shows through control. The control has the WS\_EX\_TRANSPARENT style.<br/> Include this bit in the Attributes column of the [Control](control-table.md) or [BBControl tables](bbcontrol-table.md).<br/>                                                                                                                                                                                                                                                          |



 

## Remarks

This control can be created from the WC\_LINK class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the WS\_CHILD, WS\_TABSTOP and WS\_GROUP styles.

Do not place transparent [Text controls](text-control.md) on top of colored bitmaps. The text may not be visible if the user changes the display color scheme. For example, text may become invisible if the user sets the high contrast parameter for accessibility reasons.

If the text in the control is longer than the control width, the text wraps or truncates, depending on whether the height is sufficient to fit the wrapped text.

 

 
