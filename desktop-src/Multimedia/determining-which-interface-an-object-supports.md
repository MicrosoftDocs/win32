---
title: Determining Which Interface an Object Supports
description: Determining Which Interface an Object Supports
ms.assetid: cf2aacb7-5315-4907-a49b-3eb3bbfd13d1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining Which Interface an Object Supports

The **QueryInterface** method lets an application query an object to determine which interfaces it supports. The sample application sets the *ppv* pointer to the current interface.


```C++
STDMETHODIMP CAVIFileCF::QueryInterface( 
    const IID FAR&amp; iid, 
    void FAR* FAR* ppv) 
{ 
    if (iid == IID_IUnknown) 
        *ppv = this;                     // set the interface pointer 
                                         // to this instance 
    else if (iid == IID_IClassFactory) 
        *ppv = this;                     // second chance to set the 
                                         // interface pointer to this 
                                         // instance 
    else 
        return ResultFromScode(E_NOINTERFACE); 
    AddRef();  //Increment the reference count 
    return NULL; 
} 

```



 

 




