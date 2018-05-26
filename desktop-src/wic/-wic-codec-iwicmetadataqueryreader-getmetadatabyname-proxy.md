---
Description: Proxy function for the GetMetadataByName method.
ms.assetid: 5685e282-637e-4db0-8654-fee12ae25112
title: IWICMetadataQueryReader\_GetMetadataByName\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICMetadataQueryReader\_GetMetadataByName\_Proxy function

Proxy function for the [**GetMetadataByName**](/windows/win32/Wincodec/nf-wincodec-iwicmetadataqueryreader-getmetadatabyname?branch=master) method.

## Syntax


```C++
HRESULT IWICMetadataQueryReader_GetMetadataByName_Proxy(
  _In_    IWICMetadataQueryReader *THIS_PTR,
  _In_    LPCWSTR                 wzName,
  _Inout_ PROPVARIANT             *pvarValue
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master)\***

Pointer to this [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master) object.

</dd> <dt>

*wzName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The name of the requested metadata item.

</dd> <dt>

*pvarValue* \[in, out\]
</dt> <dd>

Type: **[PROPVARIANT](http://msdn.microsoft.com/en-us/library/Aa380072(VS.85).aspx)\***

Pointer that receives the metadata property.

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



 

 




