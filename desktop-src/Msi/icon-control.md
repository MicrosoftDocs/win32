---
description: The Icon control displays a static picture of an icon. The background of the image is transparent.
ms.assetid: a2d19093-73d0-4e1f-bf82-21e7334a3f34
title: Icon Control (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Icon Control

The Icon control displays a static picture of an icon. The background of the image is transparent.

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                         | Hexadecimal bit                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md)   |                                                                              | Position of control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| [Text](text-control-attribute.md)           |                                                                              | Contains the name of an icon stored in the [Binary table](binary-table.md). To display an icon that is stored in the Binary table enter the name of the image's record appearing in the Binary table into the Text column of the [Control table](control-table.md) record for this control.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| [Visible](visible-control-attribute.md)     | 0x00000000 0x00000001<br/>                                             | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                                                                                                                                                                                                                                                                                                         |
| [Sunken](sunken-control-attribute.md)       | 0x00000000 0x00000004<br/>                                             | Displays the default visual style. Displays the control with a sunken, 3-D look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [FixedSize](fixedsize-control-attribute.md) | 0x00000000 0x00100000<br/>                                             | Stretches the icon image to fit the control. Crops or centers the icon image in the control.<br/> Include this bit in the bit word of the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [IconSize](iconsize-control-attribute.md)   | 0x00000000 0x00200000<br/> 0x00400000<br/> 0x00600000<br/> | Loads the first image. Loads the first 16x16 image.<br/> Loads the first 32x32 image.<br/> Loads the first 48x48 image.<br/> An icon file can contain different size images of the same icon. Include the value of the appropriate bit word in the Attributes column of the [Control table](control-table.md)<br/> If these bits are not set, the installer ignores the FixedSize attribute and the image is stretched to fit the control rectangle. If both the IconSize bits and the FixedSize bits are set, an image smaller than the control is centered and an image is larger than the control it is shrunk to fit.<br/> |



 

## Remarks

This control can be created from the STATIC class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **SS\_ICON**, **SS\_CENTERIMAGE**, **WS\_CHILD**, and **WS\_GROUP** styles.

 

 
