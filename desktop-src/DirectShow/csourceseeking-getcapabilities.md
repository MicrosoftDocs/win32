---
Description: 'The GetCapabilities method retrieves all the seeking capabilities of the stream. This method implements the IMediaSeeking::GetCapabilities method.'
ms.assetid: 'a2ff7ea2-09bd-49a7-8e1b-d6360939036e'
title: 'CSourceSeeking.GetCapabilities method'
---

# CSourceSeeking.GetCapabilities method

The `GetCapabilities` method retrieves all the seeking capabilities of the stream. This method implements the [**IMediaSeeking::GetCapabilities**](imediaseeking-getcapabilities.md) method.

## Syntax


```C++
HRESULT GetCapabilities(
   DWORD *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* 
</dt> <dd>

Pointer to a variable that receives a bitwise combination of [**AM\_SEEKING\_SEEKING\_CAPABILITIES**](am-seeking-seeking-capabilities.md) flags.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer value<br/> |



 

## Remarks

The seeking capabilities are specified by the [**CSourceSeeking::m\_dwSeekingCaps**](csourceseeking-m-dwseekingcaps.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




