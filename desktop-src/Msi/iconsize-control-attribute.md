---
description: An icon file can hold several different sizes of the same icon image.
ms.assetid: 2d4d3689-a45a-4088-b466-e2b3bf4c8fb5
title: IconSize Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# IconSize Control Attribute

An icon file can hold several different sizes of the same icon image. These bits specify which size of the icon image to load. If none of the bits are set, the first image is loaded. If only **msidbControlAttributesIconSize16** is set, the first 16x16 image is loaded. If only the **msidbControlAttributesIconSize32** is set, the first 32x32 image is loaded. If **msidbControlAttributesIconSize48** is set, the first 48x48 image is loaded.

## Valid Controls

[CheckBox](checkbox-control.md)

[Icon](icon-control.md)

[PushButton](pushbutton-control.md)

[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Description                          |
|---------|-------------|--------------------------------------|
| 2097152 | 0x00200000  | **msidbControlAttributesIconSize16** |
| 4194304 | 0x00400000  | **msidbControlAttributesIconSize32** |
| 6291456 | 0x00600000  | **msidbControlAttributesIconSize48** |



 

## Remarks

To set this attribute on a control, include the IconSize bits in the Attributes column of the control's record in the [Control table](control-table.md).

If the [FixedSize](fixedsize-control-attribute.md) bit is not set, the loaded image is shrunk or stretched to fit the icon control. If the [FixedSize](fixedsize-control-attribute.md) bit is set, and the loaded image is smaller than the icon control, the picture is displayed centered inside the control. If the [FixedSize](fixedsize-control-attribute.md) bit is set, and the loaded image is larger than the icon control, the picture is reduced to fit the control.

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



