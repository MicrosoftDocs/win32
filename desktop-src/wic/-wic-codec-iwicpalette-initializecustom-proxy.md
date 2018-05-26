---
Description: Proxy function for the InitializeCustom method.
ms.assetid: fe742b12-5338-41b0-b90b-aec852a26518
title: IWICPalette\_InitializeCustom\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICPalette\_InitializeCustom\_Proxy function

Proxy function for the [**InitializeCustom**](/windows/win32/Wincodec/nf-wincodec-iwicpalette-initializecustom?branch=master) method.

## Syntax


```C++
HRESULT IWICPalette_InitializeCustom_Proxy(
  _In_ IWICPalette *THIS_PTR,
  _In_ WICColor    *pColors,
  _In_ UINT        colorCount
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master)\***

Pointer to this [**IWICPalette**](/windows/win32/Wincodec/nn-wincodec-iwicpalette?branch=master) object.

</dd> <dt>

*pColors* \[in\]
</dt> <dd>

Type: **WICColor\***

Pointer to the color array.

</dd> <dt>

*colorCount* \[in\]
</dt> <dd>

Type: **UINT**

The number of colors in *pColors*.

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



 

 




