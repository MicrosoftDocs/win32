---
Description: 'Proxy function for the GetType method.'
ms.assetid: '04e71352-4f07-4026-bc32-f6926a58c707'
title: 'IWICPalette\_GetType\_Proxy function'
---

# IWICPalette\_GetType\_Proxy function

Proxy function for the [**GetType**](-wic-codec-iwicpalette-gettype.md) method.

## Syntax


```C++
HRESULT IWICPalette_GetType_Proxy(
  _In_  IWICPalette          *THIS_PTR,
  _Out_ WICBitmapPaletteType *pePaletteType
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

Pointer to this [**IWICPalette**](-wic-codec-iwicpalette.md) object.

</dd> <dt>

*pePaletteType* \[out\]
</dt> <dd>

Type: **[**WICBitmapPaletteType**](-wic-codec-wicbitmappalettetype.md)\***

Pointer that receives the palette type of the bimtap.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




