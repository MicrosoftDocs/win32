---
Description: 'Proxy function for the CopyPalette method.'
ms.assetid: '7dfe2367-036c-450a-ad2f-f862b77545a2'
title: 'IWICBitmapSource\_CopyPalette\_Proxy function'
---

# IWICBitmapSource\_CopyPalette\_Proxy function

Proxy function for the [**CopyPalette**](-wic-codec-iwicbitmapsource-copypalette.md) method.

## Syntax


```C++
HRESULT IWICBitmapSource_CopyPalette_Proxy(
  _In_ IWICBitmapSource *THIS_PTR,
  _In_ IWICPalette      *pIPalette
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

Pointer to this [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) object.

</dd> <dt>

*pIPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

The palette.

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



 

 




