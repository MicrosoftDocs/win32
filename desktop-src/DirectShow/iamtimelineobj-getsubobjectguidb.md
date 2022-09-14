---
description: The GetSubObjectGUIDB method retrieves the GUID of the subobject associated with this timeline object. This method is equivalent to IAMTimelineObj::GetSubObjectGUID, but receives a BSTR value.
ms.assetid: 693cafda-78c8-4ba4-90d7-23fedcd1fc52
title: IAMTimelineObj::GetSubObjectGUIDB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.GetSubObjectGUIDB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::GetSubObjectGUIDB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSubObjectGUIDB` method retrieves the GUID of the subobject associated with this timeline object. This method is equivalent to [**IAMTimelineObj::GetSubObjectGUID**](iamtimelineobj-getsubobjectguid.md), but receives a **BSTR** value.

## Syntax


```C++
HRESULT GetSubObjectGUIDB(
  [out, retval] BSTR *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives a string representing the subobject GUID.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

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

 

 




