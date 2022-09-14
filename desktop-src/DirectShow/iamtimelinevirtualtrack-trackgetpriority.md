---
description: The TrackGetPriority method retrieves the object's priority level.
ms.assetid: f9a138e8-e9ad-4703-bdcc-c64aea4fbad0
title: IAMTimelineVirtualTrack::TrackGetPriority method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineVirtualTrack.TrackGetPriority
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineVirtualTrack::TrackGetPriority method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `TrackGetPriority` method retrieves the object's priority level.

## Syntax


```C++
HRESULT TrackGetPriority(
   long *pPriority
);
```



## Parameters

<dl> <dt>

*pPriority* 
</dt> <dd>

Pointer to a variable that receives the priority level. If the object is not part of a timeline, the value is set to –1.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**IAMTimelineVirtualTrack Interface**](iamtimelinevirtualtrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




