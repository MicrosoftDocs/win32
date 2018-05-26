---
Description: Proxy function for the GetMetadataQueryReader method.
ms.assetid: cc32bdf1-d807-46ac-87b7-77bf2d498e72
title: IWICBitmapDecoder\_GetMetadataQueryReader\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapDecoder\_GetMetadataQueryReader\_Proxy function

Proxy function for the [**GetMetadataQueryReader**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getmetadataqueryreader?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetMetadataQueryReader_Proxy(
  _In_  IWICBitmapDecoder       *THIS_PTR,
  _Out_ IWICMetadataQueryReader **ppIMetadataQueryReader
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)\***

Pointer to this [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) object.

</dd> <dt>

*ppIMetadataQueryReader* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master)\*\***

A pointer that receives a pointer to the metadata.

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



 

 




