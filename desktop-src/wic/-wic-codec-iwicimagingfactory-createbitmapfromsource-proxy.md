---
Description: Proxy function for the CreateBitmapFromSource method.
ms.assetid: 7d000377-1855-4971-b782-4c0bf7968c5f
title: IWICImagingFactory\_CreateBitmapFromSource\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateBitmapFromSource\_Proxy function

Proxy function for the [**CreateBitmapFromSource**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createbitmapfromsource?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapFromSource_Proxy(
  _In_  IWICImagingFactory         *pFactory,
  _In_  IWICBitmapSource           *pIBitmapSource,
  _In_  WICBitmapCreateCacheOption option,
  _Out_ IWICBitmap                 **ppIBitmap
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*pIBitmapSource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

The [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) to create the bitmap from.

</dd> <dt>

*option* \[in\]
</dt> <dd>

Type: **[**WICBitmapCreateCacheOption**](/windows/win32/Wincodec/ne-wincodec-wicbitmapcreatecacheoption?branch=master)**

The cache options of the new bitmap.

</dd> <dt>

*ppIBitmap* \[out\]
</dt> <dd>

Type: **[**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master)\*\***

A pointer that receives a pointer to the new bitmap.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




