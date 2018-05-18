---
Description: 'Note  This interface is deprecated. New applications should not use it. The GetDuration method retrieves the duration of the multimedia stream.'
ms.assetid: '4d8104ec-aa2a-4151-bb7f-53611d4a71f2'
title: 'IMultiMediaStream::GetDuration method'
---

# IMultiMediaStream::GetDuration method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `GetDuration` method retrieves the duration of the multimedia stream.

## Syntax


```C++
HRESULT GetDuration(
  [out] STREAM_TIME *pDuration
);
```



## Parameters

<dl> <dt>

*pDuration* \[out\]
</dt> <dd>

Pointer to a variable that receives of the multimedia stream, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                             | Description                                                 |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>           | This multimedia stream does not support seeking.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer value.<br/>                          |
| <dl> <dt>**MS\_E\_INVALIDSTREAMTYPE**</dt> </dl> | This multimedia stream is not read-only.<br/>         |
| <dl> <dt>**S\_FALSE**</dt> </dl>                 | Could not determine the duration.<br/>                |
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                         |



 

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




