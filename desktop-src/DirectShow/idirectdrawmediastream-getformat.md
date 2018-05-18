---
Description: 'Note  This interface is deprecated. New applications should not use it. Retrieves the current media stream''s format and, optionally, its desired format.'
ms.assetid: '3729bbe6-3504-46b3-9978-e66afc56344f'
title: 'IDirectDrawMediaStream::GetFormat method'
---

# IDirectDrawMediaStream::GetFormat method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Retrieves the current media stream's format and, optionally, its desired format.

## Syntax


```C++
HRESULT GetFormat(
  [out] DDSURFACEDESC      *pDDSDCurrent,
  [out] IDirectDrawPalette **ppDirectDrawPalette,
  [out] DDSURFACEDESC      *pDDSDDesired,
  [out] DWORD              *pdwFlags
);
```



## Parameters

<dl> <dt>

*pDDSDCurrent* \[out\]
</dt> <dd>

Pointer to a DirectDraw surface description that will contain the current media stream's format.

</dd> <dt>

*ppDirectDrawPalette* \[out\]
</dt> <dd>

Address of a pointer to an **IDirectDrawPalette** interface if one exists.

</dd> <dt>

*pDDSDDesired* \[out\]
</dt> <dd>

Pointer to a DirectDraw surface description that will contain the current media stream's desired format.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Pointer to the flags set in a **DDSURFACEDESC** structure. Flags of interest include:



| Flag              | Description                                                             |
|-------------------|-------------------------------------------------------------------------|
| DDSD\_CAPS        | Indicates that the surface capability member of the structure is valid. |
| DDSD\_HEIGHT      | Indicates that the height member of the structure is valid.             |
| DDSD\_PIXELFORMAT | Indicates that the pixel format member of the structure is valid.       |
| DDSD\_WIDTH       | Indicates that the width member of the structure is valid.              |



 

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                         | Description                                                     |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**DDERR\_INVALIDPARAMS**</dt> </dl> | One of the DirectDraw surface parameters is invalid.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>           | One or more of the required parameters is invalid.<br/>   |
| <dl> <dt>**S\_OK**</dt> </dl>                | Success.<br/>                                             |



 

## Remarks

After you call this method, you can either conform to the current format or attempt to change the format by calling the [**IDirectDrawMediaStream::SetFormat**](idirectdrawmediastream-setformat.md) method.

All of this method's parameters are optional; set any of them to **NULL** to indicate that you don't want to retrieve that information.

To perform a progressive render, create a single sample and repeatedly use that sample for successive frames of video. Video decompressors use this technique to do partial updates to the previous frame.

You must initialize the *dwSize* member of the **DDSURFACEDESC** structure before calling this method.

The DDSD\_CAPS flag will return one of the values listed in the **DDSCAPS** structure or DDSCAPS\_DATAEXCHANGE, which is defined as DDSCAPS\_SYSTEMMEMORY\|DDSCAPS\_VIDEOMEMORY in Ddrawex.h.

## See also

<dl> <dt>

[**IDirectDrawMediaStream Interface**](idirectdrawmediastream.md)
</dt> </dl>

 

 




