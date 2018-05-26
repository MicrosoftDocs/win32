---
Description: Proxy function for the GetContainerFormat method.
ms.assetid: d8a2387a-fb75-4812-b046-51359071281d
title: IWICBitmapCodecInfo\_GetContainerFormat\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmapCodecInfo\_GetContainerFormat\_Proxy function

Proxy function for the [**GetContainerFormat**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapcodecinfo-getcontainerformat?branch=master) method.

## Syntax


```C++
HRESULT IWICBitmapCodecInfo_GetContainerFormat_Proxy(
  _In_  IWICBitmapCodecInfo *THIS_PTR,
  _Out_ GUID                *pguidContainerFormat
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapCodecInfo**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapcodecinfo?branch=master)\***

Pointer to this [**IWICBitmapCodecInfo**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapcodecinfo?branch=master) object.

</dd> <dt>

*pguidContainerFormat* \[out\]
</dt> <dd>

Type: **GUID\***

A pointer that receives the container GUID.

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



 

 




