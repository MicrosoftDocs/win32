---
title: Deleting an Object
description: Deleting an Object
ms.assetid: 54ea1e7d-75b5-461f-b0d6-a976c33d66fe
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Deleting an Object

The **Release** method deletes the object when its reference count is zero.


```C++
STDMETHODIMP_(ULONG) CAVIFileCF::Release() 
{ 
    if (!--m_refs) 
    { 
        delete this;   // If O, delete this instance. 
        return 0; 
    } 
    return m_refs; 
} 

```



 

 




