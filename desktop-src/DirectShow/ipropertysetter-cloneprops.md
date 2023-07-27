---
description: The CloneProps method clones a set of properties from this property setter and adds them to a new property setter.
ms.assetid: dee93e41-2925-4b4b-b5b2-7cfd6ea10e05
title: IPropertySetter::CloneProps method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.CloneProps
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IPropertySetter::CloneProps method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `CloneProps` method clones a set of properties from this property setter and adds them to a new property setter.

## Syntax


```C++
HRESULT CloneProps(
  [out] IPropertySetter **ppSetter,
  [in]  REFERENCE_TIME  rtStart,
  [in]  REFERENCE_TIME  rtStop
);
```



## Parameters

<dl> <dt>

*ppSetter* \[out\]
</dt> <dd>

Receives a pointer to the **IPropertySetter** interface of the new property setter.

</dd> <dt>

*rtStart* \[in\]
</dt> <dd>

Start time of the range of values to clone, in 100-nanosecond units.

</dd> <dt>

*rtStop* \[in\]
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Only values that fall after the specified start time are cloned. The times on the cloned values are then adjusted relative to the start time. For example, if *rtStart* is 20000000 (2 seconds), then a value at time 30000000 (3 seconds) is cloned with time 10000000 (1 second). Finally, each cloned property is given an initial value equal to the value of the original property at the start time (correctly interpolated if necessary). In effect, the property data is split at the specified start time.

If the method succeeds, the [**IPropertySetter**](ipropertysetter.md) interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




