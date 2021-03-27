---
description: The SetControlWindowPin method sets the pin with which to synchronize.
ms.assetid: 6373c046-5448-4159-88b9-9b2babdb938b
title: CBaseControlWindow.SetControlWindowPin method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.SetControlWindowPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.SetControlWindowPin method

The `SetControlWindowPin` method sets the pin with which to synchronize.

## Syntax


```C++
void SetControlWindowPin(
   CBasePin *pPin
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the pin with which the interface is synchronized.

</dd> </dl>

## Return value

No return value.

## Remarks

This member function sets the m\_pPin member variable equal to the pPin parameter. As described in the constructor, the interface can be called only when the filter has been connected successfully. The object is passed in through this member function to the pin with which it should synchronize; in most cases, it will determine if the pin is connected whenever it has an interface method called and will return VFW\_E\_NOT\_CONNECTED if it fails.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




