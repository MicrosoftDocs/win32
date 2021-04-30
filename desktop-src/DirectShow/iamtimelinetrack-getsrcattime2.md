---
description: The GetSrcAtTime2 method retrieves the source object nearest to the specified time, according to the specified boundary conditions. This method is equivalent to IAMTimelineTrack::GetSrcAtTime, but takes a REFTIME value.
ms.assetid: 11f6545b-478b-4ffd-8344-2bf8585db2a5
title: IAMTimelineTrack::GetSrcAtTime2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.GetSrcAtTime2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::GetSrcAtTime2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSrcAtTime2` method retrieves the source object nearest to the specified time, according to the specified boundary conditions. This method is equivalent to [**IAMTimelineTrack::GetSrcAtTime**](iamtimelinetrack-getsrcattime.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT GetSrcAtTime2(
  [out] IAMTimelineObj **ppSrc,
        REFTIME        Time,
        long           SearchDirection
);
```



## Parameters

<dl> <dt>

*ppSrc* \[out\]
</dt> <dd>

Receives a pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the source object.

</dd> <dt>

*Time* 
</dt> <dd>

Start time for the search, in seconds.

</dd> <dt>

*SearchDirection* 
</dt> <dd>

Member of the [**DEXTERF\_TRACK\_SEARCH\_FLAGS**](dexterf-track-search-flags.md) enumerated type that specifies the boundary conditions for the search.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                  | Description                                |
|----------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Did not locate a source object.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>         | Located a source object.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/>               |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/>      |



 

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

 

 




