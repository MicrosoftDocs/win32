---
description: The SetSmartRecompressFormat method specifies a video compression format to use for smart recompression.
ms.assetid: 80c02215-6da2-4b3e-ab0d-004e49480fb9
title: IAMTimelineGroup::SetSmartRecompressFormat method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.SetSmartRecompressFormat
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::SetSmartRecompressFormat method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetSmartRecompressFormat` method specifies a video compression format to use for smart recompression.

Smart recompression is not supported for audio groups.

## Syntax


```C++
HRESULT SetSmartRecompressFormat(
   long *pFormat
);
```



## Parameters

<dl> <dt>

*pFormat* 
</dt> <dd>

Pointer to a structure describing the compression format. Currently, only the [**SCompFmt0**](scompfmt0.md) structure is valid. You must cast this parameter to a pointer of type **long**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Before calling this method, call the [**IAMTimelineGroup::SetMediaType**](iamtimelinegroup-setmediatype.md) method on the same group, to specify an uncompressed format.

If the `SetSmartRecompressFormat` method succeeds, you can use the Smart Render Engine to output a compressed video stream. The compressed video will have the width, height, and frame rate that was specified in the *pFormat* parameter. These values will override those given for the uncompressed format in the **SetMediaType** method. However, to get the benefits of smart recompression, the two formats should match. In other words, the compressed and uncompressed formats should have the same height, width, and frame rate.

If the Smart Render Engine is unable to produce the compressed format, it will produce an uncompressed video stream instead. If that occurs, the Smart Render Engine reports a DEX\_IDS\_CANT\_FIND\_COMPRESSOR rendering error during the [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) method. The application can catch this error through the [**IAMErrorLog::LogError**](iamerrorlog-logerror.md) method. (For more information, see [Logging Errors](logging-errors.md) and [Rendering Errors](rendering-errors.md).)

The smart recompression format is not persistent. If an application uses smart recompression, it must set the recompression format whenever it loads a project file.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[Smart Render Engine](smart-render-engine.md)
</dt> <dt>

[Writing a Project to a File](writing-a-project-to-a-file.md)
</dt> </dl>

 

 




