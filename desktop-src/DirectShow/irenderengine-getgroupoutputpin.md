---
description: The GetGroupOutputPin method retrieves the output pin for the specified group.
ms.assetid: be4e17b6-15bf-43b1-8d93-d52d08c8bce6
title: IRenderEngine::GetGroupOutputPin method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.GetGroupOutputPin
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine::GetGroupOutputPin method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetGroupOutputPin` method retrieves the output pin for the specified group.

## Syntax


```C++
HRESULT GetGroupOutputPin(
        long Group,
  [out] IPin **ppRenderPin
);
```



## Parameters

<dl> <dt>

*Group* 
</dt> <dd>

Zero-based index that specifies the group.

</dd> <dt>

*ppRenderPin* \[out\]
</dt> <dd>

Receives a pointer to the output pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                                  | Description                                                                |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | Group does not have an output pin.<br/>                              |
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Invalid argument.<br/>                                               |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl>       | Render engine failed to initialize.<br/>                             |
| <dl> <dt>**E\_POINTER**</dt> </dl>                    | Invalid pointer.<br/>                                                |
| <dl> <dt>**E\_RENDER\_ENGINE\_IS\_BROKEN**</dt> </dl> | Operation failed because project was not rendered successfully.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>                 | Unexpected error.<br/>                                               |



 

## Remarks

Before calling this method, call [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) to build the front end of the graph. Each group represents a single media stream, and the front end has a corresponding output pin.

You can use this method to create the rendering portion of a file-writing graph. Connect the output pins to multiplexer filters and file writer filters. For more information, see [Rendering a Project](rendering-a-project.md).

For preview, you don't need to call this method. Just call **ConnectFrontEnd** followed by [**IRenderEngine::RenderOutputPins**](irenderengine-renderoutputpins.md).

If the method returns S\_OK, the **IPin** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

 

 




