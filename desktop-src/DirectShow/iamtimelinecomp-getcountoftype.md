---
description: The GetCountOfType method retrieves the number of objects of a given type contained in this composition and all its virtual tracks, recursively.
ms.assetid: 2d14ccf7-77bc-4095-bfb8-12a52b4b9595
title: IAMTimelineComp::GetCountOfType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.GetCountOfType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineComp::GetCountOfType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetCountOfType` method retrieves the number of objects of a given type contained in this composition and all its virtual tracks, recursively.

## Syntax


```C++
HRESULT GetCountOfType(
   long                *pVal,
   long                *pValWithComps,
   TIMELINE_MAJOR_TYPE MajorType
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives the number of objects of the specified type contained in this composition and all its virtual tracks, recursively.

</dd> <dt>

*pValWithComps* 
</dt> <dd>

Receives the count returned in *pVal* plus the number of compositions searched, including this one.

</dd> <dt>

*MajorType* 
</dt> <dd>

Member of the [**TIMELINE\_MAJOR\_TYPE**](timeline-major-type.md) enumerated type, specifying the type of object to count.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_POINTER otherwise.

## Remarks

Typically, an application will not call this method. It is called by the render engine.

If you count compositions, the value returned in *pVal* is zero and the value returned in *pValWithComps* is the number of compositions. The value of *\*pValWithComps* includes the composition on which you call the method. For example, if you call this method on an empty composition, *\*pValWithComps* equals 1.

Groups cannot reside inside compositions, so you cannot use this method to count groups. (The returned count will always be zero.) To count groups, call the [**IAMTimeline::GetGroupCount**](iamtimeline-getgroupcount.md) method.

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

[**IAMTimelineComp Interface**](iamtimelinecomp.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




