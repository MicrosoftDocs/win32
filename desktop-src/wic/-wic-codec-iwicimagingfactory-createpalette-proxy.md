---
description: Proxy function for the CreatePalette method.
ms.assetid: c83b4239-ce6b-4a4c-ab70-df31dfcdd26c
title: IWICImagingFactory_CreatePalette_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICImagingFactory_CreatePalette_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICImagingFactory\_CreatePalette\_Proxy function

Proxy function for the [**CreatePalette**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createpalette) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreatePalette_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICPalette        **ppIPalette
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)\***

</dd> <dt>

*ppIPalette* \[out\]
</dt> <dd>

Type: **[**IWICPalette**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpalette)\*\***

A pointer that receives a pointer to a new [**IWICPalette**](/windows/desktop/api/Wincodec/nn-wincodec-iwicpalette).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




