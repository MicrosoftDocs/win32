---
description: The put\_RGB method specifies the RGB color on which to key. This property applies only when the key type is DXTKEY\_RGB.
ms.assetid: 7a0b794e-bea6-4061-98a0-3f70521e89a3
title: IDxtKey::put_RGB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.put_RGB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey::put\_RGB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_RGB` method specifies the RGB color on which to key. This property applies only when the key type is DXTKEY\_RGB.

## Syntax


```C++
HRESULT put_RGB(
  [in] DWORD newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Specifies the color as a hexadecimal number with the format 0xRRGGBB, where RR is the red value, GG is the green value, and BB is the blue value.

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

[**IDxtKey::put\_KeyType**](idxtkey-put-keytype.md)
</dt> </dl>

 

 




