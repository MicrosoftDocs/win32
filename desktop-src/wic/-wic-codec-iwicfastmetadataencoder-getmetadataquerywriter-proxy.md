---
Description: 'Proxy function for the GetMetadataQueryWriter method.'
ms.assetid: '64d2c6d8-f1dd-4397-8487-4d23c69aea82'
title: 'IWICFastMetadataEncoder\_GetMetadataQueryWriter\_Proxy function'
---

# IWICFastMetadataEncoder\_GetMetadataQueryWriter\_Proxy function

Proxy function for the [**GetMetadataQueryWriter**](-wic-codec-iwicfastmetadataencoder-getmetadataquerywriter.md) method.

## Syntax


```C++
HRESULT IWICFastMetadataEncoder_GetMetadataQueryWriter_Proxy(
  _In_  IWICBitmapFrameDecode   *THIS_PTR,
  _Out_ IWICMetadataQueryWriter **ppIMetadataQueryWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)\***

Pointer to this [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) object.

</dd> <dt>

*ppIMetadataQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md)\*\***

A pointer that receives a pointer to the encoder's metadata query writer.

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



 

 




