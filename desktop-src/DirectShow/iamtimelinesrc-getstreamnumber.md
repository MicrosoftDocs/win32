---
description: The GetStreamNumber method retrieves the current stream number for the source object.
ms.assetid: c9c0c9f7-2716-436d-902c-f2255bedaffb
title: IAMTimelineSrc::GetStreamNumber method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetStreamNumber
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::GetStreamNumber method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetStreamNumber` method retrieves the current stream number for the source object.

## Syntax


```C++
HRESULT GetStreamNumber(
   long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives the stream number.

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




