---
description: The name of the PatBlt function (an abbreviation for pattern block transfer) implies that this function simply replicates the brush (or pattern) until it fills a specified rectangle.
ms.assetid: 601e1e79-a328-4e63-958a-ca26129e03f8
title: Pattern Block Transfer
ms.topic: article
ms.date: 05/31/2018
---

# Pattern Block Transfer

The name of the [**PatBlt**](/windows/desktop/api/Wingdi/nf-wingdi-patblt) function (an abbreviation for pattern block transfer) implies that this function simply replicates the brush (or pattern) until it fills a specified rectangle. However, the function is actually much more powerful. Before replicating the brush, it combines the color data for the pattern with the color data for the existing pixels on the video display by using a raster operation (ROP). An ROP is a bitwise operation that is applied to the bits of color data for the replicated brush and the bits of color data for the target rectangle on the display device. There are 256 ROPs; however, the **PatBlt** function recognizes only those that require a pattern and a destination (not those that require a source). The following table identifies the most common ROPs.



| ROP       | Description                                                                         |
|-----------|-------------------------------------------------------------------------------------|
| PATCOPY   | Copies the pattern to the destination bitmap.                                       |
| PATINVERT | Combines the destination bitmap with the pattern by using the Boolean XOR operator. |
| DSTINVERT | Inverts the destination bitmap.                                                     |
| BLACKNESS | Turns all output to binary zeros.                                                   |
| WHITENESS | Turns all output to binary ones.                                                    |



 

For more information, see [Raster Operation Codes](raster-operation-codes.md).

 

 



