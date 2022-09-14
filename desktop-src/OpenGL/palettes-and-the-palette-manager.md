---
title: Palettes and the Palette Manager
description: The Windows Palette Manager, which is part of the GDI, specifically targets 8-bit display adapters with a hardware palette of 256 color entries.
ms.assetid: 3bfa5077-37ac-4597-98da-f26ad1c107a1
keywords:
- OpenGL on Windows,palette manager
- OpenGL on Windows,hardware palettes
- palette manager OpenGL
- hardware palettes OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Palettes and the Palette Manager

The Windows Palette Manager, which is part of the GDI, specifically targets 8-bit display adapters with a *hardware palette* of 256 color entries. Pixels on the screen are stored as an 8-bit index into the hardware palette. Each entry in the hardware palette usually defines a 24-bit color (8 each of red, green, and blue).

The Palette Manager maintains a *system palette* that is a copy of the hardware palette. The system palette is divided into two sections: 20 reserved colors and the remaining 236 colors, which you can set using the Palette Manager.

A default 20-color *logical palette* is selected and realized into a device context. You can create and use a new logical palette. To change the system palette, select and realize the logical palette you created.

You'll probably create a logical palette to specify the colors you want displayed in your OpenGL application. Using certain GDI calls, you can temporarily replace most of the system palette with a logical palette. Using a logical palette, you can define pixel colors for the GDI using either the RGBA or the color-index mode. The maximum size of a logical palette is 256 colors for 8-bit devices and 4,096 colors on a true-color device (16, 24, and 32 bits).

For more information on the RGBA and color-index modes, see [RGBA Mode and Windows Palette Management](rgba-mode-and-windows-palette-management.md) and [OpenGL Color Modes and Windows Palette Management](opengl-color-modes-and-windows-palette-management.md).

 

 




