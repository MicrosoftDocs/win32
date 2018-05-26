---
Description: Proxy function for the GetColors method.
ms.assetid: 31590de3-f35c-4253-9a80-2f59c795bf3f
title: IWICPalette\_GetColors\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICPalette\_GetColors\_Proxy function

Proxy function for the [**GetColors**](/windows/win32/Wincodec/nf-wincodec-iwicpalette-getcolors?branch=master) method.

## Syntax


```C++
HRESULT IWICPalette_GetColors_Proxy(
  _In_  IWICPalette *THIS_PTR,
  _In_  UINT        colorCount,
  _Out_ WICColor    *pColors,
  _Out_ UINT        *pcActualColors
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master)\***

Pointer to this [**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master) object.

</dd> <dt>

*colorCount* \[in\]
</dt> <dd>

Type: **UINT**

The size of the *pColors* array.

</dd> <dt>

*pColors* \[out\]
</dt> <dd>

Type: **WICColor\***

Pointer that receives the colors of the palette.

</dd> <dt>

*pcActualColors* \[out\]
</dt> <dd>

Type: **UINT\***

The actual size needed to obtain the palette colors.

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



 

 




