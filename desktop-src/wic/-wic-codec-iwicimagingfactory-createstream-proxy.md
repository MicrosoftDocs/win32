---
Description: 'Proxy function for the CreateStream method.'
ms.assetid: 'c827e1aa-13ae-459e-a1dc-5ff8c31a54bc'
title: 'IWICImagingFactory\_CreateStream\_Proxy function'
---

# IWICImagingFactory\_CreateStream\_Proxy function

Proxy function for the [**CreateStream**](-wic-codec-iwicimagingfactory-createstream.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateStream_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _Out_ IWICStream         **ppIWICStream
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*ppIWICStream* \[out\]
</dt> <dd>

Type: **[**IWICStream**](-wic-codec-iwicstream.md)\*\***

A pointer that receives a pointer to a new [**IWICStream**](-wic-codec-iwicstream.md).

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



 

 




