---
description: This section lists the binary raster-operation codes used by the GetROP2 and SetROP2 functions. Raster-operation codes define how GDI combines the bits from the selected pen with the bits in the destination bitmap.
ms.assetid: 9a3a5b5d-b41f-4859-8830-98272983a635
title: Binary Raster Operations
ms.topic: article
ms.date: 05/31/2018
---

# Binary Raster Operations

This section lists the binary raster-operation codes used by the [**GetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-getrop2) and [**SetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-setrop2) functions. Raster-operation codes define how GDI combines the bits from the selected pen with the bits in the destination bitmap.

Each raster-operation code represents a Boolean operation in which the values of the pixels in the selected pen and the destination bitmap are combined. The following are the two operands used in these operations.



| Operand | Meaning            |
|---------|--------------------|
| P       | Selected pen       |
| D       | Destination bitmap |



 

The Boolean operators used in these operations follow.



| Operator | Meaning                    |
|----------|----------------------------|
| a        | Bitwise AND                |
| n        | Bitwise NOT (inverse)      |
| o        | Bitwise OR                 |
| x        | Bitwise exclusive OR (XOR) |



 

All Boolean operations are presented in reverse Polish notation. For example, the following operation replaces the values of the pixels in the destination bitmap with a combination of the pixel values of the pen and the selected brush:


```C++
DPo 
```



Each raster-operation code is a 32-bit integer whose high-order word is a Boolean operation index and whose low-order word is the operation code. The 16-bit operation index is a zero-extended 8-bit value that represents all possible outcomes resulting from the Boolean operation on two parameters (in this case, the pen and destination values). For example, the operation indexes for the DPo and DPan operations are shown in the following list.



| P   | D   | DPo | Dpan |
|-----|-----|-----|------|
| 0   | 0   | 0   | 1    |
| 0   | 1   | 1   | 1    |
| 1   | 0   | 1   | 1    |
| 1   | 1   | 1   | 0    |



 

The following list outlines the drawing modes and the Boolean operations that they represent.



| Raster operation | Boolean operation |
|------------------|-------------------|
| R2\_BLACK        | 0                 |
| R2\_COPYPEN      | P                 |
| R2\_MASKNOTPEN   | DPna              |
| R2\_MASKPEN      | DPa               |
| R2\_MASKPENNOT   | PDna              |
| R2\_MERGENOTPEN  | DPno              |
| R2\_MERGEPEN     | DPo               |
| R2\_MERGEPENNOT  | PDno              |
| R2\_NOP          | D                 |
| R2\_NOT          | Dn                |
| R2\_NOTCOPYPEN   | Pn                |
| R2\_NOTMASKPEN   | DPan              |
| R2\_NOTMERGEPEN  | DPon              |
| R2\_NOTXORPEN    | DPxn              |
| R2\_WHITE        | 1                 |
| R2\_XORPEN       | DPx               |



 

For a monochrome device, GDI maps the value zero to black and the value 1 to white. If an application attempts to draw with a black pen on a white destination by using the available binary raster operations, the following results occur.



| Raster operation | Result             |
|------------------|--------------------|
| R2\_BLACK        | Visible black line |
| R2\_COPYPEN      | Visible black line |
| R2\_MASKNOTPEN   | No visible line    |
| R2\_MASKPEN      | Visible black line |
| R2\_MASKPENNOT   | Visible black line |
| R2\_MERGENOTPEN  | No visible line    |
| R2\_MERGEPEN     | Visible black line |
| R2\_MERGEPENNOT  | Visible black line |
| R2\_NOP          | No visible line    |
| R2\_NOT          | Visible black line |
| R2\_NOTCOPYPEN   | No visible line    |
| R2\_NOTMASKPEN   | No visible line    |
| R2\_NOTMERGEPEN  | Visible black line |
| R2\_NOTXORPEN    | Visible black line |
| R2\_WHITE        | No visible line    |
| R2\_XORPEN       | No visible line    |



 

For a color device, GDI uses RGB values to represent the colors of the pen and the destination. An RGB color value is a long integer that contains a red, a green, and a blue color field, each specifying the intensity of the specified color. Intensities range from 0 through 255. The values are packed in the three low-order bytes of the long integer. The color of a pen is always a solid color, but the color of the destination may be a mixture of any two or three colors. If an application attempts to draw with a white pen on a blue destination by using the available binary raster operations, the following results occur.



| Raster operation | Result                 |
|------------------|------------------------|
| R2\_BLACK        | Visible black line     |
| R2\_COPYPEN      | Visible white line     |
| R2\_MASKNOTPEN   | Visible black line     |
| R2\_MASKPEN      | Invisible blue line    |
| R2\_MASKPENNOT   | Visible red/green line |
| R2\_MERGENOTPEN  | Invisible blue line    |
| R2\_MERGEPEN     | Visible white line     |
| R2\_MERGEPENNOT  | Visible white line     |
| R2\_NOP          | Invisible blue line    |
| R2\_NOT          | Visible red/green line |
| R2\_NOTCOPYPEN   | Visible black line     |
| R2\_NOTMASKPEN   | Visible red/green line |
| R2\_NOTMERGEPEN  | Visible black line     |
| R2\_NOTXORPEN    | Invisible blue line    |
| R2\_WHITE        | Visible white line     |
| R2\_XORPEN       | Visible red/green line |



 

 

 



