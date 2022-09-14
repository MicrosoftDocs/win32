---
description: The SplitAt2 method splits the object at the specified time. This method is equivalent to IAMTimelineSplittable::SplitAt, but takes a REFTIME value.
ms.assetid: 33d240db-4ef8-455a-81a6-633ee12837c2
title: IAMTimelineSplittable::SplitAt2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSplittable.SplitAt2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSplittable::SplitAt2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SplitAt2` method splits the object at the specified time. This method is equivalent to [**IAMTimelineSplittable::SplitAt**](iamtimelinesplittable-splitat.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT SplitAt2(
   REFTIME Time
);
```



## Parameters

<dl> <dt>

*Time* 
</dt> <dd>

Time at which to split the object, relative to the start of the timeline, in seconds.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Nothing to split.<br/>                       |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The object does not exist at this time.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>                    |



 

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

[**IAMTimelineSplittable Interface**](iamtimelinesplittable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




