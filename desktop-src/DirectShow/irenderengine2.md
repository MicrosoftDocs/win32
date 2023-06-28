---
description: The IRenderEngine2 interface enables the application to replace the default video resizing filter used by DirectShow Editing Services (DES). The Basic Render Engine and the Smart Render Engine both support this interface.
ms.assetid: 37603c73-e199-431a-9a1e-a40c77755c70
title: IRenderEngine2 interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine2 interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IRenderEngine2` interface enables the application to replace the default video resizing filter used by DirectShow Editing Services (DES). The [Basic Render Engine](basic-render-engine.md) and the [Smart Render Engine](smart-render-engine.md) both support this interface.

## Members

The **IRenderEngine2** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IRenderEngine2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IRenderEngine2** interface has these methods.



| Method                                                  | Description                                                                             |
|:--------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**SetResizerGUID**](irenderengine2-setresizerguid.md) | Specifies the CLSID of a custom resizing filter provided by the application.<br/> |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Providing a Custom Video Resizer](providing-a-custom-video-resizer.md)
</dt> </dl>

 

 
