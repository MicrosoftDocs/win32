---
description: The put\_ErrorLog method specifies an error log for the object.
ms.assetid: 39da3fb0-57d3-452f-b2ae-6dcd84fa5c8e
title: IAMSetErrorLog::put_ErrorLog method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMSetErrorLog.put_ErrorLog
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMSetErrorLog::put\_ErrorLog method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_ErrorLog` method specifies an error log for the object.

## Syntax


```C++
HRESULT put_ErrorLog(
  [in] IAMErrorLog *newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Pointer to the error log's [**IAMErrorLog**](iamerrorlog.md) interface.

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

[**IAMSetErrorLog Interface**](iamseterrorlog.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




