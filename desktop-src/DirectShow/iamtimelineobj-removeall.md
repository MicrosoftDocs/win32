---
description: The RemoveAll method permanently removes this object from the timeline, including subobjects and children.
ms.assetid: 9596cf47-63fe-4839-a6d5-3685fc91a935
title: IAMTimelineObj::RemoveAll method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.RemoveAll
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::RemoveAll method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `RemoveAll` method permanently removes this object from the timeline, including subobjects and children.

## Syntax


```C++
HRESULT RemoveAll();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

To remove an object for the purpose of reinserting it elsewhere in the timeline, call [**IAMTimelineObj::Remove**](iamtimelineobj-remove.md).

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

 

 




