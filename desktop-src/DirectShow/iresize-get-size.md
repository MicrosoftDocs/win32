---
description: The get\_Size method returns the current output size and stretch mode.
ms.assetid: 61c0e439-26ce-45fc-986a-0ffc17056a55
title: IResize::get_Size method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize.get_Size
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IResize::get\_Size method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_Size` method returns the current output size and stretch mode.

## Syntax


```C++
HRESULT get_Size(
  [out] int  *piHeight,
  [out] int  *piWidth,
  [out] long *pFlag
);
```



## Parameters

<dl> <dt>

*piHeight* \[out\]
</dt> <dd>

Receives the video height, in pixels.

</dd> <dt>

*piWidth* \[out\]
</dt> <dd>

Receives the video width, in pixels.

</dd> <dt>

*pFlag* \[out\]
</dt> <dd>

Receives a flag specifying the stretch mode. See [**Resize Flags**](resize-flags.md) for possible values.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the output type has not been set, the filter should return default values. These values can be arbitrarily chosen at design time.

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

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IResize Interface**](iresize.md)
</dt> </dl>

 

 




