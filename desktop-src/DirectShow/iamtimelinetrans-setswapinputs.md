---
description: The SetSwapInputs method specifies whether the transition inputs are swapped.
ms.assetid: c7303302-dbc4-41b6-8049-5c4496ee9264
title: IAMTimelineTrans::SetSwapInputs method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.SetSwapInputs
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrans::SetSwapInputs method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetSwapInputs` method specifies whether the transition inputs are swapped.

By default, a transition goes from the composite of all lower-priority layers to the layer where the transition resides. You can reverse this progression, so the transition goes from the layer where it resides back to the composite of lower-priority layers. For more information, see [Transition Direction](transition-direction.md).

## Syntax


```C++
HRESULT SetSwapInputs(
   BOOL Val
);
```



## Parameters

<dl> <dt>

*Val* 
</dt> <dd>

Specifies whether the inputs are swapped. If **FALSE**, the transition goes from the composite of all lower-priority layers to the transition layer. If **TRUE**, the transition goes in the opposite direction.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method does not change the direction of the visual effect. For example, a left-to-right wipe will still go from left to right. To change the direction, set the **Progress** property using the [**IPropertySetter**](ipropertysetter.md) interface.

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

[**IAMTimelineTrans Interface**](iamtimelinetrans.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




