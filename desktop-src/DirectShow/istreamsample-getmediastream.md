---
Description: 'Note  This interface is deprecated. New applications should not use it. Retrieves a pointer to the media stream object that created the current sample.'
ms.assetid: 'dfc38480-7b8d-42ad-937b-dd39384796c9'
title: 'IStreamSample::GetMediaStream method'
---

# IStreamSample::GetMediaStream method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Retrieves a pointer to the media stream object that created the current sample.

## Syntax


```C++
HRESULT GetMediaStream(
  [in] IMediaStream **ppMediaStream
);
```



## Parameters

<dl> <dt>

*ppMediaStream* \[in\]
</dt> <dd>

Address of a pointer to an [**IMediaStream**](imediastream.md) interface that will point to the media stream that created the current sample.

</dd> </dl>

## Return value

Returns S\_OK if successful or E\_POINTER if *ppMediaStream* is invalid.

## Remarks

If successful, this method increments the reference count of the media stream specified by *ppMediaStream*.

## See also

<dl> <dt>

[**IStreamSample Interface**](istreamsample.md)
</dt> </dl>

 

 



