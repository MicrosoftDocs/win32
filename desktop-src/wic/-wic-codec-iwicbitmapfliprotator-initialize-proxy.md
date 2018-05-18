---
Description: 'Proxy function for the Initialize method.'
ms.assetid: '860e8092-054d-489e-8ca1-fec43a039eca'
title: 'IWICBitmapFlipRotator\_Initialize\_Proxy function'
---

# IWICBitmapFlipRotator\_Initialize\_Proxy function

Proxy function for the [**Initialize**](-wic-codec-iwicbitmapfliprotator-initialize.md) method.

## Syntax


```C++
HRESULT IWICBitmapFlipRotator_Initialize_Proxy(
  _In_ IWICBitmapFlipRotator     *THIS_PTR,
  _In_ IWICBitmapSource          *pISource,
  _In_ WICBitmapTransformOptions options
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md)\***

Pointer to this [**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md) object.

</dd> <dt>

*pISource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

The input bitmap source.

</dd> <dt>

*options* \[in\]
</dt> <dd>

Type: **[**WICBitmapTransformOptions**](-wic-codec-wicbitmaptransformoptions.md)**

The [**WICBitmapTransformOptions**](-wic-codec-wicbitmaptransformoptions.md) to flip or rotate the image.

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



 

 




