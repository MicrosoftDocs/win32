---
Description: 'Proxy function for the SetPalette method.'
ms.assetid: 'd8e2c36e-6886-4959-b2a2-469bebfe1cdc'
title: 'IWICBitmapEncoder\_SetPalette\_Proxy function'
---

# IWICBitmapEncoder\_SetPalette\_Proxy function

Proxy function for the [**SetPalette**](-wic-codec-iwicbitmapencoder-setpalette.md) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_SetPalette_Proxy(
  _In_ IWICBitmapEncoder *THIS_PTR,
  _In_ IWICPalette       *pIPalette
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)\***

Pointer to this [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) object.

</dd> <dt>

*pIPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

The [**IWICPalette**](-wic-codec-iwicpalette.md) to use as the global palette.

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



 

 




