---
Description: 'Proxy function for the Initialize method.'
ms.assetid: '60925f5c-aca4-4f49-96d2-9b58d8310e3c'
title: 'IWICBitmapClipper\_Initialize\_Proxy function'
---

# IWICBitmapClipper\_Initialize\_Proxy function

Proxy function for the [**Initialize**](-wic-codec-iwicbitmapclipper-initialize.md) method.

## Syntax


```C++
HRESULT IWICBitmapClipper_Initialize_Proxy(
  _In_       IWICBitmapClipper *THIS_PTR,
  _In_       IWICBitmapSource  *pISource,
  _In_ const WICRect           *prc
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapClipper**](-wic-codec-iwicbitmapclipper.md)\***

Pointer to this [**IWICBitmapClipper**](-wic-codec-iwicbitmapclipper.md) object.

</dd> <dt>

*pISource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

The input bitmap source.

</dd> <dt>

*prc* \[in\]
</dt> <dd>

Type: **const [**WICRect**](-wic-codec-wicrect.md)\***

The rectangle of the bitmap source to clip.

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



 

 




