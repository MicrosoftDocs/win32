---
description: The IAMTimelineTrans interface provides methods for manipulating transitions in DirectShow Editing Services (DES).
ms.assetid: e29ff0cc-0e48-4a72-8a1b-051ed62c8130
title: IAMTimelineTrans interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrans interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineTrans` interface provides methods for manipulating transitions in [DirectShow Editing Services](directshow-editing-services.md) (DES). A transition is a progression between one video layer and the rendered composite of all video layers with a lower priority. A transition can be added to any timeline object that exposes the [**IAMTimelineTransable**](iamtimelinetransable.md) interface. To set properties on a transition, use the [**IPropertySetter**](ipropertysetter.md) interface.

The DES transition object is actually a wrapper for a DirectX Transform object. Any 2-input DirectX Transform object can be used to implement the visual effect for the transition. Microsoft no longer supports the development of third-party DirectX Transform objects. To specify the DirectX Transform object for a transition, call the [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) method.

To create a transition object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_TRANSITION. You can query the returned [**IAMTimelineObj**](iamtimelineobj.md) pointer for the `IAMTimelineTrans` interface.

## Members

The **IAMTimelineTrans** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineTrans** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineTrans** interface has these methods.



| Method                                                  | Description                                                                            |
|:--------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**GetCutPoint**](iamtimelinetrans-getcutpoint.md)     | Retrieves the cut point.<br/>                                                    |
| [**GetCutPoint2**](iamtimelinetrans-getcutpoint2.md)   | Retrieves the cut point, as a [**REFTIME**](reftime.md) value.<br/>             |
| [**GetCutsOnly**](iamtimelinetrans-getcutsonly.md)     | Determines whether the transition is rendered as a cut.<br/>                     |
| [**GetSwapInputs**](iamtimelinetrans-getswapinputs.md) | Retrieves a value that indicates whether the transition inputs are swapped.<br/> |
| [**SetCutPoint**](iamtimelinetrans-setcutpoint.md)     | Sets the cut point.<br/>                                                         |
| [**SetCutPoint2**](iamtimelinetrans-setcutpoint2.md)   | Sets the cut point, as a [**REFTIME**](reftime.md) value.<br/>                  |
| [**SetCutsOnly**](iamtimelinetrans-setcutsonly.md)     | Specifies whether the transition is rendered as a cut.<br/>                      |
| [**SetSwapInputs**](iamtimelinetrans-setswapinputs.md) | Specifies whether the transition inputs are swapped.<br/>                        |



 

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

 

 
