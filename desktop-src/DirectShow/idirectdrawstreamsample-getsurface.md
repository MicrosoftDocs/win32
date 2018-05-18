---
Description: 'Note  This interface is deprecated. New applications should not use it. Retrieves pointers to the current sample''s DirectDraw surface and associated clipping rectangle.'
ms.assetid: 'c6802940-53e5-4458-a1eb-deddd807a18a'
title: 'IDirectDrawStreamSample::GetSurface method'
---

# IDirectDrawStreamSample::GetSurface method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Retrieves pointers to the current sample's DirectDraw surface and associated clipping rectangle.

## Syntax


```C++
HRESULT GetSurface(
  [out] IDirectDrawSurface **ppDirectDrawSurface,
  [out] RECT               *pRect
);
```



## Parameters

<dl> <dt>

*ppDirectDrawSurface* \[out\]
</dt> <dd>

Address of a pointer to an **IDirectDrawSurface** interface that specifies the sample's new surface. Set this parameter to **NULL** if you don't want to specify a new surface.

</dd> <dt>

*pRect* \[out\]
</dt> <dd>

Pointer to a **RECT** structure that will contain the current sample's clipping rectangle. Set this parameter to **NULL** if you don't want to retrieve the clipping rectangle.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Both parameters are optional. All implementations of this interface must support **NULL** values as valid parameters. If you retrieve a surface pointer, this method increments its reference count, so you must release the reference.

## See also

<dl> <dt>

[**IDirectDrawStreamSample Interface**](idirectdrawstreamsample.md)
</dt> </dl>

 

 



