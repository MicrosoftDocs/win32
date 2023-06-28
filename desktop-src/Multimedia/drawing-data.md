---
title: Drawing Data
description: Drawing Data
ms.assetid: cc4f383d-54d4-4027-ad6a-da19bb07c17f
keywords:
- video compression manager (VCM),drawing
- VCM (video compression manager),drawing
- ICDraw function
- ICDrawStart macro
- ICDrawStop macro
- ICDrawFlush macro
- ICDrawEnd macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Drawing Data

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The following example uses the [**ICDraw**](/windows/desktop/api/Vfw/nf-vfw-icdraw) function and the [**ICDrawStart**](/windows/desktop/api/Vfw/nf-vfw-icdrawstart), [**ICDrawStop**](/windows/desktop/api/Vfw/nf-vfw-icdrawstop), [**ICDrawFlush**](/windows/desktop/api/Vfw/nf-vfw-icdrawflush), and [**ICDrawEnd**](/windows/desktop/api/Vfw/nf-vfw-icdrawend) macros to draw data on the screen.


```C++
DWORD    dwNumBuffers; 
 
// Find out how many buffers need filling before drawing starts.

ICGetBuffersWanted(hIC, &dwNumBuffers); 
for (dw = 0; dw < dwNumBuffers; dw++)
{ 
    ICDraw(hIC, 0, lpFormat, lpData, cbData, dw); // fill the pipeline
    
    // Point lpFormat and lpData to next format and buffer.
    
} 
ICDrawStart(hIC);  // starts the clock 
dw = 0; 
while (fPlaying) 
{ 
    ICDraw(hIC, 0, lpFormat, lpData, chData, dw); // fill more buffers 
    
    // Point lpFormat and lpData to next format and buffer,
    // update dw.
} 
 
ICDrawStop(hIC);   // stops drawing and decompressing when done 
ICDrawFlush(hIC);  // flushes any existing buffers 
ICDrawEnd(hIC);    // ends decompression 
 
```



 

 




