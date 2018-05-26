---
Description: Pointer to a function that creates an instance of the object.
ms.assetid: 86859bf9-e16a-4494-bf1b-1d8ddbc1c805
title: CFactoryTemplatem\_lpfnNew member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CFactoryTemplate::m\_lpfnNew member

Pointer to a function that creates an instance of the object.

## Syntax


```C++
LPFNNewCOMObject m_lpfnNew;
```



## Remarks

In your DLL, declare a static function that returns a pointer to a new instance of the object. In the factory template, set the **m\_lpfnNew** member variable to the address of this static function.

The function pointer type is [**LPFNNewCOMObject**](lpfnnewcomobject.md).

The following example shows a typical function for **m\_lpfnNew**:


```C++
CUnknown * WINAPI CMyComponent::CreateInstance(LPUNKNOWN pUnk, HRESULT *pHr) 
{
    CMyComponent *pNewObject = 
        new CMyComponent(NAME("My Component"), pUnk, pHr );

    if (pNewObject == NULL)  
    {
        *phr = E_OUTOFMEMORY;
    }
    return pNewObject;
}
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




