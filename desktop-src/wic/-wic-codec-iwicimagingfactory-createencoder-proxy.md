---
Description: Proxy function for the CreateEncoder method.
ms.assetid: e3ffad7f-eb0e-481d-81ee-caf18e14ba59
title: IWICImagingFactory\_CreateEncoder\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateEncoder\_Proxy function

Proxy function for the [**CreateEncoder**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createencoder?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateEncoder_Proxy(
  _In_           IWICImagingFactory *pFactory,
  _In_           REFGUID            guidContainerFormat,
  _In_opt_ const GUID               *pguidVendor,
  _Out_          IWICBitmapEncoder  **ppIEncoder
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*guidContainerFormat* \[in\]
</dt> <dd>

Type: **REFGUID**

The GUID for the desired container format.

</dd> <dt>

*pguidVendor* \[in, optional\]
</dt> <dd>

Type: **const GUID\***

The vendor GUID for the encoder.

</dd> <dt>

*ppIEncoder* \[out\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)\*\***

A pointer that receives a pointer to a new [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master).

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



 

 




