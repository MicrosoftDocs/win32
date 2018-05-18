---
Description: 'Proxy function for the DoesSupportLossless method.'
ms.assetid: 'c88d7971-cc93-458c-a31e-19a8b8350d09'
title: 'IWICBitmapCodecInfo\_DoesSupportLossless\_Proxy function'
---

# IWICBitmapCodecInfo\_DoesSupportLossless\_Proxy function

Proxy function for the [**DoesSupportLossless**](-wic-codec-iwicbitmapcodecinfo-doessupportlossless.md) method.

## Syntax


```C++
HRESULT IWICBitmapCodecInfo_DoesSupportLossless_Proxy(
  _In_  IWICBitmapCodecInfo *THIS_PTR,
  _Out_ BOOL                *pfSupportLossless
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapCodecInfo**](-wic-codec-iwicbitmapcodecinfo.md)\***

Pointer to this [**IWICBitmapCodecInfo**](-wic-codec-iwicbitmapcodecinfo.md) object.

</dd> <dt>

*pfSupportLossless* \[out\]
</dt> <dd>

Type: **BOOL\***

A pointer that receives **TRUE** if the codec supports lossless formats; otherwise, **FALSE**.

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



 

 




