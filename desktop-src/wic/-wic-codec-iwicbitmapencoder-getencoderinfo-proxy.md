---
Description: 'Proxy function for the GetEncoderInfo method.'
ms.assetid: '759965fd-7bc6-4130-b102-b49d1f0d4bf8'
title: 'IWICBitmapEncoder\_GetEncoderInfo\_Proxy function'
---

# IWICBitmapEncoder\_GetEncoderInfo\_Proxy function

Proxy function for the [**GetEncoderInfo**](-wic-codec-iwicbitmapencoder-getencoderinfo.md) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_GetEncoderInfo_Proxy(
  _In_  IWICBitmapEncoder     *THIS_PTR,
  _Out_ IWICBitmapEncoderInfo **ppIEncoderInfo
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)\***

Pointer to this [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) object.

</dd> <dt>

*ppIEncoderInfo* \[out\]
</dt> <dd>

Type: **[**IWICBitmapEncoderInfo**](-wic-codec-iwicbitmapencoderinfo.md)\*\***

A pointer that receives a pointer to an [**IWICBitmapEncoderInfo**](-wic-codec-iwicbitmapencoderinfo.md).

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



 

 




