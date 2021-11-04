---
description: The WriteBitmapBits method retrieves a video frame at the specified media time and writes it to a file. The video frame is always in 24-bit RGB format.
ms.assetid: 8b21f37b-553d-4de2-8725-c94c29fa3a1a
title: IMediaDet::WriteBitmapBits method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.WriteBitmapBits
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::WriteBitmapBits method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `WriteBitmapBits` method retrieves a video frame at the specified media time and writes it to a file. The video frame is always in 24-bit RGB format.

## Syntax


```C++
HRESULT WriteBitmapBits(
   double StreamTime,
   long   Width,
   long   Height,
   BSTR   Filename
);
```



## Parameters

<dl> <dt>

*StreamTime* 
</dt> <dd>

Time at which to retrieve the video frame.

</dd> <dt>

*Width* 
</dt> <dd>

Width of the image, in pixels.

</dd> <dt>

*Height* 
</dt> <dd>

Height of the image, in pixels.

</dd> <dt>

*Filename* 
</dt> <dd>

Path of the file in which to save the bitmap. If the file already exists, this method overwrites it.

</dd> </dl>

## Return value

Returns S\_OK it successful. Otherwise, returns an **HRESULT** value that indicates the cause of the error. Possible error codes include the following:



| Return code                                                                                             | Description                                                                                       |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>           | Could not add the [**Sample Grabber**](sample-grabber-filter.md) filter to the graph.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Failure.<br/>                                                                               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Insufficient memory.<br/>                                                                   |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>            | Unexpected error.<br/>                                                                      |
| <dl> <dt>**STG\_E\_ACCESSDENIED**</dt> </dl>     | Cannot overwrite file.<br/>                                                                 |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl> | Invalid media type.<br/>                                                                    |



 

## Remarks

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

This method puts the media detector into bitmap grab mode. Once this method has been called, the various stream information methods in **IMediaDet** do not work, unless you create a new instance of the media detector.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

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

 

 




