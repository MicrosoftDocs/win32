---
Description: 'Proxy function for the CreateFormatConverter method.'
ms.assetid: '1013720a-d00e-4381-af5d-747806546692'
title: 'IWICImagingFactory\_CreateFormatConverter\_Proxy function'
---

# IWICImagingFactory\_CreateFormatConverter\_Proxy function

Proxy function for the [**CreateFormatConverter**](-wic-codec-iwicimagingfactory-createformatconverter.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateFormatConverter_Proxy(
  _In_  IWICImagingFactory  *pFactory,
  _Out_ IWICFormatConverter **ppIFormatConverter
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*ppIFormatConverter* \[out\]
</dt> <dd>

Type: **[**IWICFormatConverter**](-wic-codec-iwicformatconverter.md)\*\***

A pointer that receives a pointer to a new [**IWICFormatConverter**](-wic-codec-iwicformatconverter.md).

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



 

 




