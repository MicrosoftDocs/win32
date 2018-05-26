---
Description: Proxy function for the Commit method.
ms.assetid: 605801e5-00f8-4e4f-87d3-ad34d3568ee5
title: IWICBitmapFrameEncode\_Commit\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapFrameEncode\_Commit\_Proxy function

Proxy function for the [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapFrameEncode_Commit_Proxy(
  _In_ IWICBitmapFrameEncode *THIS_PTR
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)\***

Pointer to this [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) object.

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



 

 




