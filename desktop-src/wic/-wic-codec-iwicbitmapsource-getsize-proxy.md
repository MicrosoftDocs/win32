---
Description: Proxy function for the GetSize method.
ms.assetid: a9b7d01c-78d9-47b8-a373-a7c49f7bccfd
title: IWICBitmapSource\_GetSize\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapSource\_GetSize\_Proxy function

Proxy function for the [**GetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-getsize?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapSource_GetSize_Proxy(
  _In_  IWICBitmapSource *THIS_PTR,
  _Out_ UINT             *puiWidth,
  _Out_ UINT             *puiHeight
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

Pointer to this [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) object.

</dd> <dt>

*puiWidth* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the pixel width of the bitmap.

</dd> <dt>

*puiHeight* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the pixel height of the bitmap

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



 

 




