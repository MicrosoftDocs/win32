---
description: The GetTransAtTime method retrieves the transition nearest to the specified time, according to the specified boundary conditions.
ms.assetid: 33b3686b-5a9d-4eb2-bd40-4d6f569e7d89
title: IAMTimelineTransable::GetTransAtTime method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable.GetTransAtTime
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTransable::GetTransAtTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetTransAtTime` method retrieves the transition nearest to the specified time, according to the specified boundary conditions.

## Syntax


```C++
HRESULT GetTransAtTime(
  [out] IAMTimelineObj **ppObj,
        REFERENCE_TIME Time,
        long           SearchDirection
);
```



## Parameters

<dl> <dt>

*ppObj* \[out\]
</dt> <dd>

Receives a pointer to the transition's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*Time* 
</dt> <dd>

Time from which to begin the search, in 100-nanosecond units.

</dd> <dt>

*SearchDirection* 
</dt> <dd>

Member of the [**DEXTERF\_TRACK\_SEARCH\_FLAGS**](dexterf-track-search-flags.md) enumerated type that specifies the boundary conditions for the search.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                  | Description                           |
|----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>      | No transition was found.<br/>   |
| <dl> <dt>**S\_OK**</dt> </dl>         | Transition was found.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/>          |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/> |



 

## Remarks

If the method returns S\_OK, the **IAMTimelineObj** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IAMTimelineTransable Interface**](iamtimelinetransable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




