---
Description: Proxy function for the CreateBitmapFlipRotator method.
ms.assetid: 1dc55744-8ae1-4d8b-9ffd-735ee45ceb47
title: IWICImagingFactory\_CreateBitmapFlipRotator\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateBitmapFlipRotator\_Proxy function

Proxy function for the [**CreateBitmapFlipRotator**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createbitmapfliprotator?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmapFlipRotator_Proxy(
  _In_  IWICImagingFactory    *pFactory,
  _Out_ IWICBitmapFlipRotator **ppIBitmapFlipRotator
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*ppIBitmapFlipRotator* \[out\]
</dt> <dd>

Type: **[**IWICBitmapFlipRotator**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapfliprotator?branch=master)\*\***

A pointer that receives a pointer to a new [**IWICBitmapFlipRotator**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapfliprotator?branch=master).

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



 

 




