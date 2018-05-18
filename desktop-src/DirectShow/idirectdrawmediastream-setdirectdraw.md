---
Description: 'Note  This interface is deprecated. New applications should not use it. Sets the current media stream''s DirectDraw object.'
ms.assetid: 'ffa425c5-5f81-4963-bf23-2139d8b245b3'
title: 'IDirectDrawMediaStream::SetDirectDraw method'
---

# IDirectDrawMediaStream::SetDirectDraw method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Sets the current media stream's DirectDraw object.

## Syntax


```C++
HRESULT SetDirectDraw(
  [in] IDirectDraw *pDirectDraw
);
```



## Parameters

<dl> <dt>

*pDirectDraw* \[in\]
</dt> <dd>

Pointer to an **IDirectDraw** interface that contains the media stream's new DirectDraw object.

</dd> </dl>

## Return value

Returns S\_OK if successful or E\_POINTER if the pointer is invalid.

## Remarks

This method fails if the current stream already has allocated samples and its DirectDraw object differs from the specified one. It will always succeed if the specified DirectDraw object matches the stream's current object.

If this stream has no allocated samples, you can set *pDirectDraw* to **NULL**. This forces the stream to release its reference to the current DirectDraw object.

## See also

<dl> <dt>

[**IDirectDrawMediaStream Interface**](idirectdrawmediastream.md)
</dt> </dl>

 

 



