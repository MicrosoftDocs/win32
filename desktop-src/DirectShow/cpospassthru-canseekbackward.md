---
Description: 'The CanSeekBackward method determines whether the stream can be seeked backward. This method implements the IMediaPosition::CanSeekBackward method.'
ms.assetid: '6443980f-6863-4941-b2dd-4a31257b5810'
title: 'CPosPassThru.CanSeekBackward method'
---

# CPosPassThru.CanSeekBackward method

The `CanSeekBackward` method determines whether the stream can be seeked backward. This method implements the [**IMediaPosition::CanSeekBackward**](imediaposition-canseekbackward.md) method.

## Syntax


```C++
HRESULT CanSeekBackward(
   LONG *pCanSeekBackward
);
```



## Parameters

<dl> <dt>

*pCanSeekBackward* 
</dt> <dd>

Pointer to a variable that receives the value OATRUE if the filter can seek backward, or OAFALSE otherwise.

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

 

 




