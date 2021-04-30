---
description: CFactoryTemplate::m_lpfnNew member - Pointer to a function that creates an instance of the object.
ms.assetid: 86859bf9-e16a-4494-bf1b-1d8ddbc1c805
title: CFactoryTemplate::m_lpfnNew member (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lpfnNew
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




