---
title: Using Structures in WCS 1.0
description: Most of the structures used by WCS 1.0 are very straightforward and require little explanation. They are documented in the WCS 1.0 Reference section entitled Structures.
ms.assetid: 8d3682e2-38fd-4a33-b386-ab0716bb6972
keywords:
- Windows Color System (WCS),structures
- WCS (Windows Color System),structures
- image color management,structures
- color management,structures
- colors,structures
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Using Structures in WCS 1.0

Most of the structures used by WCS 1.0 are very straightforward and require little explanation. They are documented in the WCS 1.0 Reference section entitled [Structures](structures.md).

Exceptions are the [**COLORMATCHSETUPW**](/windows/win32/api/icm/ns-icm-colormatchsetupw) structure used by the [**SetupColorMatchingW**](/windows/win32/api/icm/nf-icm-setupcolormatchingw) function, and the following Windows structures defined in Wingdi.h:

-   [BITMAPV5HEADER](#windows-bitmap-header-structures)
-   [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea)
-   [**CIEXYZ**](/windows/desktop/api/Wingdi/ns-wingdi-tagciexyz)
-   [**CIEXYZTRIPLE**](/windows/desktop/api/Wingdi/ns-wingdi-tagicexyztriple)

The following topics are discussed at greater length:

-   [Windows Bitmap Header Structures](#windows-bitmap-header-structures)
-   [Differences Between V4 and V5 Headers](#differences-between-v4-and-v5-headers)
-   [Bitmap.exe: a Command-Line Utility for Converting Bitmap Headers](#bitmapexe-a-command-line-utility-for-converting-bitmap-headers)

## Windows Bitmap Header Structures

WCS 1.0 allows ICC color profiles to be linked or embedded in device-independent bitmaps (DIBs). This allows DIB colors to be characterized more accurately than was possible using WCS in Windows 95. [BITMAPV5HEADER](/windows/win32/api/wingdi/ns-wingdi-bitmapv5header) , the new bitmap header structure, is defined in Wingdi.h in the release of Windows 98. For development purposes, it is also included in the file Icm.h with this Programmer's Reference. The **BITMAPV5HEADER** structure is as follows:


```C++
typedef struct {
    DWORD        bV5Size;
    LONG         bV5Width;
    LONG         bV5Height;
    WORD         bV5Planes;
    WORD         bV5BitCount;
    DWORD        bV5Compression;
    DWORD        bV5SizeImage;
    LONG         bV5XPelsPerMeter;
    LONG         bV5YPelsPerMeter;
    DWORD        bV5ClrUsed;
    DWORD        bV5ClrImportant;
    DWORD        bV5RedMask;
    DWORD        bV5GreenMask;
    DWORD        bV5BlueMask;
    DWORD        bV5AlphaMask;
    DWORD        bV5CSType;
    CIEXYZTRIPLE bV5Endpoints;
    DWORD        bV5GammaRed;
    DWORD        bV5GammaGreen;
    DWORD        bV5GammaBlue;
    DWORD        bV5Intent;         // Rendering intent for bitmap 
    DWORD        bV5ProfileData;    // Offset to profile data 
    DWORD        bV5ProfileSize;    // Size of embedded profile data 
    DWORD        bV5Reserved;       // Should be zero 
} BITMAPV5HEADER, FAR *LPBITMAPV5HEADER, *PBITMAPV5HEADER;
```



The member **bV5CSType** can have the values PROFILE\_EMBEDDED or PROFILE\_LINKED to specify whether a profile is embedded or linked with the DIB. The member **bV5ProfileData** is the offset in bytes from the beginning of the **BITMAPV5HEADER** structure to the start of the profile data. If the profile is embedded, profile data is the actual profile, and if it is linked, the profile data is the null-terminated file name of the profile. This cannot be a Unicode string. It must be composed exclusively of characters from the Windows character set (code page 1252).

When a DIB is loaded into memory, the profile data (if present) should follow the color table, and **bV5ProfileData** should give the offset of the profile data from the beginning of the **BITMAPV5HEADER** structure. The value of this member will be different now, as the bitmap bits do not follow the color table in memory. Applications should modify the **bV5ProfileData** member after loading the DIB into memory.

For packed DIBs, the profile data should follow the bitmap bits similar to the file format. The **bV5ProfileData** member should still give the offset of the profile data from the beginning of the **BITMAPV5HEADER** structure.

Applications should access the profile data only when **bV5Size** == **sizeof** ( **BITMAPV5HEADER** ) **ANDbV5CSType** is PROFILE\_EMBEDDED or PROFILE\_LINKED.

If a profile is linked, the path of the profile can be any fully qualified name (including a network path) that can be opened using the Win32 **CreateFile** function.

## Differences Between V4 and V5 Headers

In working with the new bitmap structure, it is useful to recognize differences in how **BITMAPV4HEADER** and **BITMAPV5HEADER** structures are set up:



| V4 Header     | Meaning                                                                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **bV4CSType** | LCS\_CALIBRATED\_RGB. This value implies that end points and gammas are given in the appropriate fields. Bogus values cause trouble. |
| **bV4CSType** | LCS\_sRGB. This value implies that the bitmap is in sRGB color space (gammas and endpoints ignored).                                 |
| **bV4CSType** | LCS\_WINDOWS\_COLOR\_SPACE. This value implies that the bitmap is in Windows default color space.                                    |



 



| V5 Header     | Meaning                                                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **bV5CSType** | LCS\_CALIBRATED\_RGB. This value implies that end points and gammas are given in the appropriate fields. Bogus values cause trouble.                         |
| **bV5CSType** | LCS\_sRGB. This value implies that the bitmap is in sRGB color space (gammas and endpoints ignored).                                                         |
| **bV5CSType** | PROFILE\_EMBEDDED. This value implies that **bV5ProfileData** points to a memory buffer that contains the profile to use (gammas and endpoints are ignored). |
| **bV5CSType** | PROFILE\_LINKED. This value implies that **bV5ProfileData** points to the file name of the profile to use (gammas and endpoints are ignored).                |
| **bV5CSType** | LCS\_WINDOWS\_COLOR\_SPACE. This value implies that the bitmap is in Windows default color space.                                                            |



 

In order to convert older bitmaps to and from the new **BITMAPV5HEADER** structure, a command-line conversion utility file named Bitmap.exe is included in the WCS 1.0 Programmer's Reference.

## BitMap.exe: a Command-Line Utility for Converting Bitmap Headers

Bitmap.exe is a command-line utility located in the \\Bin folder under the installation folder that you specified. It modifies the headers of Windows bitmaps, allowing you to convert existing bitmaps from **BITMAPINFOHEADER** and **BITMAPV4HEADER** header structures to the newer **BITMAPV5HEADER** structure and back again. The command-line syntax is as follows:


```C++
BITMAP [/d] [/1|4|5] [/s] [/f] 
filename
```



The command-line switches have the following effects.



| Switch | Meaning                                                                  |
|--------|--------------------------------------------------------------------------|
| /d     | Default values are automatically entered in the converted headers.       |
| /1     | Convert the specified bitmaps to **BITMAPINFOHEADER**                    |
| /4     | Convert the specified bitmaps to **BITMAPV4HEADER**                      |
| /5     | Convert the specified bitmaps to **BITMAPV5HEADER**                      |
| /f     | Forces conversion, even if the bitmap already has the right header       |
| /s     | Converts bitmaps in the specified folder and all subdirectories under it |



 

 

 