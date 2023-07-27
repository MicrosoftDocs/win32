---
description: The ConnectFrontEnd method builds the front end of the filter graph from the current timeline.
ms.assetid: ac484fd6-b88d-4c3a-bc4d-f118083d706d
title: IRenderEngine::ConnectFrontEnd method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.ConnectFrontEnd
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine::ConnectFrontEnd method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ConnectFrontEnd` method builds the front end of the filter graph from the current timeline.

## Syntax


```C++
HRESULT ConnectFrontEnd();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible return values include the following:



| Return code                                                                                                  | Description                                                                    |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                                                            |
| <dl> <dt>**S\_WARN\_OUTPUTRESET**</dt> </dl>          | Rendering portion of the graph was deleted.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | No timeline set for this render engine.<br/>                             |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl>       | Render engine failed to initialize.<br/>                                 |
| <dl> <dt>**E\_RENDER\_ENGINE\_IS\_BROKEN**</dt> </dl> | Operation failed because the project was not rendered successfully.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>                 | Unexpected error.<br/>                                                   |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl>      | Invalid media type.<br/>                                                 |



 

## Remarks

This method does not build the rendering portion of the filter graph. The application must connect the output pins on the front end to the desired rendering filters:

-   To preview, call the [**IRenderEngine::RenderOutputPins**](irenderengine-renderoutputpins.md) method.
-   To output a file, call [**IRenderEngine::GetGroupOutputPin**](irenderengine-getgroupoutputpin.md) to retrieve the output pin for each group, then connect the pins to a multiplexer filter.

If you are using the basic render engine, the output pins on the front end produce uncompressed data. If you are using the smart render engine, the output pins produce compressed data.

If you change the timeline after you build the filter graph, you must call `ConnectFrontEnd` again to rebuild the front end. The method preserves the rendering portion of the graph whenever possible. However, if you add or delete a group, or change the order of the groups, `ConnectFrontEnd` deletes the rendering portion and your application must rebuild it. If the method deletes the rendering portion, it returns S\_WARN\_OUTPUTRESET.

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

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




