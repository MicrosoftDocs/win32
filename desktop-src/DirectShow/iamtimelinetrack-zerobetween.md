---
description: The ZeroBetween method removes everything from the track between the specified times. This method splits any objects that span the specified time range and removes the pieces that fall within the range.
ms.assetid: df173a3c-147b-4f2d-9bcb-a8c2873f5420
title: IAMTimelineTrack::ZeroBetween method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.ZeroBetween
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::ZeroBetween method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ZeroBetween` method removes everything from the track between the specified times. This method splits any objects that span the specified time range and removes the pieces that fall within the range.

## Syntax


```C++
HRESULT ZeroBetween(
   REFERENCE_TIME rtStart,
   REFERENCE_TIME rtEnd
);
```



## Parameters

<dl> <dt>

*rtStart* 
</dt> <dd>

Beginning of the range to clear, in 100-nanosecond units.

</dd> <dt>

*rtEnd* 
</dt> <dd>

End of the range to clear, in 100-nanosecond units.

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

 

 




