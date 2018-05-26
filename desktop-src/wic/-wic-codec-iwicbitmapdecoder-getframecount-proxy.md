---
Description: Proxy function for the GetFrameCount method.
ms.assetid: 2103af73-60a2-4c1c-8db2-7dfd474440eb
title: IWICBitmapDecoder\_GetFrameCount\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapDecoder\_GetFrameCount\_Proxy function

Proxy function for the [**GetFrameCount**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getframecount?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetFrameCount_Proxy(
  _In_  IWICBitmapDecoder *THIS_PTR,
  _Out_ UINT              *pCount
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)\***

Pointer to this [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) object.

</dd> <dt>

*pCount* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the total number of frames in the image.

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



 

 




