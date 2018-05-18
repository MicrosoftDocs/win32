---
Description: 'Proxy function for the InitializeFromBitmap method.'
ms.assetid: '9559a56d-7201-4b39-a3cd-9c0e4eac611a'
title: 'IWICPalette\_InitializeFromBitmap\_Proxy function'
---

# IWICPalette\_InitializeFromBitmap\_Proxy function

Proxy function for the [**InitializeFromBitmap**](-wic-codec-iwicpalette-initializefrombitmap.md) method.

## Syntax


```C++
HRESULT IWICPalette_InitializeFromBitmap_Proxy(
  _In_ IWICPalette      *THIS_PTR,
  _In_ IWICBitmapSource *pISurface,
  _In_ UINT             colorCount,
  _In_ BOOL             fAddTransparentColor
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

Pointer to this [**IWICPalette**](-wic-codec-iwicpalette.md) object.

</dd> <dt>

*pISurface* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

Pointer to the source bitmap.

</dd> <dt>

*colorCount* \[in\]
</dt> <dd>

Type: **UINT**

The number of colors to initialize the palette with.

</dd> <dt>

*fAddTransparentColor* \[in\]
</dt> <dd>

Type: **BOOL**

A value to indicate whether to add a transparent color.

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



 

 




