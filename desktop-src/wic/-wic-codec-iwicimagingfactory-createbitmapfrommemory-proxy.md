---
Description: Proxy function for the CreateBitmapFromMemory method.
ms.assetid: 5aa455d5-23e3-4738-b028-b84da0fb0c50
title: IWICImagingFactory\_CreateBitmapFromMemory\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateBitmapFromMemory\_Proxy function

Proxy function for the [**CreateBitmapFromMemory**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createbitmapfrommemory?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapFromMemory_Proxy(
  _In_  IWICImagingFactory    *pFactory,
  _In_  UINT                  uiWidth,
  _In_  UINT                  uiHeight,
  _In_  REFWICPixelFormatGUID pixelFormat,
  _In_  UINT                  cbStride,
  _In_  UINT                  cbBufferSize,
  _In_  BYTE                  *pbBuffer,
  _Out_ IWICBitmap            **ppIBitmap
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*uiWidth* \[in\]
</dt> <dd>

Type: **UINT**

The width of the new bitmap.

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

*cbStride* \[in\]
</dt> <dd>

Type: **UINT**

The [*stride*](#term-stride) of the given pixel data.

</dd> <dt>

*cbBufferSize* \[in\]
</dt> <dd>

Type: **UINT**

The size of *pbBuffer*.

</dd> <dt>

*pbBuffer* \[in\]
</dt> <dd>

Type: **BYTE\***

The buffer used to create the bitmap.

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



 

 




