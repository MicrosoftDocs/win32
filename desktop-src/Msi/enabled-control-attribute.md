---
description: This attribute specifies if the given control is enabled or disabled. Most controls appear gray when disabled.
ms.assetid: d84b1b55-34e1-4173-b945-39a809014d55
title: Enabled Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Enabled Control Attribute

This attribute specifies if the given control is enabled or disabled. Most controls appear gray when disabled.

If this bit is set, the control is created as enabled.

If this bit is not set, the control is created as disabled.

## Valid Controls

All controls. The appearance of some controls that are not associated with a property, such as Bitmaps and Icons, are unaffected by setting this attribute.

## Value



| Decimal | Hexadecimal | Constant                          |
|---------|-------------|-----------------------------------|
| 2       | 0x00000002  | **msidbControlAttributesEnabled** |



 

## Remarks

You can also use the [ControlCondition table](controlcondition-table.md) to disable or enable a control according to the value of a property or conditional statement.

You can also enable or disable a control by subscribing the control to a [ControlEvent](control-events.md). Enter the attribute's identifier in the Attribute column and the event's identifier in the Event column of the [EventMapping table](eventmapping-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



