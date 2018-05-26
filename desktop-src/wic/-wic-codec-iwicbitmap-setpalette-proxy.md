---
Description: Proxy function for the SetPalette method.
ms.assetid: 3fd60833-7f21-4654-883a-2dd88c403bc8
title: IWICBitmap\_SetPalette\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmap\_SetPalette\_Proxy function

Proxy function for the [**SetPalette**](/windows/win32/Wincodec/nf-wincodec-iwicbitmap-setpalette?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmap_SetPalette_Proxy(
  _In_ IWICBitmap  *THIS_PTR,
  _In_ IWICPalette *pIPalette
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master)\***

Pointer to this [**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master) object.

</dd> <dt>

*pIPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master)\***

The palette to use for conversion.

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



 

 




