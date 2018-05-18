---
Description: 'Proxy function for the CreatePalette method.'
ms.assetid: 'c83b4239-ce6b-4a4c-ab70-df31dfcdd26c'
title: 'IWICImagingFactory\_CreatePalette\_Proxy function'
---

# IWICImagingFactory\_CreatePalette\_Proxy function

Proxy function for the [**CreatePalette**](-wic-codec-iwicimagingfactory-createpalette.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreatePalette_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICPalette        **ppIPalette
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*ppIPalette* \[out\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\*\***

A pointer that receives a pointer to a new [**IWICPalette**](-wic-codec-iwicpalette.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




