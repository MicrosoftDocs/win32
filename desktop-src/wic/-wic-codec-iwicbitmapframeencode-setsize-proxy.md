---
Description: Proxy function for the SetSize method.
ms.assetid: 28b4967f-4c8a-475c-8f86-c19e5d424a26
title: IWICBitmapFrameEncode\_SetSize\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapFrameEncode\_SetSize\_Proxy function

Proxy function for the [**SetSize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-setsize?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapFrameEncode_SetSize_Proxy(
  _In_ IWICBitmapFrameEncode *THIS_PTR,
  _In_ UINT                  uiWidth,
  _In_ UINT                  uiHeight
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)\***

Pointer to this [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) object.

</dd> <dt>

*uiWidth* \[in\]
</dt> <dd>

Type: **UINT**

The width of the output image.

</dd> <dt>

*uiHeight* \[in\]
</dt> <dd>

Type: **UINT**

The height of the output image.

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



 

 




