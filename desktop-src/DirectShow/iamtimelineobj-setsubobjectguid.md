---
description: The SetSubObjectGUID method specifies the GUID of the subobject associated with this object.
ms.assetid: 1f21e242-306e-4b28-8655-511b7db495ab
title: IAMTimelineObj::SetSubObjectGUID method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetSubObjectGUID
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetSubObjectGUID method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetSubObjectGUID` method specifies the GUID of the subobject associated with this object.

## Syntax


```C++
HRESULT SetSubObjectGUID(
   GUID newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

GUID of the subobject.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The render engine creates an instance of the subobject as needed.

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

 

 




