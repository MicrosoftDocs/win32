---
Description: Initializes an IWICColorTransform with a IWICBitmapSource and transforms it from one IWICColorContext to another.
ms.assetid: 68C8EF36-DFFF-4FF3-BD9A-583508F9C2B1
title: IWICColorTransform\_Initialize\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICColorTransform\_Initialize\_Proxy function

Initializes an [**IWICColorTransform**](/windows/win32/Wincodec/nn-wincodec-iwiccolortransform?branch=master) with a [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) and transforms it from one [**IWICColorContext**](/windows/win32/Wincodec/nn-wincodec-iwiccolorcontext?branch=master) to another.

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

Type: **[**IWICColorTransform**](/windows/win32/Wincodec/nn-wincodec-iwiccolortransform?branch=master)\***

The color transform to initialize.

</dd> <dt>

*pIBitmapSource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

The bitmap source used to initialize the color transform.

</dd> <dt>

*pIContextSource* \[in\]
</dt> <dd>

Type: **[**IWICColorContext**](/windows/win32/Wincodec/nn-wincodec-iwiccolorcontext?branch=master)\***

The color context source.

</dd> <dt>

*pIContextDest* \[in\]
</dt> <dd>

Type: **[**IWICColorContext**](/windows/win32/Wincodec/nn-wincodec-iwiccolorcontext?branch=master)\***

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



 

 




