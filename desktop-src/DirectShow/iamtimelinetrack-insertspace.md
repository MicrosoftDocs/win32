---
description: The InsertSpace method splits any objects that exist at the specified time and inserts space between them.
ms.assetid: f9e48f58-1867-405c-b208-1ab781912aa1
title: IAMTimelineTrack::InsertSpace method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.InsertSpace
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrack::InsertSpace method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `InsertSpace` method splits any objects that exist at the specified time and inserts space between them.

## Syntax


```C++
HRESULT InsertSpace(
   REFERENCE_TIME rtStart,
   REFERENCE_TIME rtEnd
);
```



## Parameters

<dl> <dt>

*rtStart* 
</dt> <dd>

Time at which to create the split, and the starting point of the inserted space, in 100-nanosecond units.

</dd> <dt>

*rtEnd* 
</dt> <dd>

End point of the inserted space, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible return values include the following:



| Return code                                                                                   | Description                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>       | There are no objects at the specified time.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid argument.<br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>                        |



 

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

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




