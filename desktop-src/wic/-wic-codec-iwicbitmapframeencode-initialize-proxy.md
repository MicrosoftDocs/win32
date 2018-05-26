---
Description: Proxy function for the Initialize method.
ms.assetid: af9e204c-7072-47b8-84eb-47a754968d5b
title: IWICBitmapFrameEncode\_Initialize\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapFrameEncode\_Initialize\_Proxy function

Proxy function for the [**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-initialize?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapFrameEncode_Initialize_Proxy(
  _In_ IWICBitmapFrameEncode *THIS_PTR,
  _In_ IPropertyBag2         *pIEncoderOptions
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)\***

Pointer to this [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) object.

</dd> <dt>

*pIEncoderOptions* \[in\]
</dt> <dd>

Type: **[IPropertyBag2](http://msdn.microsoft.com/en-us/library/Aa768192(VS.85).aspx)\***

The set of properties to use for [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) initialization.

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



 

 




