---
description: Proxy function for the CreateQueryWriter method.
ms.assetid: 7f925117-6244-4be6-bcef-fa852672ac64
title: IWICImagingFactory_CreateQueryWriter_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICImagingFactory_CreateQueryWriter_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICImagingFactory\_CreateQueryWriter\_Proxy function

Proxy function for the [**CreateQueryWriter**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createquerywriter) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateQueryWriter_Proxy(
  _In_        IWICImagingFactory      *pFactory,
  _In_        REFGUID                 guidMetadataFormat,
  _In_  const GUID                    *pguidVendor,
  _Out_       IWICMetadataQueryWriter **ppIQueryWriter
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)\***

</dd> <dt>

*guidMetadataFormat* \[in\]
</dt> <dd>

Type: **REFGUID**

The GUID for the desired metadata format.

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

The vendor GUID of the metadata writer.

</dd> <dt>

*ppIQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter)\*\***

A pointer that receives a pointer to a new [**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter).

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



 

 




