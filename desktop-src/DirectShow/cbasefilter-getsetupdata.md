---
Description: 'The GetSetupData method retrieves the registration data for the filter.'
ms.assetid: '93582c75-4f40-492c-919c-c8a06dce7715'
title: 'CBaseFilter.GetSetupData method'
---

# CBaseFilter.GetSetupData method

The `GetSetupData` method retrieves the registration data for the filter.

> [!Note]  
> This method is obsolete. It is called by the [**CBaseFilter::Register**](cbasefilter-register.md) and [**CBaseFilter::Unregister**](cbasefilter-unregister.md) methods.

 

## Syntax


```C++
virtual LPAMOVIESETUP_FILTER GetSetupData();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to an [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure containing registration information for the filter.

## Remarks

The base class returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




