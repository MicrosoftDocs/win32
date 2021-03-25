---
description: The ZeroBetween2 method removes everything from the track between the specified times. This method is equivalent to IAMTimelineTrack::ZeroBetween, but takes REFTIME values.
ms.assetid: 56b9be30-cc3f-4843-bf35-910498242d71
title: IAMTimelineTrack::ZeroBetween2 method (Qedit.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.ZeroBetween2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::ZeroBetween2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ZeroBetween2` method removes everything from the track between the specified times. This method is equivalent to [**IAMTimelineTrack::ZeroBetween**](iamtimelinetrack-zerobetween.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT ZeroBetween2(
   REFTIME rtStart,
   REFTIME rtEnd
);
```



## Parameters

<dl> <dt>

*rtStart* 
</dt> <dd>

Beginning of the range to clear, in seconds.

</dd> <dt>

*rtEnd* 
</dt> <dd>

End of the range to clear, in seconds.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                             | Description                                                     |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The time range falls beyond everything in the track.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                             |



 

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

 

 




