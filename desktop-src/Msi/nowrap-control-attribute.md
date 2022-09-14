---
description: If this bit is set the text in the control is displayed on a single line. If the text extends beyond the control's margins it is truncated and an ellipsis (&\#0034;...&\#0034;) is inserted at the end to indicate the truncation. If this bit is not set, text wraps.
ms.assetid: 0dec3d25-0da7-4054-8d5c-55e81be16489
title: NoWrap Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# NoWrap Control Attribute

If this bit is set the text in the control is displayed on a single line. If the text extends beyond the control's margins it is truncated and an ellipsis ("...") is inserted at the end to indicate the truncation. If this bit is not set, text wraps.

## Valid Controls

[Text](text-control.md)

## Value



| Decimal | Hexadecimal | Constant                         |
|---------|-------------|----------------------------------|
| 262144  | 0x00040000  | **msidbControlAttributesNoWrap** |



 

## Remarks

To set this attribute on a control, include the NoWrap bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



