---
Description: 'Proxy function for the InitializeFromPalette method.'
ms.assetid: 'e7156cae-8d59-4dbd-8845-0e892e10107b'
title: 'IWICPalette\_InitializeFromPalette\_Proxy function'
---

# IWICPalette\_InitializeFromPalette\_Proxy function

Proxy function for the [**InitializeFromPalette**](-wic-codec-iwicpalette-initializefrompalette.md) method.

## Syntax


```C++
HRESULT IWICPalette_InitializeFromPalette_Proxy(
  _In_ IWICPalette *THIS_PTR,
  _In_ IWICPalette *pIMILPalette
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

Pointer to this [**IWICPalette**](-wic-codec-iwicpalette.md) object.

</dd> <dt>

*pIMILPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

Pointer to the source palette.

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



 

 




