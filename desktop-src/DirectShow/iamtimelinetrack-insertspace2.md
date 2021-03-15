---
description: The InsertSpace2 method splits any objects that exist at the specified time and inserts space between them. This method is equivalent to IAMTimelineTrack::InsertSpace, but takes REFTIME values.
ms.assetid: 818a1dad-0c8d-4728-82d6-cd52c6c830a2
title: IAMTimelineTrack::InsertSpace2 method (Qedit.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.InsertSpace2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::InsertSpace2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `InsertSpace2` method splits any objects that exist at the specified time and inserts space between them. This method is equivalent to [**IAMTimelineTrack::InsertSpace**](iamtimelinetrack-insertspace.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT InsertSpace2(
   REFTIME rtStart,
   REFTIME rtEnd
);
```



## Parameters

<dl> <dt>

*rtStart* 
</dt> <dd>

Time at which to create the split, and the starting point of the inserted space, in seconds.

</dd> <dt>

*rtEnd* 
</dt> <dd>

End point of the inserted space, in seconds.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible return values include the following:



| Return code                                                                                   | Description                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>       | There are no objects at the specified time.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid argument.<br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>                        |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




