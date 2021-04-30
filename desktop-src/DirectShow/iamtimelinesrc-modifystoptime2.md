---
description: The ModifyStopTime2 method sets the stop time. This method is equivalent to IAMTimelineSrc::ModifyStopTime, but takes a REFTIME value.
ms.assetid: 8bebda47-3e52-42a2-870c-acc14561fa25
title: IAMTimelineSrc::ModifyStopTime2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.ModifyStopTime2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::ModifyStopTime2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ModifyStopTime2` method sets the stop time. This method is equivalent to [**IAMTimelineSrc::ModifyStopTime**](iamtimelinesrc-modifystoptime.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT ModifyStopTime2(
   REFTIME Stop
);
```



## Parameters

<dl> <dt>

*Stop* 
</dt> <dd>

New stop time, in seconds.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_INVALIDARG if the specified time is not valid.

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




