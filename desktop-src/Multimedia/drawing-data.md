---
title: Drawing Data
description: Drawing Data
ms.assetid: 'cc4f383d-54d4-4027-ad6a-da19bb07c17f'
keywords: ["video compression manager (VCM),drawing", "VCM (video compression manager),drawing", "ICDraw function", "ICDrawStart macro", "ICDrawStop macro", "ICDrawFlush macro", "ICDrawEnd macro"]
---

# Drawing Data

The following example uses the [**ICDraw**](icdraw.md) function and the [**ICDrawStart**](icdrawstart.md), [**ICDrawStop**](icdrawstop.md), [**ICDrawFlush**](icdrawflush.md), and [**ICDrawEnd**](icdrawend.md) macros to draw data on the screen.


```C++
DWORD    dwNumBuffers; 
 
// Find out how many buffers need filling before drawing starts.

ICGetBuffersWanted(hIC, &amp;dwNumBuffers); 
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



 

 




