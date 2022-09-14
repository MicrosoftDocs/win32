---
description: Proxy function for the InitializePredefined method.
ms.assetid: 78137d43-c32f-4d60-b289-2e2154cf4d1e
title: IWICPalette_InitializePredefined_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICPalette_InitializePredefined_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICPalette\_InitializePredefined\_Proxy function

Proxy function for the [**InitializePredefined**](/windows/desktop/api/Wincodec/nf-wincodec-iwicpalette-initializepredefined) method.

## Syntax


```C++
HRESULT IWICPalette_InitializePredefined_Proxy(
  _In_ IWICPalette          *THIS_PTR,
  _In_ WICBitmapPaletteType ePaletteType,
  _In_ BOOL                 fAddTransparentColor
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpalette)\***

Pointer to this [**IWICPalette**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpalette) object.

</dd> <dt>

*ePaletteType* \[in\]
</dt> <dd>

Type: **[**WICBitmapPaletteType**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmappalettetype)**

The desired pre-defined palette type.

</dd> <dt>

*fAddTransparentColor* \[in\]
</dt> <dd>

Type: **BOOL**

The optional tranparent color to add to the palette. If no transparent color is needed, use 0.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




