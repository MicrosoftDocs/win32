---
Description: Proxy function for the CreateMetadataWriterFromReader method.
ms.assetid: da9e80d3-3265-428d-987e-8b344472527a
title: IWICComponentFactory\_CreateMetadataWriterFromReader\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICComponentFactory\_CreateMetadataWriterFromReader\_Proxy function

Proxy function for the [**CreateMetadataWriterFromReader**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwiccomponentfactory-createmetadatawriterfromreader?branch=master) method.

## Syntax


```C++
HRESULT IWICComponentFactory_CreateMetadataWriterFromReader_Proxy(
  _In_        IWICComponentFactory *THIS_PTR,
  _In_        IWICMetadataReader   *pIReader,
  _In_  const GUID                 *pguidVendor,
  _Out_       IWICMetadataWriter   **ppIWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master)\***

Pointer to this [**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master) object.

</dd> <dt>

*pIReader* \[in\]
</dt> <dd>

Type: **[**IWICMetadataReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatareader?branch=master)\***

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

</dd> <dt>

*ppIWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataWriter**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter?branch=master)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




