---
Description: Proxy function for the GetMetadataQueryReader method.
ms.assetid: 2a3e0a59-3524-4da4-993a-607a3727faba
title: IWICBitmapFrameDecode\_GetMetadataQueryReader\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapFrameDecode\_GetMetadataQueryReader\_Proxy function

Proxy function for the [**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframedecode-getmetadataqueryreader?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapFrameDecode_GetMetadataQueryReader_Proxy(
  _In_  IWICBitmapFrameDecode   *THIS_PTR,
  _Out_ IWICMetadataQueryReader **ppIMetadataQueryReader
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)\***

Pointer to this [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) object.

</dd> <dt>

*ppIMetadataQueryReader* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master)\*\***

A pointer that receives a pointer to an [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master).

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



 

 




