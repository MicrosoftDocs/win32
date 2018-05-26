---
title: Incrementing the Handler Reference Count
description: Incrementing the Handler Reference Count
ms.assetid: 9e71ce1f-5805-4240-9dcc-7e71fbabfe7e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Incrementing the Handler Reference Count

The **AddRef** method increments the stream-hander or file-handler reference count.


```C++
STDMETHODIMP_(ULONG) CAVIFileCF::AddRef() 
{ 
    return ++m_refs; 
} 

```



 

 




