---
Description: 'Proxy function for the GetBitsPerPixel method.'
ms.assetid: 'bb98daeb-3886-473b-9c8e-5c606602249a'
title: 'IWICPixelFormatInfo\_GetBitsPerPixel\_Proxy function'
---

# IWICPixelFormatInfo\_GetBitsPerPixel\_Proxy function

Proxy function for the [**GetBitsPerPixel**](-wic-codec-iwicpixelformatinfo-getbitsperpixel.md) method.

## Syntax


```C++
HRESULT IWICPixelFormatInfo_GetBitsPerPixel_Proxy(
  _In_  IWICPixelFormatInfo *THIS_PTR,
  _Out_ UINT                *puiBitsPerPixel
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPixelFormatInfo**](-wic-codec-iwicpixelformatinfo.md)\***

Pointer to this [**IWICPixelFormatInfo**](-wic-codec-iwicpixelformatinfo.md) object.

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



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




