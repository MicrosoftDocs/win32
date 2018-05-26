---
Description: Proxy function for the CreateBitmapClipper method.
ms.assetid: 163a8d7b-f22b-4ab5-9dba-00b0cdaab440
title: IWICImagingFactory\_CreateBitmapClipper\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateBitmapClipper\_Proxy function

Proxy function for the [**CreateBitmapClipper**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createbitmapclipper?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapClipper_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICBitmapClipper  **ppIBitmapClipper
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*ppIBitmapClipper* \[out\]
</dt> <dd>

Type: **[**IWICBitmapClipper**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapclipper?branch=master)\*\***

A pointer that receives a pointer to a new [**IWICBitmapClipper**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapclipper?branch=master).

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



 

 




