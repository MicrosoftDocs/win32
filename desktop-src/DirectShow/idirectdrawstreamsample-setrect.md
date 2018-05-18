---
Description: 'Note  This interface is deprecated. New applications should not use it. Changes the clipping rectangle for a sample.'
ms.assetid: '10b25552-e923-4cd5-afb7-52164057f2e0'
title: 'IDirectDrawStreamSample::SetRect method'
---

# IDirectDrawStreamSample::SetRect method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Changes the clipping rectangle for a sample.

## Syntax


```C++
HRESULT SetRect(
  [in] const RECT *pRect
);
```



## Parameters

<dl> <dt>

*pRect* \[in\]
</dt> <dd>

Pointer to a **RECT** structure that specifies the stream's new clipping rectangle.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                              | Description                                                                                               |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDERR\_INVALIDPIXELFORMAT**</dt> </dl> | The stream isn't compatible with the pixel format.<br/>                                             |
| <dl> <dt>**DDERR\_INVALIDRECT**</dt> </dl>        | The specified rectangle is invalid.<br/>                                                            |
| <dl> <dt>**DDERR\_INVALIDSURFACETYPE**</dt> </dl> | The stream isn't compatible with the surface.<br/>                                                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>                | One of the pointers is invalid.<br/>                                                                |
| <dl> <dt>**MS\_E\_SAMPLEALLOC**</dt> </dl>        | The stream format doesn't match the surface and samples are currently allocated to the stream.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                                                       |



 

## Remarks

Both parameters are optional; set either to **NULL** to avoid changing that value. If the surface format doesn't match the stream format, this method fails.

If the new rectangle's size isn't the same as the current rectangle, a call to this method will fail.

## See also

<dl> <dt>

[**IDirectDrawStreamSample Interface**](idirectdrawstreamsample.md)
</dt> </dl>

 

 




