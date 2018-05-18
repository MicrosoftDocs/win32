---
Description: 'Note  This interface is deprecated. New applications should not use it. Allocates a new stream sample object for the current media stream.'
ms.assetid: 'a035797d-ebf2-40c2-b1a3-b903a691b7d2'
title: 'IMediaStream::AllocateSample method'
---

# IMediaStream::AllocateSample method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Allocates a new stream sample object for the current media stream.

## Syntax


```C++
HRESULT AllocateSample(
  [in]  DWORD         dwFlags,
  [out] IStreamSample **ppSample
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags. Must be zero.

</dd> <dt>

*ppSample* \[out\]
</dt> <dd>

Address of a pointer to the newly created stream sample's [**IStreamSample**](istreamsample.md) interface.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                   | Description                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There isn't enough memory available to create a stream sample.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A parameter is invalid.<br/>                                        |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                                       |



 

## Remarks

This method allocates the sample and its associated backing object or buffer. The backing object is either the DirectDraw surface for video or the [**IAudioData**](iaudiodata.md) object for audio.

## See also

<dl> <dt>

[**IMediaStream Interface**](imediastream.md)
</dt> </dl>

 

 




