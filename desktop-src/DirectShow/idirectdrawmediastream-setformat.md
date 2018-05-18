---
Description: 'Note  This interface is deprecated. New applications should not use it. Sets the format of the current media stream.'
ms.assetid: '465b4f0c-40e1-4aec-be62-0b55c29fa05e'
title: 'IDirectDrawMediaStream::SetFormat method'
---

# IDirectDrawMediaStream::SetFormat method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Sets the format of the current media stream.

## Syntax


```C++
HRESULT SetFormat(
  [in] const DDSURFACEDESC      *pDDSurfaceDesc,
  [in]       IDirectDrawPalette *pDirectDrawPalette
);
```



## Parameters

<dl> <dt>

*pDDSurfaceDesc* \[in\]
</dt> <dd>

Pointer to a DirectDraw surface description that contains the new format.

</dd> <dt>

*pDirectDrawPalette* \[in\]
</dt> <dd>

Optional parameter that is a pointer to an **IDirectDrawPalette** interface.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                              | Description                                                                                                  |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDERR\_INVALIDSURFACETYPE**</dt> </dl> | The specified format is incompatible with the current stream.<br/>                                     |
| <dl> <dt>**MS\_E\_SAMPLEALLOC**</dt> </dl>        | Can't change the format because one or more stream samples are already allocated for this stream.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                                                          |



 

## Remarks

If the stream already has allocated samples and the sample format doesn't match the specified format, this method fails. This method always succeeds if the specified format matches the current format.

## See also

<dl> <dt>

[**IDirectDrawMediaStream Interface**](idirectdrawmediastream.md)
</dt> </dl>

 

 




