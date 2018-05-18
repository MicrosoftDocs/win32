---
Description: 'Note  This interface is deprecated. New applications should not use it. The Seek method seeks all of the media streams to a new position.'
ms.assetid: 'ac65613f-3fca-4043-83ad-740ebd7687a4'
title: 'IMultiMediaStream::Seek method'
---

# IMultiMediaStream::Seek method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `Seek` method seeks all of the media streams to a new position.

## Syntax


```C++
HRESULT Seek(
  [in] STREAM_TIME SeekTime
);
```



## Parameters

<dl> <dt>

*SeekTime* \[in\]
</dt> <dd>

[**STREAM\_TIME**](stream-time.md) value that specifies the new position.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                   | Description                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | The media streams do not support seeking.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                  |



 

## Remarks

To determine whether the media streams support seeking, call the [**IMultiMediaStream::GetInformation**](imultimediastream-getinformation.md) method.

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




