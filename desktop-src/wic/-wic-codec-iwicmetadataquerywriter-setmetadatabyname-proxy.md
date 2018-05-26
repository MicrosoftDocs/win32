---
Description: Proxy function for the SetMetadataByName method.
ms.assetid: 467d7735-152a-4e7c-93b1-fd031cc57c19
title: IWICMetadataQueryWriter\_SetMetadataByName\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICMetadataQueryWriter\_SetMetadataByName\_Proxy function

Proxy function for the [**SetMetadataByName**](/windows/win32/Wincodec/nf-wincodec-iwicmetadataquerywriter-setmetadatabyname?branch=master) method.

## Syntax


```C++
HRESULT IWICMetadataQueryWriter_SetMetadataByName_Proxy(
  _In_       IWICMetadataQueryWriter *THIS_PTR,
  _In_       LPCWSTR                 wzName,
  _In_ const PROPVARIANT             *pvarValue
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master)\***

Pointer to this [**IWICMetadataQueryWriter**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataquerywriter?branch=master) object.

</dd> <dt>

*wzName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The name of the metadata item.

</dd> <dt>

*pvarValue* \[in\]
</dt> <dd>

Type: **const [PROPVARIANT](http://msdn.microsoft.com/en-us/library/Aa380072(VS.85).aspx)\***

The metadata to set.

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



 

 




