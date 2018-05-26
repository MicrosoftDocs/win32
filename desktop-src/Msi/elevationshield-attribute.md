---
Description: This attribute adds the User Account Control (UAC) elevation icon (shield icon) to the PushButton control.
ms.assetid: ec52d660-eb83-4f27-b640-ea89156260aa
title: ElevationShield Attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ElevationShield Attribute

This attribute adds the [*User Account Control*](u-gly.md#-msi-user-account-control-gly) (UAC) elevation icon (shield icon) to the [PushButton control](pushbutton-control.md).

If this bit is set, and the installation is not yet running with [*elevated*](e-gly.md#-msi-elevated-gly) privileges, the pushbutton control is created using the [*User Account Control*](u-gly.md#-msi-user-account-control-gly) (UAC) elevation icon (shield icon).

If this bit is set, and the installation is already running with [*elevated*](e-gly.md#-msi-elevated-gly) privileges, the pushbutton control is created using the other icon attributes.

If this bit is not set, the pushbutton control is created using the other icon attributes.

## Valid Controls

[PushButton](pushbutton-control.md)

## Value



| Decimal | Hexadecimal | Constant                                  |
|---------|-------------|-------------------------------------------|
| 8388608 | 0x00800000  | **msidbControlAttributesElevationShield** |



 

 

 



