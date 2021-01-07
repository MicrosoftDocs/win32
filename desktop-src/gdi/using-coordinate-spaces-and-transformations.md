---
description: 'This section contains an example that demonstrates the following tasks:'
ms.assetid: 61db38d7-9371-4ff1-b96b-1bed4c2a2749
title: Using Coordinate Spaces and Transformations
ms.topic: article
ms.date: 05/31/2018
---

# Using Coordinate Spaces and Transformations

This section contains an example that demonstrates the following tasks:

-   Drawing graphics with predefined units.
-   Centering graphics in the application's client area.
-   Scaling graphics output to half its original size.
-   Translating graphics output 3/4 of an inch to the right.
-   Rotating graphics 30 degrees.
-   Shearing graphics output along the x-axis.
-   Reflecting graphics output about an imaginary horizontal axis drawn through its midpoint.

The following example was used to create the illustrations that appear earlier in this overview.


```C++
void TransformAndDraw(int iTransform, HWND hWnd) 
{ 
    HDC hDC; 
    XFORM xForm; 
    RECT rect; 
 
    // Retrieve a DC handle for the application's window.  
 
    hDC = GetDC(hWnd); 
 
    // Set the mapping mode to LOENGLISH. This moves the  
    // client area origin from the upper left corner of the  
    // window to the lower left corner (this also reorients  
    // the y-axis so that drawing operations occur in a true  
    // Cartesian space). It guarantees portability so that  
    // the object drawn retains its dimensions on any display.  

    SetGraphicsMode(hDC, GM_ADVANCED);
    SetMapMode(hDC, MM_LOENGLISH); 
 
    // Set the appropriate world transformation (based on the  
    // user's menu selection).  
 
    switch (iTransform) 
    { 
        case SCALE:        // Scale to 1/2 of the original size.  
            xForm.eM11 = (FLOAT) 0.5; 
            xForm.eM12 = (FLOAT) 0.0; 
            xForm.eM21 = (FLOAT) 0.0; 
            xForm.eM22 = (FLOAT) 0.5; 
            xForm.eDx  = (FLOAT) 0.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
        case TRANSLATE:   // Translate right by 3/4 inch.  
            xForm.eM11 = (FLOAT) 1.0; 
            xForm.eM12 = (FLOAT) 0.0; 
            xForm.eM21 = (FLOAT) 0.0; 
            xForm.eM22 = (FLOAT) 1.0; 
            xForm.eDx  = (FLOAT) 75.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
        case ROTATE:      // Rotate 30 degrees counterclockwise.  
            xForm.eM11 = (FLOAT) 0.8660; 
            xForm.eM12 = (FLOAT) 0.5000; 
            xForm.eM21 = (FLOAT) -0.5000; 
            xForm.eM22 = (FLOAT) 0.8660; 
            xForm.eDx  = (FLOAT) 0.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
        case SHEAR:       // Shear along the x-axis with a  
                          // proportionality constant of 1.0.  
            xForm.eM11 = (FLOAT) 1.0; 
            xForm.eM12 = (FLOAT) 1.0; 
            xForm.eM21 = (FLOAT) 0.0; 
            xForm.eM22 = (FLOAT) 1.0; 
            xForm.eDx  = (FLOAT) 0.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
        case REFLECT:     // Reflect about a horizontal axis.  
            xForm.eM11 = (FLOAT) 1.0; 
            xForm.eM12 = (FLOAT) 0.0; 
            xForm.eM21 = (FLOAT) 0.0; 
            xForm.eM22 = (FLOAT) -1.0; 
            xForm.eDx  = (FLOAT) 0.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
        case NORMAL:      // Set the unity transformation.  
            xForm.eM11 = (FLOAT) 1.0; 
            xForm.eM12 = (FLOAT) 0.0; 
            xForm.eM21 = (FLOAT) 0.0; 
            xForm.eM22 = (FLOAT) 1.0; 
            xForm.eDx  = (FLOAT) 0.0; 
            xForm.eDy  = (FLOAT) 0.0; 
            SetWorldTransform(hDC, &xForm); 
            break; 
 
    } 
 
    // Find the midpoint of the client area.  
 
    GetClientRect(hWnd, (LPRECT) &rect); 
    DPtoLP(hDC, (LPPOINT) &rect, 2); 
 
    // Select a hollow brush.  
 
    SelectObject(hDC, GetStockObject(HOLLOW_BRUSH)); 
 
    // Draw the exterior circle.  
 
    Ellipse(hDC, (rect.right / 2 - 100), (rect.bottom / 2 + 100), 
        (rect.right / 2 + 100), (rect.bottom / 2 - 100)); 
 
    // Draw the interior circle.  
 
    Ellipse(hDC, (rect.right / 2 -94), (rect.bottom / 2 + 94), 
        (rect.right / 2 + 94), (rect.bottom / 2 - 94)); 
 
    // Draw the key.  
 
    Rectangle(hDC, (rect.right / 2 - 13), (rect.bottom / 2 + 113), 
        (rect.right / 2 + 13), (rect.bottom / 2 + 50)); 
    Rectangle(hDC, (rect.right / 2 - 13), (rect.bottom / 2 + 96), 
        (rect.right / 2 + 13), (rect.bottom / 2 + 50)); 
 
    // Draw the horizontal lines.  
 
    MoveToEx(hDC, (rect.right/2 - 150), (rect.bottom / 2 + 0), NULL); 
    LineTo(hDC, (rect.right / 2 - 16), (rect.bottom / 2 + 0)); 
 
    MoveToEx(hDC, (rect.right / 2 - 13), (rect.bottom / 2 + 0), NULL); 
    LineTo(hDC, (rect.right / 2 + 13), (rect.bottom / 2 + 0)); 
 
    MoveToEx(hDC, (rect.right / 2 + 16), (rect.bottom / 2 + 0), NULL); 
    LineTo(hDC, (rect.right / 2 + 150), (rect.bottom / 2 + 0)); 
 
    // Draw the vertical lines.  
 
    MoveToEx(hDC, (rect.right/2 + 0), (rect.bottom / 2 - 150), NULL); 
    LineTo(hDC, (rect.right / 2 + 0), (rect.bottom / 2 - 16)); 
 
    MoveToEx(hDC, (rect.right / 2 + 0), (rect.bottom / 2 - 13), NULL); 
    LineTo(hDC, (rect.right / 2 + 0), (rect.bottom / 2 + 13)); 
 
    MoveToEx(hDC, (rect.right / 2 + 0), (rect.bottom / 2 + 16), NULL); 
    LineTo(hDC, (rect.right / 2 + 0), (rect.bottom / 2 + 150)); 
 
    ReleaseDC(hWnd, hDC); 
} 
```



 

 



