---
Description: 'Proxy function for the CreateQueryWriterFromReader method.'
ms.assetid: '7784c5e9-38e0-43de-83db-4de3361fa20e'
title: 'IWICImagingFactory\_CreateQueryWriterFromReader\_Proxy function'
---

# IWICImagingFactory\_CreateQueryWriterFromReader\_Proxy function

Proxy function for the [**CreateQueryWriterFromReader**](-wic-codec-iwicimagingfactory-createquerywriterfromreader.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateQueryWriterFromReader_Proxy(
  _In_        IWICImagingFactory      *pFactory,
  _In_        IWICMetadataQueryReader *pIQueryReader,
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

*pIQueryReader* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](-wic-codec-iwicmetadataqueryreader.md)\***

The metadata query reader to create the metadata writer from.

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

The vendor GUID for the metadata query writer.

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



 

 




