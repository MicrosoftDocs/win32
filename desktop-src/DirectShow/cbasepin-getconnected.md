---
description: The GetConnected method retrieves the pin connected to this pin.
ms.assetid: 7b47aa8e-55a9-45f8-aa32-902fee037c72
title: CBasePin.GetConnected method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.GetConnected
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.GetConnected method

The `GetConnected` method retrieves the pin connected to this pin.

## Syntax


```C++
IPin* GetConnected();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the other pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

## Remarks

If the pin is not connected, this method returns **NULL**. Call the [**CBasePin::IsConnected**](cbasepin-isconnected.md) method to determine whether the pin is connected.

The method does not call **AddRef** on the **IPin** interface, so the caller should not release the interface.

## Examples

Because the reference count is not incremented on the returned pointer, you can chain method calls together:


```C++
if (m_MyPin->IsConnected())
{
    m_MyPin->GetConnected()->EndOfStream();
}
```



This coding pattern is very convenient; but as the example shows, you must be careful not to dereference a **NULL** pointer when the pin is unconnected.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




