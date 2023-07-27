---
description: The IDxtCompositor interface sets properties on the Compositor transition.This interface is used internally by DirectShow Editing Services (DES) when it renders the Compositor transition.
ms.assetid: 519f1e00-4b67-4014-906b-043f2478baa7
title: IDxtCompositor interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtCompositor
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IDxtCompositor interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IDxtCompositor` interface sets properties on the [Compositor](compositor-transition.md) transition.

This interface is used internally by DirectShow Editing Services (DES) when it renders the Compositor transition. DES applications do not have to use this interface. To set the properties on a transition in DES, use the [**IPropertySetter**](ipropertysetter.md) interface.

The Compositor transition composites a foreground image onto a background image. The *source rectangle* defines the section of the foreground image that is composited. The *destination rectangle* defines the section of the background image that receives the foreground image. The following diagram illustrates these rectangles.

![compositor transition properties](images/compmeasure.png)

## Members

The **IDxtCompositor** interface inherits from **IDXEffect**. **IDxtCompositor** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDxtCompositor** interface has these methods.



| Method                                                   | Description                                                         |
|:---------------------------------------------------------|:--------------------------------------------------------------------|
| [**get\_Height**](idxtcompositor-get-height.md)         | Retrieves the height of the target rectangle.<br/>            |
| [**get\_OffsetX**](idxtcompositor-get-offsetx.md)       | Retrieves the horizontal offset of the target rectangle.<br/> |
| [**get\_OffsetY**](idxtcompositor-get-offsety.md)       | Retrieves the vertical offset of the target rectangle.<br/>   |
| [**get\_SrcHeight**](idxtcompositor-get-srcheight.md)   | Retrieves the height of the source rectangle.<br/>            |
| [**get\_SrcOffsetX**](idxtcompositor-get-srcoffsetx.md) | Retrieves the horizontal offset of the source rectangle.<br/> |
| [**get\_SrcOffsetY**](idxtcompositor-get-srcoffsety.md) | Retrieves the vertical offset of the source rectangle.<br/>   |
| [**get\_SrcWidth**](idxtcompositor-get-srcwidth.md)     | Retrieves the width of the source rectangle.<br/>             |
| [**get\_Width**](idxtcompositor-get-width.md)           | Retrieves the width of the target rectangle.<br/>             |
| [**put\_Height**](idxtcompositor-put-height.md)         | Specifies the height of the target rectangle.<br/>            |
| [**put\_OffsetX**](idxtcompositor-put-offsetx.md)       | Specifies the horizontal offset of the target rectangle.<br/> |
| [**put\_OffsetY**](idxtcompositor-put-offsety.md)       | Specifies the vertical offset of the target rectangle.<br/>   |
| [**put\_SrcHeight**](idxtcompositor-put-srcheight.md)   | Specifies the height of the source rectangle.<br/>            |
| [**put\_SrcOffsetX**](idxtcompositor-put-srcoffsetx.md) | Specifies the horizontal offset of the source rectangle.<br/> |
| [**put\_SrcOffsetY**](idxtcompositor-put-srcoffsety.md) | Specifies the vertical offset of the source rectangle.<br/>   |
| [**put\_SrcWidth**](idxtcompositor-put-srcwidth.md)     | Specifies the width of the source rectangle.<br/>             |
| [**put\_Width**](idxtcompositor-put-width.md)           | Specifies the width of the target rectangle.<br/>             |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 




