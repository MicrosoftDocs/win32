---
Description: Proxy function for the GetChannelCount method.
ms.assetid: f74916d9-d4b5-4b1b-adba-489d46c8d81c
title: IWICPixelFormatInfo\_GetChannelCount\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICPixelFormatInfo\_GetChannelCount\_Proxy function

Proxy function for the [**GetChannelCount**](/windows/win32/Wincodec/nf-wincodec-iwicpixelformatinfo-getchannelcount?branch=master) method.

## Syntax


```C++
HRESULT IWICPixelFormatInfo_GetChannelCount_Proxy(
  _In_  IWICPixelFormatInfo *THIS_PTR,
  _Out_ UINT                *puiChannelCount
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPixelFormatInfo**](/windows/win32/Wincodec/nn-wincodec-iwicpixelformatinfo?branch=master)\***

Pointer to this [**IWICPixelFormatInfo**](/windows/win32/Wincodec/nn-wincodec-iwicpixelformatinfo?branch=master) object.

</dd> <dt>

*puiChannelCount* \[out\]
</dt> <dd>

Type: **UINT\***

Pointer that receives the channel count.

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



 

 




