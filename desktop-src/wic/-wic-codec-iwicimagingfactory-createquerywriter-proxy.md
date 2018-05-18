---
Description: 'Proxy function for the CreateQueryWriter method.'
ms.assetid: '7f925117-6244-4be6-bcef-fa852672ac64'
title: 'IWICImagingFactory\_CreateQueryWriter\_Proxy function'
---

# IWICImagingFactory\_CreateQueryWriter\_Proxy function

Proxy function for the [**CreateQueryWriter**](-wic-codec-iwicimagingfactory-createquerywriter.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateQueryWriter_Proxy(
  _In_        IWICImagingFactory      *pFactory,
  _In_        REFGUID                 guidMetadataFormat,
  _In_  const GUID                    *pguidVendor,
  _Out_       IWICMetadataQueryWriter **ppIQueryWriter
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

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

Type: **[**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md)\*\***

A pointer that receives a pointer to a new [**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md).

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



 

 




