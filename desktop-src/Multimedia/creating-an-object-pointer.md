---
title: Creating an Object Pointer
description: Creating an Object Pointer
ms.assetid: b66a2725-6ba1-4aea-b165-fe3f4da00375
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating an Object Pointer

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




