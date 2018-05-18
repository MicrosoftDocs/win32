---
Description: 'Note  This interface is deprecated. New applications should not use it. The GetTime method retrieves the current stream time.'
ms.assetid: 'da92c68b-176c-4773-9ae1-63f803bc206e'
title: 'IMultiMediaStream::GetTime method'
---

# IMultiMediaStream::GetTime method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The **GetTime** method retrieves the current stream time.

## Syntax


```C++
HRESULT GetTime(
  [out] STREAM_TIME *pCurrentTime
);
```



## Parameters

<dl> <dt>

*pCurrentTime* \[out\]
</dt> <dd>

Pointer to a variable that receives the stream time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                               | Description                                                     |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>                           |
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Could not get the stream time, or there is no clock.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                                             |



 

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




