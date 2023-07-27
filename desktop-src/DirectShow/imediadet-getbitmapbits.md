---
description: The GetBitmapBits method retrieves a video frame at the specified media time. The returned frame is always in 24-bit RGB format.
ms.assetid: b51df9d1-9c54-41bd-b0f8-ec290525deca
title: IMediaDet::GetBitmapBits method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.GetBitmapBits
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IMediaDet::GetBitmapBits method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetBitmapBits` method retrieves a video frame at the specified media time. The returned frame is always in 24-bit RGB format.

## Syntax


```C++
HRESULT GetBitmapBits(
   double StreamTime,
   long   *pBufferSize,
   char   *pBuffer,
   long   Width,
   long   Height
);
```



## Parameters

<dl> <dt>

*StreamTime* 
</dt> <dd>

Time at which to retrieve the video frame, in seconds.

</dd> <dt>

*pBufferSize* 
</dt> <dd>

Receives the required buffer size. If *pBuffer* is **NULL**, the variable receives the size of the buffer needed to retrieve the frame. If *pBuffer* is not **NULL**, this parameter is ignored.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer that receives a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure followed by the DIB bits.

</dd> <dt>

*Width* 
</dt> <dd>

Width of the video image, in pixels.

</dd> <dt>

*Height* 
</dt> <dd>

Height of the video image, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                             | Description                                                                                       |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                                                               |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>           | Could not add the [**Sample Grabber**](sample-grabber-filter.md) filter to the graph.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Insufficient memory.<br/>                                                                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer error.<br/>                                                                |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>            | Unexpected error.<br/>                                                                      |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl> | Invalid media type.<br/>                                                                    |



 

## Remarks

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

To determine the size of the buffer that is required, call this method with *pBuffer* equal to **NULL**. The size is returned in the variable pointed to by *pBufferSize*. Then create the buffer and call the method again, with *pBuffer* equal to the address of the buffer. When the method returns, the buffer contains a **BITMAPINFOHEADER** structure followed by the bitmap. The bitmap is scaled to the dimensions specified in the *Width* and *Height* parameters.

This method puts the media detector into bitmap grab mode. Once this method has been called, the various stream information methods in **IMediaDet** do not work, unless you create a new instance of the media detector.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Examples

The following code uses the `GetBitmapBits` method to create a device-independent bitmap.


```C++
long size;
hr = pDet->GetBitmapBits(0, &size, 0, width, height);
if (SUCCEEDED(hr)) 
{
    char *pBuffer = new char[size];
    if (!pBuffer)
        return E_OUTOFMEMORY;
    try {
        hr = pDet->GetBitmapBits(0, 0, pBuffer, width, height);
    }
    catch (...) {
        delete [] pBuffer;
        throw;
    }
    if (SUCCEEDED(hr))
    {
        BITMAPINFOHEADER *bmih = (BITMAPINFOHEADER*)pBuffer;
        HDC hdcDest = GetDC(0);
        
        // Find the address of the start of the image data.
        void *pData = pBuffer + sizeof(BITMAPINFOHEADER);
        
        // Note: In general a BITMAPINFOHEADER can include extra color
        // information at the end, so calculating the offset to the image
        // data is not generally correct. However, the IMediaDet interface
        // always returns an RGB-24 image with no extra color information.
        
        BITMAPINFO bmi;
        ZeroMemory(&bmi, sizeof(BITMAPINFO));
        CopyMemory(&(bmi.bmiHeader), bmih, sizeof(BITMAPINFOHEADER));
        HBITMAP hBitmap = CreateDIBitmap(hdcDest, bmih, CBM_INIT, 
            pData, &bmi, DIB_RGB_COLORS);
    }
    delete[] pBuffer;
}
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




