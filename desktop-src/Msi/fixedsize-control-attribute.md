---
description: If the FixedSize Control bit is set, the picture is cropped or centered in the control without changing its shape or size.
ms.assetid: fb1ef0ba-5183-4708-a47d-26c83584df6c
title: FixedSize Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# FixedSize Control Attribute

If the FixedSize Control bit is set, the picture is cropped or centered in the control without changing its shape or size.

If this bit is not set the picture is stretched to fit the control.

## Valid Controls

[Bitmap](bitmap-control.md)

[CheckBox](checkbox-control.md)

[Icon](icon-control.md)

[PushButton](pushbutton-control.md)

[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Constant                            |
|---------|-------------|-------------------------------------|
| 1048576 | 0x00100000  | **msidbControlAttributesFixedSize** |



 

## Remarks

To set this attribute on a control, include the FixedSize bit in the Attributes column of the control's record in the [Control table](control-table.md).

Setting the FixedSize bit has no effect on a [CheckBox](checkbox-control.md), [PushButton](pushbutton-control.md), or [RadioButtonGroup](radiobuttongroup-control.md) if neither the [Bitmap](bitmap-control-attribute.md) or the [Icon](icon-control-attribute.md) have been set.

Setting the FixedSize bit has no effect on an Icon control, or a PushButton associated with an icon, if the [IconSize](iconsize-control-attribute.md) bits is not set.

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



