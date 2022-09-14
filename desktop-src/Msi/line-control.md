---
description: The Line control is a horizontal line.
ms.assetid: 8b180b71-1e80-47c0-bb44-d5fcecabaed2
title: Line Control
ms.topic: article
ms.date: 05/31/2018
---

# Line Control

The Line control is a horizontal line.

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                       | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Position](position-control-attribute.md) |                                  | Position of the control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                         |
| [Visible](visible-control-attribute.md)   | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) or [BBControl table](bbcontrol-table.md) to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/> |
| [Sunken](sunken-control-attribute.md)     | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                                   |



 

## Remarks

This control can be created from the STATIC class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **SS\_ETCHEDHORZ** and **SS\_SUNKEN** styles.

 

 
