---
Description: The GetSubObjectGUID method retrieves the GUID of the subobject associated with this timeline object.
ms.assetid: c2787e6b-ed72-4a6c-9e1e-c79c00020585
title: IAMTimelineObj::GetSubObjectGUID method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAMTimelineObj::GetSubObjectGUID method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSubObjectGUID` method retrieves the GUID of the subobject associated with this timeline object.

## Syntax


```C++
HRESULT GetSubObjectGUID(
   GUID *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives the GUID of the subobject, or GUID\_NULL if the object does not have a subobject.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




