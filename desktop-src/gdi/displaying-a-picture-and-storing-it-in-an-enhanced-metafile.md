---
description: This section contains an example demonstrating the creation of a picture and the process of storing the corresponding records in a metafile.
ms.assetid: 8be95fef-93dc-4c9c-a0d3-840918c00e43
title: Displaying a Picture and Storing It in an Enhanced Metafile
ms.topic: article
ms.date: 05/31/2018
---

# Displaying a Picture and Storing It in an Enhanced Metafile

This section contains an example demonstrating the creation of a picture and the process of storing the corresponding records in a metafile. The example draws a picture to the display or stores it in a metafile. If a display device context handle is given, it draws a picture to the screen using various GDI functions. If an enhanced metafile device context is given, it stores the same picture in the enhanced metafile.


```C++
void DrawOrStore(HWND hwnd, HDC hdcMeta, HDC hdcDisplay) 
{ 
 
RECT rect; 
HDC hDC; 
int fnMapModeOld; 
HBRUSH hbrOld; 
 
// Draw it to the display DC or store it in the metafile device context.  
 
if (hdcMeta) 
    hDC = hdcMeta; 
else 
    hDC = hdcDisplay; 
 
// Set the mapping mode in the device context.  
 
fnMapModeOld = SetMapMode(hDC, MM_LOENGLISH); 
 
// Find the midpoint of the client area.  
 
GetClientRect(hwnd, (LPRECT)&rect); 
DPtoLP(hDC, (LPPOINT)&rect, 2); 
 
// Select a gray brush.  
 
hbrOld = SelectObject(hDC, GetStockObject(GRAY_BRUSH)); 
 
// Draw a circle with a one inch radius.  
 
Ellipse(hDC, (rect.right/2 - 100), (rect.bottom/2 + 100), 
       (rect.right/2 + 100), (rect.bottom/2 - 100)); 
 
// Perform additional drawing here.  
 
 
 
// Set the device context back to its original state.  
 
SetMapMode(hDC, fnMapModeOld); 
SelectObject(hDC, hbrOld); 
} 
```



 

 



