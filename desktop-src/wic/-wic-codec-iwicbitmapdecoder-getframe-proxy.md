---
Description: Proxy function for the GetFrame method.
ms.assetid: 31612afa-5017-4ddb-bdf8-25555db35da5
title: IWICBitmapDecoder\_GetFrame\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapDecoder\_GetFrame\_Proxy function

Proxy function for the [**GetFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getframe?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetFrame_Proxy(
  _In_  IWICBitmapDecoder     *THIS_PTR,
  _In_  UINT                  index,
  _Out_ IWICBitmapFrameDecode **ppIBitmapFrame
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)\***

Pointer to this [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) object.

</dd> <dt>

*index* \[in\]
</dt> <dd>

Type: **UINT**

The particular frame to retrieve.

</dd> <dt>

*ppIBitmapFrame* \[out\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master)\*\***

A pointer that receives a pointer to the [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master).

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



 

 




