---
Description: 'Proxy function for the CreateMetadataWriterFromReader method.'
ms.assetid: 'da9e80d3-3265-428d-987e-8b344472527a'
title: 'IWICComponentFactory\_CreateMetadataWriterFromReader\_Proxy function'
---

# IWICComponentFactory\_CreateMetadataWriterFromReader\_Proxy function

Proxy function for the [**CreateMetadataWriterFromReader**](-wic-codec-iwiccomponentfactory-createmetadatawriterfromreader.md) method.

## Syntax


```C++
HRESULT IWICComponentFactory_CreateMetadataWriterFromReader_Proxy(
  _In_        IWICComponentFactory *THIS_PTR,
  _In_        IWICMetadataReader   *pIReader,
  _In_  const GUID                 *pguidVendor,
  _Out_       IWICMetadataWriter   **ppIWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICComponentFactory**](-wic-codec-iwiccomponentfactory.md)\***

Pointer to this [**IWICComponentFactory**](-wic-codec-iwiccomponentfactory.md) object.

</dd> <dt>

*pIReader* \[in\]
</dt> <dd>

Type: **[**IWICMetadataReader**](-wic-codec-iwicmetadatareader.md)\***

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

</dd> <dt>

*ppIWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataWriter**](-wic-codec-iwicmetadatawriter.md)\*\***

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



 

 




