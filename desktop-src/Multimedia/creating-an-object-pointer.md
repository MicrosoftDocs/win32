---
title: Creating an Object Pointer
description: Creating an Object Pointer
ms.assetid: b66a2725-6ba1-4aea-b165-fe3f4da00375
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Object Pointer

AVIBall uses the following structure as its object pointer. The first member of this structure points to the virtual function table that AVIBall uses to access its functions. Applications can cast this structure to the PAVISTREAM data type. Methods that use the PAVISTREAM data type use only the pointer to the virtual function table. The members following the pointer to the virtual function table are used internally by AVIBall.


```C++
typedef struct 
{ 
    IAVIStreamVtbl FAR * lpvtbl; 
 
    // Ball instance data. 
    ULONG     ulRefCount; 
    DWORD     fccType;  // is this audio/video? 
    int        width;    // size, in pixels, of each frame 
    int        height; 
    int        length;   // length, in frames 
    int        size; 
    COLORREF    color;    // ball color 
} AVIBALL, FAR * PAVIBALL; 

```



 

 




