---
description: Proxy function for the CreateBitmap method.
ms.assetid: 5647521b-231d-4819-97ab-4dfb5f796211
title: IWICImagingFactory_CreateBitmap_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICImagingFactory_CreateBitmap_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICImagingFactory\_CreateBitmap\_Proxy function

Proxy function for the [**CreateBitmap**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createbitmap) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmap_Proxy(
  _In_  IWICImagingFactory         *pFactory,
  _In_  UINT                       uiWidth,
  _In_  UINT                       uiHeight,
  _In_  REFWICPixelFormatGUID      pixelFormat,
  _In_  WICBitmapCreateCacheOption option,
  _Out_ IWICBitmap                 **ppIBitmap
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)\***

</dd> <dt>

*uiWidth* \[in\]
</dt> <dd>

Type: **UINT**

The width of the new bitmap .

</dd> <dt>

*uiHeight* \[in\]
</dt> <dd>

Type: **UINT**

The height of the new bitmap.

</dd> <dt>

*pixelFormat* \[in\]
</dt> <dd>

Type: **REFWICPixelFormatGUID**

The pixel format of the new bitmap.

</dd> <dt>

*option* \[in\]
</dt> <dd>

Type: **[**WICBitmapCreateCacheOption**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmapcreatecacheoption)**

The cache creation options of the new bitmap.

</dd> <dt>

*ppIBitmap* \[out\]
</dt> <dd>

Type: **[**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap)\*\***

A pointer that receives a pointer to the new bitmap.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




