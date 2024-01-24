---
description: Palette animation is a technique to simulate motion by rapidly changing the colors of selected entries in a color palette.
ms.assetid: fc5b8061-fd4f-4751-883d-877fa32cdfcc
title: Palette Animation
ms.topic: article
ms.date: 05/31/2018
---

# Palette Animation

Palette animation is a technique to simulate motion by rapidly changing the colors of selected entries in a color palette. An application can carry out palette animation by creating a logical palette that contains "reserved" entries and then using the [**AnimatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-animatepalette) function to change colors in those reserved entries.

An application creates a reserved entry in a logical palette by setting the **peFlags** member of the [**PALETTEENTRY**](/previous-versions//dd162769(v=vs.85)) structure to the PC\_RESERVED flag. Once this logical palette is selected and realized, the application can call the [**AnimatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-animatepalette) function to change one or more reserved entries. If the given palette is associated with the active window, the system updates the colors on the screen immediately.

 

 
