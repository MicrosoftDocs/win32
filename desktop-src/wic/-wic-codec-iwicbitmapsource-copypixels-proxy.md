---
Description: Proxy function for the CopyPixels method.
ms.assetid: 020c11e9-0847-468e-b240-20529f6460cd
title: IWICBitmapSource\_CopyPixels\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapSource\_CopyPixels\_Proxy function

Proxy function for the [**CopyPixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapsource-copypixels?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapSource_CopyPixels_Proxy(
  _In_        IWICBitmapSource *THIS_PTR,
  _In_  const WICRect          *prc,
  _In_        UINT             cbStride,
  _In_        UINT             cbBufferSize,
  _Out_       BYTE             *pbBuffer
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master)\***

Pointer to this [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) object.

</dd> <dt>

*prc* \[in\]
</dt> <dd>

Type: **const [**WICRect**](/windows/win32/Wincodec/ns-wincodec-wicrect?branch=master)\***

The rectangle to copy. A NULL value specifies the entire bitmap.

</dd> <dt>

*cbStride* \[in\]
</dt> <dd>

Type: **UINT**

The stride of the bitmap

</dd> <dt>

*cbBufferSize* \[in\]
</dt> <dd>

Type: **UINT**

The size of the buffer.

</dd> <dt>

*pbBuffer* \[out\]
</dt> <dd>

Type: **BYTE\***

A pointer to the buffer.

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



 

 




