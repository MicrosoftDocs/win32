---
Description: Proxy function for the GetMetadataQueryWriter method.
ms.assetid: 64d2c6d8-f1dd-4397-8487-4d23c69aea82
title: IWICFastMetadataEncoder\_GetMetadataQueryWriter\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICFastMetadataEncoder\_GetMetadataQueryWriter\_Proxy function

Proxy function for the [**GetMetadataQueryWriter**](/windows/win32/Wincodec/nf-wincodec-iwicfastmetadataencoder-getmetadataquerywriter?branch=master) method.

## Syntax


```C++
HRESULT IWICFastMetadataEncoder_GetMetadataQueryWriter_Proxy(
  _In_  IWICBitmapFrameDecode   *THIS_PTR,
  _Out_ IWICMetadataQueryWriter **ppIMetadataQueryWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)\***

Pointer to this [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) object.

</dd> <dt>

*ppIMetadataQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master)\*\***

A pointer that receives a pointer to the encoder's metadata query writer.

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



 

 




