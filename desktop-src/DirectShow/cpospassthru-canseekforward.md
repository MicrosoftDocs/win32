---
Description: 'The CanSeekForward method determines whether the stream can be seeked forward. This method implements the IMediaPosition::CanSeekForward method.'
ms.assetid: 'ccb2db8d-b52e-4e3d-b49b-9689197a974a'
title: 'CPosPassThru.CanSeekForward method'
---

# CPosPassThru.CanSeekForward method

The `CanSeekForward` method determines whether the stream can be seeked forward. This method implements the [**IMediaPosition::CanSeekForward**](imediaposition-canseekforward.md) method.

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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




