---
Description: Proxy function for the Initialize method.
ms.assetid: 60925f5c-aca4-4f49-96d2-9b58d8310e3c
title: IWICBitmapClipper\_Initialize\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapClipper\_Initialize\_Proxy function

Proxy function for the [**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapclipper-initialize?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapClipper_Initialize_Proxy(
  _In_       IWICBitmapClipper *THIS_PTR,
  _In_       IWICBitmapSource  *pISource,
  _In_ const WICRect           *prc
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapClipper**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapclipper?branch=master)\***

Pointer to this [**IWICBitmapClipper**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapclipper?branch=master) object.

</dd> <dt>

*pISource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

The input bitmap source.

</dd> <dt>

*prc* \[in\]
</dt> <dd>

Type: **const [**WICRect**](/windows/win32/Wincodec/ns-wincodec-wicrect?branch=master)\***

The rectangle of the bitmap source to clip.

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



 

 




