---
title: Obtaining the Address of a Virtual Function Table
description: Obtaining the Address of a Virtual Function Table
ms.assetid: c9e9e2df-75e6-4684-a465-6905e76b10a2
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Obtaining the Address of a Virtual Function Table

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In an application written in the C programming language, you can retrieve the address of the **IAVIStreamVtbl** structure by using the NewBall function. This function returns the address of a structure containing a pointer to **IAVIStreamVtbl**. Information following the **IAVIStreamVtbl** pointer specifies data used internally by AVIBall. Your stream handler can append its own information after the **IAVIStreamVtbl** pointer. This information is returned in subsequent calls to your stream handler.


```C++
PAVISTREAM WINAPI NewBall(VOID) 
{ 
    PAVIBALL pball; 
    pball = (PAVIBALL) GlobalAllocPtr(GHND, sizeof(AVIBALL)); 
    if (!pball) 
        return 0; 
    pball->lpvtbl = &AVIBallHandler; 
    pball->lpvtbl->Create((PAVISTREAM) pball, 0, 0); 
    return (PAVISTREAM) pball; 
} 
```



 

 




