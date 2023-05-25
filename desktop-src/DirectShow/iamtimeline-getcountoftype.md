---
description: The GetCountOfType method retrieves the number of objects of the specified type that are contained in a specified group and all of its children.
ms.assetid: f3571fa5-8020-4079-ab7e-ba9ff280c0c5
title: IAMTimeline::GetCountOfType method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetCountOfType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimeline::GetCountOfType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetCountOfType` method retrieves the number of objects of the specified type that are contained in a specified group and all of its children.

## Syntax


```C++
HRESULT GetCountOfType(
   long                Group,
   long                *pVal,
   long                *pValWithComps,
   TIMELINE_MAJOR_TYPE MajorType
);
```



## Parameters

<dl> <dt>

*Group* 
</dt> <dd>

Index number of the group for which to retrieve the count.

</dd> <dt>

*pVal* 
</dt> <dd>

Receives the number of objects of the specified type contained in the group and all of its virtual tracks, recursively.

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

Returns one of the following **HRESULT** values.



| Return code                                                                                  | Description                           |
|----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid group number.<br/>      |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/> |



 

## Remarks

Calling this method is equivalent to calling [**IAMTimelineComp::GetCountOfType**](iamtimelinecomp-getcountoftype.md) on the specified group. See the Remarks section of that method for more information.

Typically, an application will not call this method. It is called internally by the render engine.

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

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




