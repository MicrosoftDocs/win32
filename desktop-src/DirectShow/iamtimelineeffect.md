---
description: The IAMTimelineEffect interface provides methods for manipulating audio and video effects in DirectShow Editing Services (DES).
ms.assetid: 3cc8a5f8-3f57-4e2b-82dd-827e04c771f7
title: IAMTimelineEffect interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffect
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineEffect interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineEffect` interface provides methods for manipulating audio and video effects in [DirectShow Editing Services](directshow-editing-services.md) (DES). An effect can be added to any timeline object that exposes the [**IAMTimelineEffectable**](iamtimelineeffectable.md) interface. To set properties on an effect, use the [**IPropertySetter**](ipropertysetter.md) interface.

The DES effect object is actually a wrapper for one of two other objects:

-   For audio effects, any DirectShow audio effect filter.
-   For video effects, and 1-input DirectX Transform object.

Microsoft no longer supports the development of third-party DirectX Transform objects.

To specify the filter or DirectX Transform object for an effect, call the [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) method.

To create an effect object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_EFFECT. You can query the returned [**IAMTimelineObj**](iamtimelineobj.md) pointer for the `IAMTimelineEffect` interface.

## Members

The **IAMTimelineEffect** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineEffect** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineEffect** interface has these methods.



| Method                                                           | Description                                       |
|:-----------------------------------------------------------------|:--------------------------------------------------|
| [**EffectGetPriority**](iamtimelineeffect-effectgetpriority.md) | Retrieves the effect's priority level.<br/> |



 

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



## See also

<dl> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 
