---
description: The CanSeekForward method determines whether the stream can be seeked forward. This method implements the IMediaPosition::CanSeekForward method.
ms.assetid: ccb2db8d-b52e-4e3d-b49b-9689197a974a
title: CPosPassThru.CanSeekForward method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.CanSeekForward
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.CanSeekForward method

The `CanSeekForward` method determines whether the stream can be seeked forward. This method implements the [**IMediaPosition::CanSeekForward**](/windows/desktop/api/Control/nf-control-imediaposition-canseekforward) method.

## Syntax


```C++
HRESULT CanSeekForward(
   LONG *pCanSeekForward
);
```



## Parameters

<dl> <dt>

*pCanSeekForward* 
</dt> <dd>

Pointer to a variable that receives the value OATRUE if the filter can seek forward, or OAFALSE otherwise.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




