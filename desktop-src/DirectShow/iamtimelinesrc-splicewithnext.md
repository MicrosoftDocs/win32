---
description: The SpliceWithNext method joins the source object to another source object.
ms.assetid: 65b23466-404c-4eef-943e-8b40186f2b96
title: IAMTimelineSrc::SpliceWithNext method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SpliceWithNext
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSrc::SpliceWithNext method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SpliceWithNext` method joins the source object to another source object.

## Syntax


```C++
HRESULT SpliceWithNext(
   IAMTimelineObj *pNext
);
```



## Parameters

<dl> <dt>

*pNext* 
</dt> <dd>

Pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the source object to join to the current source.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible return values include the following:



| Return code                                                                                   | Description                                                              |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid argument.<br/>                                             |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | Object specified by *pNext* parameter is not a source object.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/>                                    |



 

## Remarks

As currently implemented, this method discards any effects on *pNext*.

For this method to succeed, *pNext* must be a match frame of the current source object, defined as follows:

-   It must share the same source file.
-   The media start time must equal the media stop time of the current source.
-   The playback rate must be the same. Playback rate is media duration divided by timeline duration.

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




