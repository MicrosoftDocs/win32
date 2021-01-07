---
description: This attribute is the text string displayed in the control.
ms.assetid: 0c4b7183-a43a-4c91-b01e-9f377500ba38
title: Text Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Text Control Attribute

This attribute is the text string displayed in the control. On setting, if the field 0 of the record is not null, the record is formatted using FormatText. If the field 0 is null, the first field of the record defines the text. On getting the value is always returned in the first field. For some controls this text may not be visible. In Windows the accelerator key for a control is defined by placing a "&" in front of the desired character in this string.

## Valid Controls

All controls except the [Line Control](line-control.md).

## Associated Bit Flags

None.

## Remarks

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



