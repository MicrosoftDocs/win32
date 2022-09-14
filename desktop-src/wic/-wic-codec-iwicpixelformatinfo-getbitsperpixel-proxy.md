---
description: Proxy function for the GetBitsPerPixel method.
ms.assetid: bb98daeb-3886-473b-9c8e-5c606602249a
title: IWICPixelFormatInfo_GetBitsPerPixel_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICPixelFormatInfo_GetBitsPerPixel_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICPixelFormatInfo\_GetBitsPerPixel\_Proxy function

Proxy function for the [**GetBitsPerPixel**](/windows/desktop/api/Wincodec/nf-wincodec-iwicpixelformatinfo-getbitsperpixel) method.

## Syntax


```C++
HRESULT IWICPixelFormatInfo_GetBitsPerPixel_Proxy(
  _In_  IWICPixelFormatInfo *THIS_PTR,
  _Out_ UINT                *puiBitsPerPixel
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPixelFormatInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpixelformatinfo)\***

Pointer to this [**IWICPixelFormatInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpixelformatinfo) object.

</dd> <dt>

*puiBitsPerPixel* \[out\]
</dt> <dd>

Type: **UINT\***

Pointer that receives the BPP of the pixel format.

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



 

 




