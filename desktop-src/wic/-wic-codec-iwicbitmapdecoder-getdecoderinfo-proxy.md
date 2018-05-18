---
Description: 'Proxy function for the GetDecoderInfo method.'
ms.assetid: '4117492e-d652-4c72-9979-cc4e554a6fd8'
title: 'IWICBitmapDecoder\_GetDecoderInfo\_Proxy function'
---

# IWICBitmapDecoder\_GetDecoderInfo\_Proxy function

Proxy function for the [**GetDecoderInfo**](-wic-codec-iwicbitmapdecoder-getdecoderinfo.md) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetDecoderInfo_Proxy(
  _In_  IWICBitmapDecoder     *THIS_PTR,
  _Out_ IWICBitmapDecoderInfo **ppIDecoderInfo
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

Pointer to this [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) object.

</dd> <dt>

*ppIDecoderInfo* \[out\]
</dt> <dd>

Type: **[**IWICBitmapDecoderInfo**](-wic-codec-iwicbitmapdecoderinfo.md)\*\***

A pointer that receives a pointer to an [**IWICBitmapDecoderInfo**](-wic-codec-iwicbitmapdecoderinfo.md).

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



 

 




