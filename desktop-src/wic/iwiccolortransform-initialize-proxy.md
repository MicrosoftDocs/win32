---
Description: 'Initializes an IWICColorTransform with a IWICBitmapSource and transforms it from one IWICColorContext to another.'
ms.assetid: '68C8EF36-DFFF-4FF3-BD9A-583508F9C2B1'
title: 'IWICColorTransform\_Initialize\_Proxy function'
---

# IWICColorTransform\_Initialize\_Proxy function

Initializes an [**IWICColorTransform**](-wic-codec-iwiccolortransform.md) with a [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) and transforms it from one [**IWICColorContext**](-wic-codec-iwiccolorcontext.md) to another.

## Syntax


```C++
HRESULT IWICColorTransform_Initialize_Proxy(
  _In_ IWICColorTransform    *pIColorTransform,
  _In_ IWICBitmapSource      *pIBitmapSource,
  _In_ IWICColorContext      *pIContextSource,
  _In_ IWICColorContext      *pIContextDest,
  _In_ REFWICPixelFormatGUID pixelFmtDest
);
```



## Parameters

<dl> <dt>

*pIColorTransform* \[in\]
</dt> <dd>

Type: **[**IWICColorTransform**](-wic-codec-iwiccolortransform.md)\***

The color transform to initialize.

</dd> <dt>

*pIBitmapSource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

The bitmap source used to initialize the color transform.

</dd> <dt>

*pIContextSource* \[in\]
</dt> <dd>

Type: **[**IWICColorContext**](-wic-codec-iwiccolorcontext.md)\***

The color context source.

</dd> <dt>

*pIContextDest* \[in\]
</dt> <dd>

Type: **[**IWICColorContext**](-wic-codec-iwiccolorcontext.md)\***

The color context destination.

</dd> <dt>

*pixelFmtDest* \[in\]
</dt> <dd>

Type: **REFWICPixelFormatGUID**

The GUID of the desired pixel format.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                |                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>WindowsCodecsExt.dll</dt> </dl> |



 

 




