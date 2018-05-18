---
Description: 'Proxy function for the CreateBitmapClipper method.'
ms.assetid: '163a8d7b-f22b-4ab5-9dba-00b0cdaab440'
title: 'IWICImagingFactory\_CreateBitmapClipper\_Proxy function'
---

# IWICImagingFactory\_CreateBitmapClipper\_Proxy function

Proxy function for the [**CreateBitmapClipper**](-wic-codec-iwicimagingfactory-createbitmapclipper.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapClipper_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICBitmapClipper  **ppIBitmapClipper
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*ppIBitmapClipper* \[out\]
</dt> <dd>

Type: **[**IWICBitmapClipper**](-wic-codec-iwicbitmapclipper.md)\*\***

A pointer that receives a pointer to a new [**IWICBitmapClipper**](-wic-codec-iwicbitmapclipper.md).

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



 

 




