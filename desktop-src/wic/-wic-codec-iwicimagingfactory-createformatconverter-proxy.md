---
description: Proxy function for the CreateFormatConverter method.
ms.assetid: 1013720a-d00e-4381-af5d-747806546692
title: IWICImagingFactory_CreateFormatConverter_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICImagingFactory_CreateFormatConverter_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICImagingFactory\_CreateFormatConverter\_Proxy function

Proxy function for the [**CreateFormatConverter**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createformatconverter) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateFormatConverter_Proxy(
  _In_  IWICImagingFactory  *pFactory,
  _Out_ IWICFormatConverter **ppIFormatConverter
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)\***

</dd> <dt>

*ppIFormatConverter* \[out\]
</dt> <dd>

Type: **[**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter)\*\***

A pointer that receives a pointer to a new [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter).

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



 

 




