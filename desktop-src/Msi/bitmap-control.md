---
description: The Bitmap control displays a bitmap or JPEG static picture file. The Windows Installer will automatically determine the format of the binary data and display the picture. The control does not support animation.
ms.assetid: 4b511d8a-1819-4a9b-a942-dc32fade75c6
title: Bitmap Control
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Control

The Bitmap control displays a bitmap or JPEG static picture file. The Windows Installer will automatically determine the format of the binary data and display the picture. The control does not support animation.

**Windows 8 and Windows Server 2012:** The image file can be in any standard format supported by the Windows Imaging Component (WIC), including TIFF, JPEG, PNG, GIF, BMP, and HDPhoto. The control does not support animation.

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                                 | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md)           |                                  | Position of the control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                         |
| [Text](text-control-attribute.md)                   |                                  | Contains the name of a bitmap stored in the [Binary table](binary-table.md). To display a bitmap stored in the Binary table, do the following. Enter the name of the bitmap image appearing in the Name column of the Binary table into the Text column of the [Control table](control-table.md) record for this control. <br/>                                         |
| [Visible](visible-control-attribute.md)             | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md).to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/> |
| [Sunken](sunken-control-attribute.md)               | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                   |
| [FixedSize control](fixedsize-control-attribute.md) | 0x00000000 0x00100000<br/> | Stretches the bitmap image to fit the control. Crops or centers the bitmap image in the control.<br/> Include this bit in the bit word of the Attributes column of the [BBControl table](bbcontrol-table.md) or the [Control table](control-table.md).<br/>                                                                                                       |



 

## Remarks

This control can be created from the STATIC class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **SS\_BITMAP**, **SS\_CENTERIMAGE**, **WS\_CHILD**, and **WS\_GROUP** styles.

 

