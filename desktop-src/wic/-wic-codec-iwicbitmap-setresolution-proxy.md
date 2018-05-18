---
Description: 'Proxy function for the SetResolution method.'
ms.assetid: 'c4e3927c-6f9d-401d-acd7-711674cdbb53'
title: 'IWICBitmap\_SetResolution\_Proxy function'
---

# IWICBitmap\_SetResolution\_Proxy function

Proxy function for the [**SetResolution**](-wic-codec-iwicbitmap-setresolution.md) method.

## Syntax


```C++
HRESULT IWICBitmap_SetResolution_Proxy(
  _In_ IWICBitmap *THIS_PTR,
  _In_ double     dpiX,
  _In_ double     dpiY
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmap**](-wic-codec-iwicbitmap.md)\***

Pointer to this [**IWICBitmap**](-wic-codec-iwicbitmap.md) object.

</dd> <dt>

*dpiX* \[in\]
</dt> <dd>

Type: **double**

The horizontal resolution.

</dd> <dt>

*dpiY* \[in\]
</dt> <dd>

Type: **double**

The vertical resolution.

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



 

 




