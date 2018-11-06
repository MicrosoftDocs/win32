---
title: Preparing to Draw Data
description: Preparing to Draw Data
ms.assetid: 98adcee4-06c0-4684-bd9e-e030e3f9a59d
keywords:
- video compression manager (VCM),drawing
- VCM (video compression manager),drawing
- ICDrawBegin macro
- ICDrawEnd macro
ms.topic: article
ms.date: 05/31/2018
---

# Preparing to Draw Data

The following example shows the initialization sequence that instructs the decompressor to draw full-screen. It uses the [**ICDrawBegin**](/windows/desktop/api/Vfw/nf-vfw-icdrawbegin) and [**ICDrawEnd**](/windows/desktop/api/Vfw/nf-vfw-icdrawend) macros.


```C++
// Assume lpbiIn has the input format, dwRate has the data rate. 

if (ICDrawBegin(hIC, ICDRAW_QUERY | ICDRAW_FULLSCREEN, NULL, NULL, 
    NULL, 0, 0, 0, 0, lpbiIn, 0, 0, 0, 0, dwRate, 
    dwScale) == ICERR_OK) 
{ 
    // Decompressor supports this drawing so set up to draw. 
    ICDrawBegin(hIC, ICDRAW_FULLSCREEN, hPal, NULL, NULL, 0, 0, 0, 
        0, lpbiIn, 0, 0, lbpi->biWidth, lpbi->biHeight, dwRate, 
        dwScale); 
    . 
    . // Start decompressing and drawing frames. 
    . 
 
    // Drawing done. Terminate procedure. 
    ICDrawEnd(hIC); 
} 
else 
{ 
    
    // Use another renderer to draw data on the screen; 
    // ICDraw does not support the format. 
} 
 
```



 

 




