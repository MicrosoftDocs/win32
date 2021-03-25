---
description: The TransAdd method adds a transition to the object. An object can have multiple transitions, but they must not overlap in time. Transitions must fall within the time boundaries of the object.
ms.assetid: 2c3f923f-c754-4cc8-82ca-d3979d4bda07
title: IAMTimelineTransable::TransAdd method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable.TransAdd
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTransable::TransAdd method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `TransAdd` method adds a transition to the object. An object can have multiple transitions, but they must not overlap in time. Transitions must fall within the time boundaries of the object.

## Syntax


```C++
HRESULT TransAdd(
   IAMTimelineObj *pTrans
);
```



## Parameters

<dl> <dt>

*pTrans* 
</dt> <dd>

Pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the transition to add.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                   | Description                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Cannot insert the transition.<br/>              |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | *pTrans* is not a pointer to a transition.<br/> |



 

## Remarks

If the transition overlaps an existing transition, the method returns E\_INVALIDARG.

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

[**IAMTimelineTransable Interface**](iamtimelinetransable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




