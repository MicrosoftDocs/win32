---
title: Examining a Device Contexts Current Pixel Format
description: Use the GetPixelFormat and DescribePixelFormat functions to examine a device context's current pixel format, as shown in the following code fragment.
ms.assetid: 1da8c8e0-9444-421a-9c2e-c196b5a9db36
keywords:
- OpenGL on Windows,pixels
ms.topic: article
ms.date: 05/31/2018
---

# Examining a Device Contexts Current Pixel Format

Use the [**GetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-getpixelformat) and [**DescribePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-describepixelformat) functions to examine a device context's current pixel format, as shown in the following code fragment.


```C++
PIXELFORMATDESCRIPTOR  pfd;
HDC    hdc;
int    iPixelFormat;
 
// if the device context has a current pixel format ...  
if (iPixelFormat = GetPixelFormat(hdc)) { 
 
    // obtain a detailed description of that pixel format  
    DescribePixelFormat(hdc, iPixelFormat, 
                             sizeof(PIXELFORMATDESCRIPTOR), &pfd); 
    }
```



 

 




