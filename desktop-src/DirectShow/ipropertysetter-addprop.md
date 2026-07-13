---
description: The AddProp method adds a property to the property setter, with an array of time-value pairs defining the value of the property over a range of time.
ms.assetid: bf49e6ed-110d-4851-ace9-04d025f1d21f
title: IPropertySetter::AddProp method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.AddProp
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IPropertySetter::AddProp method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `AddProp` method adds a property to the property setter, with an array of time-value pairs defining the value of the property over a range of time.

## Syntax


```C++
HRESULT AddProp(
  [in] DEXTER_PARAM Param,
  [in] DEXTER_VALUE *paValue
);
```



## Parameters

<dl> <dt>

*Param* \[in\]
</dt> <dd>

[**DEXTER\_PARAM**](dexter-param.md) structure that specifies the property. The **nValues** member of the structure must equal the size of the array given in the *paValue* parameter.

</dd> <dt>

*paValue* \[in\]
</dt> <dd>

Pointer to an array of [**DEXTER\_VALUE**](dexter-value.md) structures that contain time-value pairs. The array must be in ascending time order. The times are relative to the starting time of the effect or transition.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The first [**DEXTER\_VALUE**](dexter-value.md) structure must specify a reference time of zero and an interpolation flag (**dwInterp**) of **DEXTERF\_JUMP**, or the method returns an error.

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

 

 




