---
description: The CAutoUsingOutputPin class obtains and releases access to a CDynamicOutputPin object.
ms.assetid: 4ded5d18-4b14-4574-ad1f-73b886a51fac
title: CAutoUsingOutputPin class (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAutoUsingOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAutoUsingOutputPin class

The **CAutoUsingOutputPin** class obtains and releases access to a [**CDynamicOutputPin**](cdynamicoutputpin.md) object.

**CAutoUsingOutputPin** has these types of members:



| Public Methods                                                           | Description                                              |
|--------------------------------------------------------------------------|----------------------------------------------------------|
| [**CAutoUsingOutputPin**](cautousingoutputpin-cautousingoutputpin.md)   | Constructor method. Obtains access to the specified pin. |
| [**~CAutoUsingOutputPin**](cautousingoutputpin--cautousingoutputpin.md) | Destructor method. Obtains access to the specified pin.  |



 

## Remarks

When certain methods are called on [**CDynamicOutputPin**](cdynamicoutputpin.md), the caller must obtain access to the pin and then release that access. To obtain access, the caller uses the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method. To release access, it calls the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method. The **CAutoUsingOutputPin** class is a helper class that handles these tasks in its constructor and destructor methods. The following code example shows how to use this class:


```
CDynamicOutputPin *pPin;
HRESULT hr = S_OK;  // Important! Initialize to S_OK.

// TODO: Obtain a pointer to the pin (not shown).

// Scope for lock.
{
    // Hold lock on pin.
    CAutoUsingOutputPin UsingPin(pPin, &hr)

    if (SUCCEEDED(hr)) 
    {

        // Safe to use the pin.
        hr = pPin->Deliver(pSample);

    }

} // Object goes out of scope here.

// No longer safe to use the pin.
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Base Class Reference](base-class-reference.md)
</dt> </dl>

 

 




