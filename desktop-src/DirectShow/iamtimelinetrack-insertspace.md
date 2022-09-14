---
description: The InsertSpace method splits any objects that exist at the specified time and inserts space between them.
ms.assetid: f9e48f58-1867-405c-b208-1ab781912aa1
title: IAMTimelineTrack::InsertSpace method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.InsertSpace
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::InsertSpace method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `InsertSpace` method splits any objects that exist at the specified time and inserts space between them.

## Syntax


```C++
HRESULT InsertSpace(
   REFERENCE_TIME rtStart,
   REFERENCE_TIME rtEnd
);
```



## Parameters

<dl> <dt>

*rtStart* 
</dt> <dd>

Time at which to create the split, and the starting point of the inserted space, in 100-nanosecond units.

</dd> <dt>

*rtEnd* 
</dt> <dd>

End point of the inserted space, in 100-nanosecond units.

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

 

 




