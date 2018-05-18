---
Description: 'Proxy function for the Initialize method.'
ms.assetid: '0db79eb4-dcb2-491a-9bea-a0dec418f80f'
title: 'IWICBitmapEncoder\_Initialize\_Proxy function'
---

# IWICBitmapEncoder\_Initialize\_Proxy function

Proxy function for the [**Initialize**](-wic-codec-iwicbitmapencoder-initialize.md) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_Initialize_Proxy(
  _In_ IWICBitmapEncoder           *THIS_PTR,
  _In_ IStream                     *pIStream,
  _In_ WICBitmapEncoderCacheOption cacheOption
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)\***

Pointer to this [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) object.

</dd> <dt>

*pIStream* \[in\]
</dt> <dd>

Type: **[IStream](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

The output stream.

</dd> <dt>

*cacheOption* \[in\]
</dt> <dd>

Type: **[**WICBitmapEncoderCacheOption**](-wic-codec-wicbitmapencodercacheoption.md)**

The [**WICBitmapEncoderCacheOption**](-wic-codec-wicbitmapencodercacheoption.md) used on initialization.

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



 

 




