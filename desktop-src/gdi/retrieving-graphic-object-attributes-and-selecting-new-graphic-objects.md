---
title: Retrieve object attributes, select new objects
description: An application can retrieve the attributes for a pen, brush, palette, font, or bitmap by calling the GetCurrentObject and GetObject functions.
ms.assetid: 09d8412f-a67d-48d5-9c04-9233dee43cf9
ms.topic: article
ms.date: 05/31/2018
---

# Retrieve object attributes, select new objects

An application can retrieve the attributes for a pen, brush, palette, font, or bitmap by calling the [**GetCurrentObject**](/windows/desktop/api/Wingdi/nf-wingdi-getcurrentobject) and [**GetObject**](/windows/desktop/api/Wingdi/nf-wingdi-getobject) functions. The **GetCurrentObject** function returns a handle identifying the object currently selected into the DC; the **GetObject** function returns a structure that describes the attributes of the object.

The following example shows how an application can retrieve the current brush attributes and use the retrieved data to determine whether it is necessary to select a new brush.


```C++
    HDC hdc;                     // display DC handle  
    HBRUSH hbrushNew, hbrushOld; // brush handles  
    HBRUSH hbrush;               // brush handle  
    LOGBRUSH lb;                 // logical-brush structure  
 
    // Retrieve a handle identifying the current brush.  
 
    hbrush = GetCurrentObject(hdc, OBJ_BRUSH); 
 
    // Retrieve a LOGBRUSH structure that contains the  
    // current brush attributes.  
 
    GetObject(hbrush, sizeof(LOGBRUSH), &lb); 
 
    // If the current brush is not a solid-black brush,  
    // replace it with the solid-black stock brush.  
 
    if ((lb.lbStyle != BS_SOLID) 
           || (lb.lbColor != 0x000000)) 
    { 
        hbrushNew = GetStockObject(BLACK_BRUSH); 
        hbrushOld = SelectObject(hdc, hbrushNew); 
    } 
 
    // Perform painting operations with the white brush.  
 
 
    // After completing the last painting operation with the new  
    // brush, the application should select the original brush back  
    // into the device context and delete the new brush.  
    // In this example, hbrushNew contains a handle to a stock object.  
    // It is not necessary (but it is not harmful) to call  
    // DeleteObject on a stock object. If hbrushNew contained a handle  
    // to a brush created by a function such as CreateBrushIndirect,  
    // it would be necessary to call DeleteObject.  
 
    SelectObject(hdc, hbrushOld); 
    DeleteObject(hbrushNew); 
```



> [!Note]
>
> The application saved the original brush handle when calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function the first time. This handle is saved so that the original brush can be selected back into the DC after the last painting operation has been completed with the new brush. After the original brush is selected back into the DC, the new brush is deleted, freeing memory in the GDI heap.

 

 

 



