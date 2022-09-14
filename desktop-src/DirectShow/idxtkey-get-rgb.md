---
description: The get\_RGB method retrieves the RGB color on which to key. This property applies only when the key type is DXTKEY\_RGB.
ms.assetid: 7b1b22ff-457a-48c8-9221-ca38601874a9
title: IDxtKey::get_RGB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.get_RGB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey::get\_RGB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_RGB` method retrieves the RGB color on which to key. This property applies only when the key type is DXTKEY\_RGB.

## Syntax


```C++
HRESULT get_RGB(
  [out, retval] DWORD *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the color. The returned value is a hexadecimal number with the format 0xRRGGBB, where RR is the red value, GG is the green value, and BB is the blue value.

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

[**IDxtKey Interface**](idxtkey.md)
</dt> <dt>

[**IDxtKey::get\_KeyType**](idxtkey-get-keytype.md)
</dt> </dl>

 

 




