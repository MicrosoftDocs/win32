---
description: The get\_ErrorLog method retrieves the current error log for this object.
ms.assetid: 580b8a06-6bf2-49ef-a5fb-5e6df2f09793
title: IAMSetErrorLog::get_ErrorLog method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMSetErrorLog.get_ErrorLog
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMSetErrorLog::get\_ErrorLog method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_ErrorLog` method retrieves the current error log for this object.

## Syntax


```C++
HRESULT get_ErrorLog(
  [out, retval] IAMErrorLog **pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives a pointer to the error log's [**IAMErrorLog**](iamerrorlog.md) interface. If the timeline does not have an error log, the value is set to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the value returned in *pVal* is not **NULL**, the [**IAMErrorLog**](iamerrorlog.md) interface has an outstanding reference count. Be sure to release the interface when you are done using it.

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

 

 




