---
description: If the Visible Control bit is set, the control is visible on the dialog box. If this bit is not set, the control is hidden on the dialog box. The visible or hidden state of the Visible control attribute can be later changed by a Control Event.
ms.assetid: 77d3164c-ea8a-4dcf-afd5-02bb2c2568c6
title: Visible Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Visible Control Attribute

If the Visible Control bit is set, the control is visible on the dialog box. If this bit is not set, the control is hidden on the dialog box. The visible or hidden state of the Visible control attribute can be later changed by a [Control Event](control-events.md).

## Valid Controls

All controls.

## Value



| Decimal | Hexadecimal | Constant                          |
|---------|-------------|-----------------------------------|
| 1       | 0x00000001  | **msidbControlAttributesVisible** |



 

## Remarks

You can use the [ControlCondition table](controlcondition-table.md) to show or hide a control according to the value of a property or conditional statement. You can also show or hide a control by subscribing the control to a [ControlEvent](control-events.md). Enter the attribute's identifier in the Attribute column and the event's identifier in the Event column of the [EventMapping table](eventmapping-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



