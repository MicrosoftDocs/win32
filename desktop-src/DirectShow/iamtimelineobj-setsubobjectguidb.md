---
description: The SetSubObjectGUIDB method specifies the GUID of the subobject associated with this object. This method is equivalent to IAMTimelineObj::SetSubObjectGUID but takes a BSTR value.
ms.assetid: b2523b17-1df3-4be5-8bbb-6b67815f9349
title: IAMTimelineObj::SetSubObjectGUIDB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetSubObjectGUIDB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetSubObjectGUIDB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetSubObjectGUIDB` method specifies the GUID of the subobject associated with this object. This method is equivalent to [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) but takes a **BSTR** value.

## Syntax


```C++
HRESULT SetSubObjectGUIDB(
   BSTR newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

**BSTR** representing the GUID of the subobject.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

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

 

 




