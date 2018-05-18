---
Description: 'Note  This interface is deprecated. New applications should not use it. Retrieves a pointer to the DirectDraw object used by the current media stream.'
ms.assetid: '44c505fe-70d9-49bd-9135-8a6dc2c72e98'
title: 'IDirectDrawMediaStream::GetDirectDraw method'
---

# IDirectDrawMediaStream::GetDirectDraw method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Retrieves a pointer to the DirectDraw object used by the current media stream.

## Syntax


```C++
HRESULT GetDirectDraw(
  [out] IDirectDraw **ppDirectDraw
);
```



## Parameters

<dl> <dt>

*ppDirectDraw* \[out\]
</dt> <dd>

Address of a pointer to an **IDirectDraw** interface that will contain the current media stream's associated DirectDraw object.

</dd> </dl>

## Return value

Returns S\_OK if successful or E\_POINTER if the parameter is invalid.

## Remarks

If you haven't initialized the stream yet, the retrieved pointer will be **NULL** and the method will return S\_OK. If you have initialized the stream, this method increments the retrieved pointer's reference count.

## See also

<dl> <dt>

[**IDirectDrawMediaStream Interface**](idirectdrawmediastream.md)
</dt> </dl>

 

 



