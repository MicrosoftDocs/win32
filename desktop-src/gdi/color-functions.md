---
description: The following functions are used with color.
ms.assetid: 9dd32d4a-30bd-406f-a934-bb71ad4ca2cb
title: Color Functions
ms.topic: article
ms.date: 05/31/2018
---

# Color Functions

The following functions are used with color.



| Function                                                   | Description                                                                                                                                           |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AnimatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-animatepalette)                   | Replaces entries in the specified logical palette.                                                                                                    |
| [**CreateHalftonePalette**](/windows/desktop/api/Wingdi/nf-wingdi-createhalftonepalette)     | Creates a halftone palette for the specified device context (DC).                                                                                     |
| [**CreatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-createpalette)                     | Creates a logical palette.                                                                                                                            |
| [**GetColorAdjustment**](/windows/desktop/api/Wingdi/nf-wingdi-getcoloradjustment)           | Retrieves the color adjustment values for the specified DC.                                                                                           |
| [**GetNearestColor**](/windows/desktop/api/Wingdi/nf-wingdi-getnearestcolor)                 | Retrieves a color value identifying a color from the system palette that will be displayed when the specified color value is used.                    |
| [**GetNearestPaletteIndex**](/windows/desktop/api/Wingdi/nf-wingdi-getnearestpaletteindex)   | Retrieves the index for the entry in the specified logical palette most closely matching a specified color value.                                     |
| [**GetPaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-getpaletteentries)             | Retrieves a specified range of palette entries from the given logical palette.                                                                        |
| [**GetSystemPaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-getsystempaletteentries) | Retrieves a range of palette entries from the system palette that is associated with the specified DC.                                                |
| [**GetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-getsystempaletteuse)         | Retrieves the current state of the system (physical) palette for the specified DC.                                                                    |
| [**RealizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-realizepalette)                   | Maps palette entries from the current logical palette to the system palette.                                                                          |
| [**ResizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-resizepalette)                     | Increases or decreases the size of a logical palette based on the specified value.                                                                    |
| [**SelectPalette**](/windows/desktop/api/Wingdi/nf-wingdi-selectpalette)                     | Selects the specified logical palette into a device context.                                                                                          |
| [**SetColorAdjustment**](/windows/desktop/api/Wingdi/nf-wingdi-setcoloradjustment)           | Sets the color adjustment values for a DC using the specified values.                                                                                 |
| [**SetPaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-setpaletteentries)             | Sets RGB (red, green, blue) color values and flags in a range of entries in a logical palette.                                                        |
| [**SetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-setsystempaletteuse)         | Allows an application to specify whether the system palette contains 2 or 20 static colors.                                                           |
| [**UnrealizeObject**](/windows/desktop/api/Wingdi/nf-wingdi-unrealizeobject)                 | Resets the origin of a brush or resets a logical palette.                                                                                             |
| [**UpdateColors**](/windows/desktop/api/Wingdi/nf-wingdi-updatecolors)                       | Updates the client area of the specified device context by remapping the current colors in the client area to the currently realized logical palette. |



 

 

 



