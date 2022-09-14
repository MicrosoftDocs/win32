---
description: The SetLocked method sets the object's editing state to locked or unlocked.
ms.assetid: 801b8bf0-5c7a-4122-9038-6b0d8bdc5da3
title: IAMTimelineObj::SetLocked method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetLocked
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetLocked method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetLocked` method sets the object's editing state to locked or unlocked.

A locked state indicates that the object should not be edited; an unlocked state indicates that the object can be edited. The timeline does not enforce the lock. The locked setting exists only for the convenience of the application.

## Syntax


```C++
HRESULT SetLocked(
   BOOL newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

Boolean value that specifies the object's editing state. If **TRUE**, the object is locked and should not be edited. If **FALSE**, the object is unlocked and can be edited.

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




