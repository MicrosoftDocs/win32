---
description: The GetNextTrans method retrieves the first transition that appears at the specified time or later.
ms.assetid: 40598d8d-ce74-4a6f-83d0-ea409b0a858c
title: IAMTimelineTransable::GetNextTrans method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable.GetNextTrans
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTransable::GetNextTrans method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextTrans` method retrieves the first transition that appears at the specified time or later.

## Syntax


```C++
HRESULT GetNextTrans(
  [out] IAMTimelineObj **ppTrans,
        REFERENCE_TIME *pInOut
);
```



## Parameters

<dl> <dt>

*ppTrans* \[out\]
</dt> <dd>

Receives a pointer to the transition object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*pInOut* 
</dt> <dd>

Pointer to a variable that specifies the time in 100-nanosecond units. On input, this value specifies the time from which to find the transition. On output, if a transition is retrieved, this value is set to the stop time of the transition.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a transition, or S\_FALSE if it does not find a transition. Otherwise, returns an **HRESULT** value indicating the cause of the failure.

## Remarks

The start time of the transition might be less than the time that you specify in *pInOut*, if the transition spans the specified time.

If the method returns S\_OK, the [**IAMTimelineObj**](iamtimelineobj.md) interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

 

 




