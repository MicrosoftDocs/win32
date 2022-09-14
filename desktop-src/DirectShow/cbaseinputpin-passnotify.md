---
description: The PassNotify method passes a quality-control message to the appropriate object.
ms.assetid: dbc9a4b7-a522-4fbf-8e3a-af50e11c1d80
title: CBaseInputPin.PassNotify method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.PassNotify
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.PassNotify method

The `PassNotify` method passes a quality-control message to the appropriate object.

## Syntax


```C++
HRESULT PassNotify(
   Quality q
);
```



## Parameters

<dl> <dt>

*q* 
</dt> <dd>

[**Quality**](/windows/win32/api/strmif/ns-strmif-quality) structure that contains the quality-control message.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                       | Description                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                                        |
| <dl> <dt>**VFW\_E\_NOT\_FOUND**</dt> </dl> | Could not find an object to accept the message.<br/> |



 

## Remarks

Call this method if the filter does not handle quality-control messages. This method passes the message to one of the following objects, in order of preference:

-   An external quality-control manager, if the [**IQualityControl::SetSink**](/windows/desktop/api/Strmif/nf-strmif-iqualitycontrol-setsink) method was called.
-   The upstream output pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> <dt>

[Quality-Control Management](quality-control-management.md)
</dt> </dl>

 

 




