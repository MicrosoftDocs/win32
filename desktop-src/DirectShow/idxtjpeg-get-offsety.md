---
description: The get\_OffsetY method retrieves the vertical offset of the wipe origin.
ms.assetid: 0d8b8df2-b916-4143-b1f1-7912ef3fa025
title: IDxtJpeg::get_OffsetY method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg.get_OffsetY
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtJpeg::get\_OffsetY method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_OffsetY` method retrieves the vertical offset of the wipe origin.

## Syntax


```C++
HRESULT get_OffsetY(
  [out, retval] long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the vertical offset of the wipe origin, in pixels. The center of the wipe is offset by this amount.

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

[**IDxtJpeg Interface**](idxtjpeg.md)
</dt> </dl>

 

 




