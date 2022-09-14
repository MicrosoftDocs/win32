---
description: The SetUserID method sets an application-defined identifier for the object.
ms.assetid: 102fe29e-dc2c-4377-bce3-ba3c61dcb355
title: IAMTimelineObj::SetUserID method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetUserID
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetUserID method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetUserID` method sets an application-defined identifier for the object.

## Syntax


```C++
HRESULT SetUserID(
   long newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

Value that specifies the identifier. This identifier is used only by the application and can be any value.

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

 

 




