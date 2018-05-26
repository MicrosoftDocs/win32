---
Description: Proxy function for the CreateQueryWriterFromBlockWriter method.
ms.assetid: f941e3b1-1645-4ed6-b2c5-180cb4c43fca
title: IWICComponentFactory\_CreateQueryWriterFromBlockWriter\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICComponentFactory\_CreateQueryWriterFromBlockWriter\_Proxy function

Proxy function for the [**CreateQueryWriterFromBlockWriter**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwiccomponentfactory-createquerywriterfromblockwriter?branch=master) method.

## Syntax


```C++
HRESULT IWICComponentFactory_CreateQueryWriterFromBlockWriter_Proxy(
  _In_  IWICComponentFactory    *THIS_PTR,
  _In_  IWICMetadataBlockWriter *pIBlockWriter,
  _Out_ IWICMetadataQueryWriter **ppIQueryWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master)\***

Pointer to this [**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master) object.

</dd> <dt>

*pIBlockWriter* \[in\]
</dt> <dd>

Type: **[**IWICMetadataBlockWriter**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter?branch=master)\***

</dd> <dt>

*ppIQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master)\*\***

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



 

 




