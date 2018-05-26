---
Description: The following functions are used with color.
ms.assetid: 9dd32d4a-30bd-406f-a934-bb71ad4ca2cb
title: Color Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Color Functions

The following functions are used with color.



| Function                                                   | Description                                                                                                                                           |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AnimatePalette**](/windows/win32/Wingdi/nf-wingdi-animatepalette?branch=master)                   | Replaces entries in the specified logical palette.                                                                                                    |
| [**CreateHalftonePalette**](/windows/win32/Wingdi/nf-wingdi-createhalftonepalette?branch=master)     | Creates a halftone palette for the specified device context (DC).                                                                                     |
| [**CreatePalette**](/windows/win32/Wingdi/nf-wingdi-createpalette?branch=master)                     | Creates a logical palette.                                                                                                                            |
| [**GetColorAdjustment**](/windows/win32/Wingdi/nf-wingdi-getcoloradjustment?branch=master)           | Retrieves the color adjustment values for the specified DC.                                                                                           |
| [**GetNearestColor**](/windows/win32/Wingdi/nf-wingdi-getnearestcolor?branch=master)                 | Retrieves a color value identifying a color from the system palette that will be displayed when the specified color value is used.                    |
| [**GetNearestPaletteIndex**](/windows/win32/Wingdi/nf-wingdi-getnearestpaletteindex?branch=master)   | Retrieves the index for the entry in the specified logical palette most closely matching a specified color value.                                     |
| [**GetPaletteEntries**](/windows/win32/Wingdi/nf-wingdi-getpaletteentries?branch=master)             | Retrieves a specified range of palette entries from the given logical palette.                                                                        |
| [**GetSystemPaletteEntries**](/windows/win32/Wingdi/nf-wingdi-getsystempaletteentries?branch=master) | Retrieves a range of palette entries from the system palette that is associated with the specified DC.                                                |
| [**GetSystemPaletteUse**](/windows/win32/Wingdi/nf-wingdi-getsystempaletteuse?branch=master)         | Retrieves the current state of the system (physical) palette for the specified DC.                                                                    |
| [**RealizePalette**](/windows/win32/Wingdi/nf-wingdi-realizepalette?branch=master)                   | Maps palette entries from the current logical palette to the system palette.                                                                          |
| [**ResizePalette**](/windows/win32/Wingdi/nf-wingdi-resizepalette?branch=master)                     | Increases or decreases the size of a logical palette based on the specified value.                                                                    |
| [**SelectPalette**](/windows/win32/Wingdi/nf-wingdi-selectpalette?branch=master)                     | Selects the specified logical palette into a device context.                                                                                          |
| [**SetColorAdjustment**](/windows/win32/Wingdi/nf-wingdi-setcoloradjustment?branch=master)           | Sets the color adjustment values for a DC using the specified values.                                                                                 |
| [**SetPaletteEntries**](/windows/win32/Wingdi/nf-wingdi-setpaletteentries?branch=master)             | Sets RGB (red, green, blue) color values and flags in a range of entries in a logical palette.                                                        |
| [**SetSystemPaletteUse**](/windows/win32/Wingdi/nf-wingdi-setsystempaletteuse?branch=master)         | Allows an application to specify whether the system palette contains 2 or 20 static colors.                                                           |
| [**UnrealizeObject**](/windows/win32/Wingdi/nf-wingdi-unrealizeobject?branch=master)                 | Resets the origin of a brush or resets a logical palette.                                                                                             |
| [**UpdateColors**](/windows/win32/Wingdi/nf-wingdi-updatecolors?branch=master)                       | Updates the client area of the specified device context by remapping the current colors in the client area to the currently realized logical palette. |



 

 

 



