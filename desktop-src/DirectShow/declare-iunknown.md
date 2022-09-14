---
description: The DECLARE\_IUNKNOWN macro declares the three methods of the base interface for a new interface.
ms.assetid: 3bf8e830-c923-4c31-8855-88fa08f80422
title: DECLARE_IUNKNOWN (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DECLARE_IUNKNOWN
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DECLARE\_IUNKNOWN

The **DECLARE\_IUNKNOWN** macro declares the three methods of the base interface for a new interface.

**Syntax**

``` syntax
#define DECLARE_IUNKNOWN                                        \
    STDMETHODIMP QueryInterface(REFIID riid, void **ppv) {      \
        return GetOwner()->QueryInterface(riid,ppv);            \
    };                                                          \
    STDMETHODIMP_(ULONG) AddRef() {                             \
        return GetOwner()->AddRef();                            \
    };                                                          \
    STDMETHODIMP_(ULONG) Release() {                            \
        return GetOwner()->Release();                           \
    };
```

## Remarks

When you create a new interface, it must derive from **IUnknown**, which has three methods: **QueryInterface**, **AddRef**, and **Release**. This macro simplifies the declaration process by declaring each of these methods for the new interface.

This macro works only with classes that derive, directly or indirectly, from the [**CUnknown**](cunknown.md) class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COM Helper Functions**](com-helper-functions.md)
</dt> <dt>

[**CUnknown::GetOwner**](cunknown-getowner.md)
</dt> <dt>

[How to Implement IUnknown](how-to-implement-iunknown.md)
</dt> </dl>

 

 




