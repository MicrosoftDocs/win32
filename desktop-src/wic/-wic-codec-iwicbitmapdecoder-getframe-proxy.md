---
Description: 'Proxy function for the GetFrame method.'
ms.assetid: '31612afa-5017-4ddb-bdf8-25555db35da5'
title: 'IWICBitmapDecoder\_GetFrame\_Proxy function'
---

# IWICBitmapDecoder\_GetFrame\_Proxy function

Proxy function for the [**GetFrame**](-wic-codec-iwicbitmapdecoder-getframe.md) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetFrame_Proxy(
  _In_  IWICBitmapDecoder     *THIS_PTR,
  _In_  UINT                  index,
  _Out_ IWICBitmapFrameDecode **ppIBitmapFrame
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

Pointer to this [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) object.

</dd> <dt>

*index* \[in\]
</dt> <dd>

Type: **UINT**

The particular frame to retrieve.

</dd> <dt>

*ppIBitmapFrame* \[out\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)\*\***

A pointer that receives a pointer to the [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md).

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



 

 




