---
Description: Proxy function for the CreateBitmapScaler method.
ms.assetid: 27fcb17e-bdcd-44cc-9fe6-f93816589b50
title: IWICImagingFactory\_CreateBitmapScaler\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateBitmapScaler\_Proxy function

Proxy function for the [**CreateBitmapScaler**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createbitmapscaler?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapScaler_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICBitmapScaler   **ppIBitmapScaler
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*ppIBitmapScaler* \[out\]
</dt> <dd>

Type: **[**IWICBitmapScaler**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapscaler?branch=master)\*\***

A pointer that receives a pointer to a new [**IWICBitmapScaler**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapscaler?branch=master).

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



 

 




