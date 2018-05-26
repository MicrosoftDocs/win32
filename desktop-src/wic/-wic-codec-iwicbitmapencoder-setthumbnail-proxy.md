---
Description: Proxy function for the SetThumbnail method.
ms.assetid: 6c062eaf-27a4-4d48-8315-be9bf168f999
title: IWICBitmapEncoder\_SetThumbnail\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapEncoder\_SetThumbnail\_Proxy function

Proxy function for the [**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_SetThumbnail_Proxy(
  _In_ IWICBitmapEncoder *THIS_PTR,
  _In_ IWICBitmapSource  *pIThumbnail
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)\***

Pointer to this [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master) object.

</dd> <dt>

*pIThumbnail* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

The [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) to set as the global thumbnail.

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



 

 




