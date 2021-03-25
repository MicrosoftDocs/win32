---
description: The put\_AlphaRamp method specifies the alpha ramp property. The alpha ramp is the percentage by which the alpha values in the original image are adjusted. For example, if the alpha ramp is 0.5, the alpha values in the image are reduced 50%.
ms.assetid: 19ea5828-54fc-43a1-be7c-f6c12cf84648
title: IDxtAlphaSetter::put_AlphaRamp method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtAlphaSetter.put_AlphaRamp
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtAlphaSetter::put\_AlphaRamp method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_AlphaRamp` method specifies the alpha ramp property. The alpha ramp is the percentage by which the alpha values in the original image are adjusted. For example, if the alpha ramp is 0.5, the alpha values in the image are reduced 50%.

## Syntax


```C++
HRESULT put_AlphaRamp(
  [in] double Alpha
);
```



## Parameters

<dl> <dt>

*Alpha* \[in\]
</dt> <dd>

The alpha ramp as a percentage. For example, 1.0 is 100%. To disable this property, set a negative value.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If you set this property to a non-negative value, you must also disable the alpha property, by calling **put\_Alpha** with a negative value. Otherwise the effect will not render correctly.

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

[**IDxtAlphaSetter Interface**](idxtalphasetter.md)
</dt> <dt>

[**IDxtAlphaSetter::put\_Alpha**](idxtalphasetter-put-alpha.md)
</dt> </dl>

 

 




