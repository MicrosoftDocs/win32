---
description: The Billboard control displays commonly used controls that are added and removed from the dialog box by ControlEvents.
ms.assetid: c4c0ed5a-2518-499f-805f-dcbe0b0f9393
title: Billboard Control
ms.topic: article
ms.date: 05/31/2018
---

# Billboard Control

The Billboard control displays commonly used controls that are added and removed from the dialog box by ControlEvents. Only controls that are not associated with a property, such as [Text](text-control.md), [Bitmap](bitmap-control.md), or [Icon](icon-control.md), or custom controls can be placed on a billboard. Billboard controls most typically display progress messages.

## Control Attributes

You can use the following attributes with the Billboard control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                                 | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BillboardName](billboardname-control-attribute.md) |                                  | Name of the current billboard. Enter the billboard's identifier in the Billboard column of the [BBControl table](bbcontrol-table.md).<br/>                                                                                                                                                                            |
| [Position](position-control-attribute.md)           |                                  | Position of control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                |
| [Visible](visible-control-attribute.md)             | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [BBControl table](bbcontrol-table.md) to make the control visible or hidden upon its creation.<br/> Hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/> |
| [Sunken](sunken-control-attribute.md)               | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                               |



 

## Remarks

This control has no window of its own.

Billboard controls that appear in the full user interface are listed in the [Billboard table](billboard-table.md).

Controls that are located on a billboard must be listed in the [BBControl table](bbcontrol-table.md) rather than the [Control table](control-table.md).

 

 




