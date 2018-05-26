---
title: Examining a Device Contexts Current Pixel Format
description: Use the GetPixelFormat and DescribePixelFormat functions to examine a device contexts current pixel format, as shown in the following code fragment.
ms.assetid: 1da8c8e0-9444-421a-9c2e-c196b5a9db36
keywords:
- OpenGL on Windows,pixels
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Examining a Device Contexts Current Pixel Format

Use the [**GetPixelFormat**](/windows/win32/wingdi/nf-wingdi-getpixelformat?branch=master) and [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master) functions to examine a device context's current pixel format, as shown in the following code fragment.


```C++
PIXELFORMATDESCRIPTOR  pfd;
HDC    hdc;
int    iPixelFormat;
 
// if the device context has a current pixel format ...  
if (iPixelFormat = GetPixelFormat(hdc)) { 
 
    // obtain a detailed description of that pixel format  
    DescribePixelFormat(hdc, iPixelFormat, 
                             sizeof(PIXELFORMATDESCRIPTOR), &amp;pfd); 
    }
```



 

 




