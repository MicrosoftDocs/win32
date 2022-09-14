---
description: The GetSrcAtTime method retrieves the source object nearest to the specified time, according to the specified boundary conditions.
ms.assetid: 0469c0c2-13df-49f7-95b2-15d3069c5b1c
title: IAMTimelineTrack::GetSrcAtTime method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.GetSrcAtTime
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::GetSrcAtTime method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSrcAtTime` method retrieves the source object nearest to the specified time, according to the specified boundary conditions.

## Syntax


```C++
HRESULT GetSrcAtTime(
  [out] IAMTimelineObj **ppSrc,
        REFERENCE_TIME Time,
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

Start time for the search, in 100-nanosecond units.

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

 

 




