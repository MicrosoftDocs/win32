---
title: Examining a Devices Supported Pixel Formats
description: The DescribePixelFormat function obtains pixel format data for a device context.
ms.assetid: '1ebeb051-2dc9-4753-a0f3-7d2737b5f7f2'
keywords: ["OpenGL on Windows,pixels"]
---

# Examining a Devices Supported Pixel Formats

The [**DescribePixelFormat**](describepixelformat.md) function obtains pixel format data for a device context. It also returns an integer that is the maximum pixel format index for the device context. The following code sample shows how to use that result to step through and examine the pixel formats supported by a device:


```C++
// local variables  
int                      iMax ; 
PIXELFORMATDESCRIPTOR    pfd; 
int                      iPixelFormat ; 
 
// initialize a pixel format index variable  
iPixelFormat = 1; 
 
// keep obtaining and examining pixel format data...  
do { 
    // try to obtain some pixel format data  
    iMax = DescribePixelFormat(hdc, iPixelFormat, sizeof(pfd), &amp;pfd); 
 
    // if there was some problem with that...   
    if (iMax == 0) 
     
        // return indicating failure  
        return(FALSE); 
     
    // we have successfully obtained pixel format data  
 
    // let's examine the pixel format data...  
    myPixelFormatExaminer (&amp;pfd); 
    }  
 
// ...until we've looked at all the device context's pixel formats  
while (++iPixelFormat <= iMax);
```



 

 




