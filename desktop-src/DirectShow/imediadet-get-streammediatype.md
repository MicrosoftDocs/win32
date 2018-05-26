---
Description: The get\_StreamMediaType method retrieves the media type of the current stream. All video streams are converted to VIDEOINFOHEADER types, and all audio streams are converted to WAVEFORMATEX types.
ms.assetid: 7fc15cb3-af77-42c1-b5eb-d1d88bf9cd1d
title: IMediaDetget\_StreamMediaType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMediaDet::get\_StreamMediaType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_StreamMediaType` method retrieves the media type of the current stream. All video streams are converted to [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) types, and all audio streams are converted to [**WAVEFORMATEX**](/windows/win32/mmreg/?branch=master) types.

## Syntax


```C++
HRESULT get_StreamMediaType(
  [out, retval] AM_MEDIA_TYPE *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure that is filled with the media type.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

If the media detector is in bitmap grab mode, this method returns E\_INVALIDARG. For more information, see [**IMediaDet::EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md).

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




