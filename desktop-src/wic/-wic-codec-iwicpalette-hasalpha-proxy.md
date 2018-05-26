---
Description: Proxy function for the HasAlpha method.
ms.assetid: 8af9f588-ac22-40c4-8973-9636951cc9e6
title: IWICPalette\_HasAlpha\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICPalette\_HasAlpha\_Proxy function

Proxy function for the [**HasAlpha**](/windows/win32/Wincodec/nf-wincodec-iwicpalette-hasalpha?branch=master) method.

## Syntax


```C++
HRESULT IWICPalette_HasAlpha_Proxy(
  _In_  IWICPalette *THIS_PTR,
  _Out_ BOOL        *pfHasAlpha
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master)\***

Pointer to this [**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master) object.

</dd> <dt>

*pfHasAlpha* \[out\]
</dt> <dd>

Type: **BOOL\***

Pointer that receives `TRUE` if the palette contains a transparent color; otherwise, `FALSE`.

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



 

 




