---
description: If this bit is set on a text control, the occurrence of the character &\#0034;&&\#0034; in a text string is displayed as itself. If this bit is not set, then the character following &\#0034;&&\#0034; in the text string is displayed as an underscored character.
ms.assetid: b958eecb-2f44-420f-8c93-7a4bd8b589da
title: NoPrefix Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# NoPrefix Control Attribute

If this bit is set on a text control, the occurrence of the character "&" in a text string is displayed as itself. If this bit is not set, then the character following "&" in the text string is displayed as an underscored character.

## Valid Controls

[Text](text-control.md)

## Value



| Decimal | Hexadecimal | Constant                           |
|---------|-------------|------------------------------------|
| 131072  | 0x20000     | **msidbControlAttributesNoPrefix** |



 

## Remarks

To set this attribute on a control, include the NoPrefix bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



