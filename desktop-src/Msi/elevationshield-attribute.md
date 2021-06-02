---
description: This attribute adds the User Account Control (UAC) elevation icon (shield icon) to the PushButton control.
ms.assetid: ec52d660-eb83-4f27-b640-ea89156260aa
title: ElevationShield Attribute
ms.topic: article
ms.date: 05/31/2018
---

# ElevationShield Attribute

This attribute adds the [*User Account Control*](u-gly.md) (UAC) elevation icon (shield icon) to the [PushButton control](pushbutton-control.md).

If this bit is set, and the installation is not yet running with [*elevated*](e-gly.md) privileges, the pushbutton control is created using the [*User Account Control*](u-gly.md) (UAC) elevation icon (shield icon).

If this bit is set, and the installation is already running with [*elevated*](e-gly.md) privileges, the pushbutton control is created using the other icon attributes.

If this bit is not set, the pushbutton control is created using the other icon attributes.

## Valid Controls

[PushButton](pushbutton-control.md)

## Value



| Decimal | Hexadecimal | Constant                                  |
|---------|-------------|-------------------------------------------|
| 8388608 | 0x00800000  | **msidbControlAttributesElevationShield** |



 

 

 



