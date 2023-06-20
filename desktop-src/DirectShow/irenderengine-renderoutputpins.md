---
description: The RenderOutputPins method creates the previewing portion of the filter graph.
ms.assetid: 66bcb698-cd85-4c22-bfef-2e51973958f1
title: IRenderEngine::RenderOutputPins method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.RenderOutputPins
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine::RenderOutputPins method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `RenderOutputPins` method creates the previewing portion of the filter graph.

## Syntax


```C++
HRESULT RenderOutputPins();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** values. The following are possible values:



| Return code                                                                                                  | Description                                                                |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                                                        |
| <dl> <dt>**VFW\_S\_AUDIO\_NOT\_RENDERED**</dt> </dl>  | Cannot play back the audio stream.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Invalid argument.<br/>                                               |
| <dl> <dt>**E\_RENDER\_ENGINE\_IS\_BROKEN**</dt> </dl> | Operation failed because project was not rendered successfully.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>                 | Unexpected error.<br/>                                               |



 

## Remarks

Before calling this method, call [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) to build the front end of the graph. To perform an operation other than preview, do not call this method. Instead, call [**IRenderEngine::GetGroupOutputPin**](irenderengine-getgroupoutputpin.md) to obtain pointers to the output pins.

If there is no sound card on the user's computer, this method returns VFW\_S\_AUDIO\_NOT\_RENDERED. There will not be audio preview in this case, but video preview is unaffected.

If the pin is from a video group, this method creates a video window. The calling thread must dispatch messages—for example, to move the window, or respond to mouse clicks in the window's client area.

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

 

 




