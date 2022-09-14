---
description: A color palette is an array that contains color values identifying the colors that can currently be displayed or drawn on the output device.
ms.assetid: 260c5924-d082-4ed2-a8ed-b8a3ad1ca1a9
title: Color Palettes (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Color Palettes (Windows GDI)

A color palette is an array that contains color values identifying the colors that can currently be displayed or drawn on the output device. Color palettes are used by devices that are capable of generating many colors but that can only display or draw a subset of these at any given time. For such devices, the system maintains a *system palette* to track and manage the current colors of the device. Applications do not have direct access to the system palette. Instead, the system associates a default palette with each device context. Applications can use the colors in the default palette or define their own colors by creating *logical palettes* and associating them with individual device contexts.

An application can determine whether a device supports color palettes by checking for the RC\_PALETTE bit in the RASTERCAPS value returned by the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function.

 

 



