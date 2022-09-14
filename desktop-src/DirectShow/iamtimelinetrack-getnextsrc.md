---
description: The GetNextSrc method searches the track for the next source that appears at the specified time or later.
ms.assetid: e87d8978-7b45-41a3-a74d-b5dd231d1d85
title: IAMTimelineTrack::GetNextSrc method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.GetNextSrc
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::GetNextSrc method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextSrc` method searches the track for the next source that appears at the specified time or later.

## Syntax


```C++
HRESULT GetNextSrc(
  [out] IAMTimelineObj **ppSrc,
        REFERENCE_TIME *pInOut
);
```



## Parameters

<dl> <dt>

*ppSrc* \[out\]
</dt> <dd>

Receives a pointer to the source object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*pInOut* 
</dt> <dd>

Pointer to a variable that contains the start time for the search, in 100-nanosecond units. If the method retrieves a source, it sets the value to the stop time of the source. If the method does not retrieve a source, the value becomes invalid and the application should not use it.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a source, or S\_FALSE otherwise.

## Remarks

If the time specified by *pInOut* falls between the start and stop times of a source, the method retrieves that source.

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

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




